# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install build dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire backend project
COPY . .

# Install dependencies from pyproject.toml
RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "prp_core.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]

