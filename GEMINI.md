# GEMINI Project Context

This document provides context for the Gemini AI assistant to understand the project structure, technologies, and development conventions.

## Project Overview

This is a full-stack personal finance application designed to track financial accounts and calculate net worth. The project is containerized using Docker and consists of three main services: a PostgreSQL database, a Python backend, and a SvelteKit frontend.

### Technologies Used

*   **Backend:**
    *   Python 3.10+
    *   FastAPI
    *   SQLAlchemy for ORM
    *   PostgreSQL for the database
    *   `uvicorn` as the ASGI server

*   **Frontend:**
    *   SvelteKit
    *   TypeScript
    *   Tailwind CSS
    *   Vite for the build tool

*   **Orchestration:**
    *   Docker Compose

### Architecture

The application is architected as a three-tier system:

1.  **Database:** A PostgreSQL container (`db`) stores all the application data.
2.  **Backend:** A FastAPI application (`backend`) provides a RESTful API for the frontend. It handles business logic and database interactions. The API is accessible on port 8000 and is prefixed with `/api/v1`.
3.  **Frontend:** A SvelteKit application (`frontend`) provides the user interface. It runs on port 5173 and communicates with the backend API.

## Building and Running

The entire application can be built and run using Docker Compose:

```sh
docker-compose up --build
```

### Frontend Development

To run the frontend development server:

```sh
cd frontend
npm install
npm run dev
```

The frontend will be available at `http://localhost:5173`.

### Backend Development

The backend is a Python project. To run it locally, you'll need to set up a Python environment and install the dependencies from `backend/pyproject.toml`.

```sh
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn prp_core.main:app --reload
```

The backend API will be available at `http://localhost:8000`.

## Development Conventions

*   **API:** The backend exposes a RESTful API at `/api/v1/`.
*   **Styling:** The frontend uses Tailwind CSS for styling.
*   **Typing:** The frontend uses TypeScript.
*   **Database:** Database migrations are handled by SQLAlchemy's `metadata.create_all` on application startup. For more complex migrations, a dedicated migration tool might be needed in the future.
