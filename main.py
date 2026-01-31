from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from weasyprint import HTML
import os

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
def view_resume():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/resume", response_class=HTMLResponse)
def view_resume():
    with open("templates/resume.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/download-pdf")
def download_pdf():
    html_path = os.path.abspath("templates/resume.html")

    pdf_bytes = HTML(filename=html_path).write_pdf()

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=Rohit_Kumar_AI_ML_Engineer.pdf"
        }
    )
