FROM python:3.12-slim AS base

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the application port
EXPOSE 8000

# Base CMD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Development Stage
FROM base AS dev
RUN pip install watchdog
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
