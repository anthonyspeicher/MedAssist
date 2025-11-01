from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import uuid

UPLOAD_DIR = Path("../uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
        with open((UPLOAD_DIR / f"{uuid.uuid4()}_{file.filename}"), "wb") as f:
                f.write(await file.read())
        return {"filename": file.filename, "status":"saved"}
