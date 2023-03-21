import tempfile
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

from read_pdf import read_pdf
from extract_info import extract_info

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


@app.get("/api")
def read_root():
    return {"Hello": "World"}


@app.post("/api/upload_pdf/", response_model=Dict[str, str])
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {"error": "Invalid file type. Only PDF files are accepted."}

    # PDFファイルのデータを読み込む
    pdf_data = await file.read()
    file_name = file.filename

    # 一時ファイルを作成し、PDFデータを書き込む
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(pdf_data)
        temp_file_path = temp_file.name

    user_name, resume_text = read_pdf(file_name, temp_file_path)
    summarize_resume = extract_info(resume_text)

    return {
        "user_name": user_name,
        "resume": resume_text,
        "summarize_resume": summarize_resume,
    }
