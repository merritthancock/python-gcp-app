from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allows your future frontend to communicate with this backend API securely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "backend is running smoothly"}

@app.get("/api/greet")
def greet():
    return {"message": "Hello from your cloud-hosted FastAPI backend!"}