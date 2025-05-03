from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from utils.template import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

