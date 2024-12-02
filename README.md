# interview-prep

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Quick Start with Docker](#quick-start-with-docker)
5. [Frontend](#frontend)
   - [Technologies](#main-technologies)
   - [Local Development Setup](#local-development-setup)
6. [Backend](#backend)
   - [Technologies](#main-technologies-1)
   - [Setup](#project-setup)
7. [TODOs](#todos)
   - [Backend](#backend-1)
   - [Frontend](#frontend-1)
   - [General](#general)
   - [TBD](#tbd)

## Overview

This project is designed to help users prepare for interviews by providing a platform to manage questions and answers.<br>
It consists of a frontend built with Vue.js and a backend built with FastAPI.<br>
The project now includes Docker-based containerization and centralized logging with Loki.<br><br>
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
- Centralized logging with Loki for streamlined debugging and monitoring.

---

## Prerequisites
Before you begin, ensure you have the following installed on your system:
- [Docker](https://docs.docker.com/get-docker/) (for running the project in containers)
- [Node.js 18+](https://nodejs.org/) (for local frontend development)
- [Python 3.12+](https://www.python.org/) (for local backend development)

---

## 
1. Clone the repository:
  ```bash
  git clone <repository-url>
  cd interview-prep
  ```

2. Start all services
  ```bash
  docker-compose up --build -d
  ```

3. Access the services
  * Frontend (development): http://localhost:5173
  * Frontend (production): http://localhost
  * Backend: http://localhost:8000/docs (Swagger UI)
  * Grafana: http://localhost:3000 (default login: admin/admin)
  * Loki: Centralized logging service.

---

## To stop all services
```bash
docker-compose down
```

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
- [PostgreSQL](https://www.postgresql.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/en/stable/)
- [python-logging-loki](https://pypi.org/project/python-logging-loki/)

### Project Setup
Run the Application
```shell
cd backend
pip install -r requirements.txt
uvicorn main:app [--host <HOST>] [--port <PORT>] [--reload]
```

### TODOs:
#### Backend
- ✅ Replace SQLAlchemy with SQLModel
- ✅ add logging services
- ✅ Store user UI preferences
- ✅ Move form SQLite to PostgreSQL
- 🟧 send logs to loki
- ⬜ add alembic for database migrations
- ⬜ Create job endpoint to link between a job and questions
- ⬜ Add user login and subscription
- ⬜ Write unit tests

#### Frontend
- ✅ Add support for csv file as an input
- ✅ Add support for json file as an input
- ✅ Add support for excel file as an input
- ✅ Add the answer to the question card 
- ✅ Implement a grouping functionality for questions
- ✅ Group the questions by the topic or difficulty
- ✅ Enable editing a question
- ⬜ send logs to loki
- ⬜ Implement a search functionality for questions
- ⬜ Write unit tests

#### General
- ✅ add logging services
- ✅ wrap the project with docker and docker-compose
- ⬜ Write e2e tests

#### TBD
- ⬜ create CI/CD
