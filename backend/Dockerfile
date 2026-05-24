FROM python:3.11-slim

WORKDIR /app

# 1. Pull requirements from the backend folder
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the backend directory structure into the container
COPY backend/ backend/

EXPOSE 8080

# 3. Point Uvicorn directly to the backend.main module
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]