from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Enterprise RAG API is running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename
    }