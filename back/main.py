from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="MedAssist AI Backend")

# Allow local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes import upload

app.include_router(upload.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Backend is running"}

