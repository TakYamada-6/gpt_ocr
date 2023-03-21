import os
from pathlib import Path
from llama_index import download_loader

PDF_FILE = Path(r"\Users\yamad\Downloads\会員検索 ｜ BU2680284 の職務経歴 - ビズリーチ.pdf")
SAVE_DIR = Path(r'./resumes')


def pdf_to_text(pdf_file):
    CJKPDFReader = download_loader("CJKPDFReader")

    loader = CJKPDFReader()
    documents = loader.load_data(file=pdf_file)
    return documents[0].text


def find_resume(text):
    index = text.find("職務要約")
    resume = text[index:]
    return resume


def find_user_name(file_name):
    start_word = "B"
    end_word = "の"
    file_name = os.path.basename(file_name)

    start_index = file_name.find(start_word)
    if start_index == -1:
        print(f"{start_word}が見つかりませんでした。")
        exit()

    end_index = file_name.find(end_word)
    if end_index == -1:
        print(f"{end_word}が見つかりませんでした。")
        exit()

    user_name = file_name[(start_index - 1) + len(start_word):end_index].replace(" ", "")
    print(user_name)
    return user_name


def read_pdf(file_name, pdf_file):
    user_name = find_user_name(file_name)
    resume_text = find_resume(pdf_to_text(pdf_file))

    return user_name, resume_text

