from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from analyze import analyze_image
from database import localSession, Analysis
from sqlalchemy.orm import Session
from PIL import Image, UnidentifiedImageError
import os
from pathlib import Path
import uuid

app = FastAPI(title="Chest X-Ray Diagnostic API")

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

# fix to only allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Chest X-Ray Analyzer API is running."}

@app.post("/analyze")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # save file
    NEW_NAME = f"{uuid.uuid4()}_{file.filename}"
    with open((Path("../uploads") / NEW_NAME), "wb") as f:
        f.write(await file.read())

    # is random placeholder function currently
    result = analyze_image(file.file)

    # db entry with correct column names this time
    db_entry = Analysis(
        filename=NEW_NAME,
        result=result["condition"],
        confidence=result["confidence"]
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

    # return id/result
    return {
        "message": "Analysis complete",
        "id": db_entry.id,
        "result": result
    }
