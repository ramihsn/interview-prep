# interview-prep

## Overview

This project is designed to help users prepare for interviews by providing a platform to manage questions and answers. It consists of a frontend built with Vue.js and a backend built with FastAPI.

## Frontend

The frontend is developed using Vue 3 and Vite. It provides a user-friendly interface for interacting with the interview preparation platform.

### Main Technologies

- [Vue 3](https://vuejs.org/guide/quick-start)
- [Vite](https://vite.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [daisyUI](https://daisyui.com/)

### Project Setup

```sh
cd frontend
npm install
```

Compile and Hot-Reload for Development
```sh
npm run dev
```

Type-Check, Compile and Minify for Production
```sh
npm run build
```

Lint with ESLint
```sh
npm run lint
```

### Backend
The backend is developed using FastAPI. It provides a RESTful API for managing questions and answers, and handles file uploads for bulk question imports.

### Main Technologies
- [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/)
- [SQLite](https://www.sqlite.org/)
- [openPyXL](https://openpyxl.readthedocs.io/en/stable/)

### Project Setup
Run the Application
```sh
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### TODOs
- [ ] Improve the UI/UX of the frontend
- [ ] Write unit tests for frontend
- [ ] Write unit tests for backend
- [ ] Write e2e tests
- [x] Add support for csv file as an input
- [x] Add support for json file as an input
- [x] Add support for excel file as an input
- [ ] Add support for more file types in the file uploader - TBD
- [ ] Implement a search functionality for questions
- [ ] Optimize database queries for better performance
- [ ] Remove SQLAlchemy and use SQLModel instead
- [ ] Group the questions by the topic or difficulty
- [ ] Enable editing a question
