FROM python:3.11-slim

WORKDIR /app

# 1. Copy requirements from your backend folder directly to /app/
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy the CONTENTS of the backend folder directly to /app/ (flattened)
COPY backend/ .

# 3. Force Python to look at the /app directory for module resolutions
ENV PYTHONPATH=/app

EXPOSE 8080

# 4. Invoke main directly since it is flattened in /app/main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]