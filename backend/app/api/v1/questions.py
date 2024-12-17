from fastapi import HTTPException, Depends, status, Response, UploadFile, File
from typing import Literal
import logging

from app.services import questions as services
from app.schemas import questions as schemas
from app.db.session import get_db
from app.core import file_readers
from . import _api_factory

logger = logging.getLogger(__name__)
router = _api_factory.factory('question', logger, services, schemas)
_INPUT_FILE_TYPES = Literal['csv', 'json', 'excel']


@router.post('/{id}/mark-as-answered', status_code=status.HTTP_202_ACCEPTED, response_class=Response,
             responses={202: {"description": "Question answered"}, 404: {"description": "Question not found"}})
async def mark_question_as_answered(id: int, db=Depends(get_db)) -> None:
    logger.info(f'Marking question with id {id} as answered')
    if not await services.answer_question(db, id):
        raise HTTPException(status_code=404, detail="Question not found")
    return


@router.post('/{id}/mark-as-unanswered', status_code=status.HTTP_202_ACCEPTED, response_class=Response,
             responses={202: {"description": "Question unanswered"}, 404: {"description": "Question not found"}})
async def mark_question_as_unanswered(id: int, db=Depends(get_db)) -> None:
    logger.info(f'Marking question with id {id} as unanswered')
    if not await services.unanswered_question(db, id):
        raise HTTPException(status_code=404, detail="Question not found")


@router.post('/upload-file')
async def upload_file(position_id: int, file_type: _INPUT_FILE_TYPES, file: UploadFile = File(...), db=Depends(get_db)):
    logger.info(f'Uploading file of type {file_type}')
    questions: list[schemas.QuestionCreate] = []
    result: list[schemas.QuestionRead] = []
    try:
        match file_type:
            case 'csv':
                questions = await file_readers.from_csv_file(position_id, file.file)
            case 'json':
                questions = await file_readers.from_json_file(position_id, file.file)
            case 'excel':
                questions = await file_readers.from_excel_file(position_id, file.file)
            case _:
                raise HTTPException(status_code=400, detail="File type not supported")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    for question in questions:
        logger.info(f'Adding question: {question}')
        result.append(await services.create_question(db, question))

    return result
