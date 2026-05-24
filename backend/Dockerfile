FROM python:3.11-slim

WORKDIR /app

# 1. Pull requirements from the backend folder
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the contents of the backend folder into the container
COPY backend/ .

EXPOSE 8080

# 3. Standard execution since main.py lands in /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]