# interview-prep

## Overview

This project is designed to help users prepare for interviews by providing a platform to manage questions and answers.<br>
It consists of a frontend built with Vue.js and a backend built with FastAPI.<br>
The project now includes Docker-based containerization and centralized logging with Loki and Promtail.<br><br>
I do recommend to use tools like chatGPT for evaluation the answers<br>
by using a prompt like:
> I have an interview at \<COMPANY NAME>, I will post a question with an answer,
> as the interviewer you should give me feedback for my answer...

be creative :wink:

---

## Features
- Frontend built with Vue 3 and styled with Tailwind CSS and daisyUI.
- Backend developed with FastAPI, utilizing SQLAlchemy and SQLite for data persistence.
- Dockerized services for simplified setup and deployment.
- Centralized logging with Loki and Promtail for streamlined debugging and monitoring.

---

## Prerequisites
- Docker
- Node.js (for local frontend development)
- Python 3.12+ (for local backend development)

---

## Quick Start with Docker
### Run All Services with Docker Compose
docker-compose up --build

### Services Overview
- Frontend:
  - Development: http://localhost:5173
  - Production: http://localhost
- Backend: http://localhost:8000
- Grafana: http://localhost:3000 (admin/admin for login)
- Loki: Centralized logging service.
- Promtail: Log collector, configured to send logs to Loki.

---

## Frontend

The frontend is developed using Vue 3 and Vite. It provides a user-friendly interface for interacting with the interview preparation platform.

### Main Technologies
- [Vue 3](https://vuejs.org/guide/quick-start)
- [Vite](https://vite.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [Tailwind CSS](https://tailwindcss.com/)
- [daisyUI](https://daisyui.com/)

### Local Development Setup
For local development without Docker:
```shell
cd frontend
npm install
```

Compile and Hot-Reload for Development:
```shell
npm run dev
```

Type-Check, Compile and Minify for Production:
```shell
npm run build
```

Lint with ESLint:
```shell
npm run lint
```

---

## Backend

The backend is developed using FastAPI. It provides a RESTful API for managing questions and answers, and handles file uploads for bulk question imports.


### Main Technologies
- [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [SQLite](https://www.sqlite.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)

### Project Setup
Run the Application
```shell
cd backend
pip install -r requirements.txt
uvicorn main:app [--host <HOST>] [--port <PORT>] [--reload]
```

### TODOs
- [x] Add support for csv file as an input
- [x] Add support for json file as an input
- [x] Add support for excel file as an input
- [x] Replace SQLAlchemy with SQLModel
- [x] Add the answer to the question card 
- [x] Implement a grouping functionality for questions
- [x] Add support for more file types in the file uploader
- [x] Group the questions by the topic or difficulty
- [x] Enable editing a question
- [x] wrap the project with docker and docker-compose
- [x] add logging services
- [ ] Store user UI preferences
- [ ] Implement a search functionality for questions
- [ ] Write unit tests for frontend
- [ ] Write unit tests for backend
- [ ] Write e2e tests
