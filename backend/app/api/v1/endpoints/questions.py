from fastapi import APIRouter, HTTPException, Depends, status, Response, UploadFile, File

from app import schemas, services, db
from app.core import file_readers

router = APIRouter()


@router.get('/', response_model=list[schemas.questions.QuestionRead])
async def get_questions(skip: int = None, limit: int = None, db=Depends(db.session.get_db)):
    return await services.questions.get_questions(db, skip, limit)


@router.post('/', response_model=schemas.questions.QuestionRead, status_code=status.HTTP_201_CREATED)
async def create_question(question: schemas.questions.QuestionCreate, db=Depends(db.session.get_db)):
    return await services.questions.add_question(db, question)


@router.get('/{question_id}', response_model=schemas.questions.QuestionRead,
            responses={404: {"description": "Question not found"}})
async def get_question(question_id: int, db=Depends(db.session.get_db)):
    if question := await services.questions.get_question(db, question_id):
        return question
    raise HTTPException(status_code=404, detail="Question not found")


@router.put('/{question_id}', response_model=schemas.questions.QuestionRead)
async def update_question(question_id: int, question: schemas.questions.QuestionUpdate, db=Depends(db.session.get_db)):
    return await services.questions.update_question(db, question_id, question)


@router.delete('/{question_id}', response_model=schemas.questions.QuestionRead)
async def delete_question(question_id: int, db=Depends(db.session.get_db)):
    return await services.questions.delete_question(db, question_id)


@router.post('/{question_id}/mark-as-answered', status_code=status.HTTP_202_ACCEPTED, response_class=Response,
             responses={202: {"description": "Question answered"}, 404: {"description": "Question not found"}})
async def mark_question_as_answered(question_id: int, db=Depends(db.session.get_db)) -> None:
    if not await services.questions.answer_question(db, question_id):
        raise HTTPException(status_code=404, detail="Question not found")
    return


@router.post('/{question_id}/mark-as-unanswered', status_code=status.HTTP_202_ACCEPTED, response_class=Response,
             responses={202: {"description": "Question unanswered"}, 404: {"description": "Question not found"}})
async def mark_question_as_unanswered(question_id: int, db=Depends(db.session.get_db)) -> None:
    if not await services.questions.unanswered_question(db, question_id):
        raise HTTPException(status_code=404, detail="Question not found")


@router.post('/upload-file')
async def upload_file(file_type: str, file: UploadFile = File(...)):
    try:
        match file_type:
            case 'csv':
                questions = await file_readers.from_csv_file(file.file)
                return questions
            case 'json':
                questions = await file_readers.from_json_file(file.file)
                return questions
            case _:
                raise HTTPException(status_code=400, detail="File type not supported")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
