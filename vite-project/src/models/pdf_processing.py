import tempfile
from fastapi import UploadFile
from pdf_to_text import pdf_to_text
from extract_info import extract_info


def save_pdf_temporarily(pdf_data: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(pdf_data)
        return temp_file.name


async def process_pdf(file: UploadFile):
    pdf_data = await file.read()
    file_name = file.filename
    temp_file_path = save_pdf_temporarily(pdf_data)
    user_name, resume = pdf_to_text(file_name, temp_file_path)
    summarized_resume = extract_info(resume)
    return user_name, resume, summarized_resume
