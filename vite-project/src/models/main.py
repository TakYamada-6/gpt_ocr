import tempfile
from fastapi import FastAPI, File, UploadFile, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

from pydantic import BaseModel
from pdf_processing import process_pdf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"content": "Hello World!"}


@app.get("/api")
def read_root():
    return {"content": "This is API root."}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


class ExtractedInfo(BaseModel):
    user_name: str
    summarized_resume: str


@app.post("/api/summarize_resume/", response_model=ExtractedInfo)
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "Invalid file type. Only PDF files are accepted."}

    user_name, resume, summarized_resume = await process_pdf(file)

    return ExtractedInfo(
        user_name=user_name,
        summarized_resume=summarized_resume,
    )
