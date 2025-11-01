from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.routes import upload
from PIL import Image, UnidentifiedImageError
import io
import os

app = FastAPI(title="Chest X-Ray Diagnostic API")

# Allow all origins for now (for local testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Chest X-Ray Analyzer API is running."}
