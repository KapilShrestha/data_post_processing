# app/api/routes/merge.py

from fastapi import APIRouter, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from services.merge import merge_files  # Import the merge function
from typing import List


router = APIRouter()
templates = Jinja2Templates(directory="templates")

# This route will serve the page for merging CSVs
@router.get("/merge")
async def merge_page(request: Request):
    return templates.TemplateResponse("merge.html", {"request": request})

# This route will handle the merge process when a form is submitted
@router.post("/merge")
async def trigger_merge(request: Request, files: List[UploadFile] = File(...)):
    message = merge_files(files)  # Call the merge function from the service
    return templates.TemplateResponse("merge.html", {"request": request, "message": message})

