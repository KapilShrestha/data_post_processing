from fastapi import APIRouter, Request, UploadFile, File
from typing import List

from fastapi.responses import HTMLResponse
from services.concat import concat_csv_files

from utils.template import templates

router = APIRouter()


# GET endpoint to serve the upload form
@router.get("/concat", response_class=HTMLResponse)
async def get_concat_form(request: Request):
    return templates.TemplateResponse(
        "concat.html", {"request": request, "message": ""}
    )


# POST endpoint to process uploaded files
@router.post("/concat", response_class=HTMLResponse)
async def trigger_concat(request: Request, files: List[UploadFile] = File(...)):
    try:
        print("===> Files received:")
        for f in files:
            print(f"Type: {type(f)}, Filename: {getattr(f, 'filename', 'N/A')}")

        df = concat_csv_files(files)
        message = df.to_html()
    except Exception as e:
        print(f"===> ERROR: {str(e)}")
        message = f"Concatenation failed: {str(e)}"

    return templates.TemplateResponse(
        "concat.html", {"request": request, "message": message}
    )
