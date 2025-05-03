# app/api/routes/home.py

from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.concat import concat_csv_files  # Import the concat function
from typing import List


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/concat", response_class=HTMLResponse)
async def trigger_concat(request: Request, files: List[UploadFile] = File(...)):
    try:
        # Pass the uploaded files to the concat function
        combined_df = concat_csv_files(files)
        # Convert the resulting dataframe to HTML to display in the template
        message = combined_df.to_html(classes="table table-striped")
    except Exception as e:
        message = f"Error during concatenation: {str(e)}"
    
    return templates.TemplateResponse("index.html", {"request": request, "message": message})
