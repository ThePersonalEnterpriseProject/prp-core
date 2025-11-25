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
    *   **Modules:** The backend uses a modular architecture. Features like `finance` and `assets` are self-contained modules in `src/prp_core/modules/`. They can be enabled/disabled via the database.
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
*   **Database:** Database migrations are handled by SQLAlchemy's `metadata.create_all` on application startup.
*   **Fake Data:** A modular `fake_data` service orchestrates seeders from each enabled module. It can be triggered via the `/api/v1/debug/seed` endpoint or the "Developer Tools" section in the frontend Settings page.
*   **Frontend Structure:**
    *   `src/routes/+layout.svelte`: Main layout with Sidebar.
    *   `src/lib/components/ui`: Reusable UI components (Card, Button, Input).
    *   `src/routes/accounts`: Accounts management page.
    *   `src/routes/transactions`: Transactions management page.
    *   `src/routes/assets`: Assets management page.
    *   `src/routes/transactions`: Transactions management page.
    *   `src/routes/assets`: Assets management page.

## Testing Architecture

The project follows a "Fail Fast" testing strategy with three tiers:

1.  **Unit Tests (`backend/tests/unit`)**:
    *   **Scope**: Isolated backend logic (no DB, no network).
    *   **Execution**: Runs during Docker build (`docker build --target test`).
    *   **Command**: `make test-unit`

2.  **Integration Tests (`backend/tests/integration`)**:
    *   **Scope**: Backend API endpoints and database interactions.
    *   **Infrastructure**: Runs in a Docker container connected to a dedicated Postgres service.
    *   **Command**: `make test-int`

3.  **E2E/Frontend Tests (`frontend/src`)**:
    *   **Scope**: Frontend UI components and flows.
    *   **Execution**: Runs using `vitest` inside the frontend container.
    *   **Command**: `make test-e2e`
