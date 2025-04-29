from fastapi import APIRouter, Request
from starlette.responses import RedirectResponse  # Import from starlette
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.services.merge import merge_files  # Import the merge function from merge.py

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    message = "Welcome to the homepage!"
    return templates.TemplateResponse("index.html", {"request": request, "message": message})

@router.get("/merge", response_class=HTMLResponse)
async def merge_page(request: Request):
    return templates.TemplateResponse("merge.html", {"request": request})

@router.post("/merge", response_class=HTMLResponse)
async def trigger_merge(request: Request):
    try:
        merge_files()  # Assume this function handles merging logic
        message = "Merge was successful!"
    except Exception as e:
        message = f"Merge failed: {str(e)}"
    return templates.TemplateResponse("merge.html", {"request": request, "message": message})

@router.get("/back", response_class=RedirectResponse)  # Example of RedirectResponse
async def back_to_homepage():
    return RedirectResponse(url="/")
