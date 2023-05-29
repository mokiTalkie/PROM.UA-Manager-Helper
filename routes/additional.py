from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

additional = APIRouter(prefix="", default_response_class=HTMLResponse)

templates = Jinja2Templates(directory="templates")


@additional.get("/")
async def index(request: Request) -> str:
    return templates.TemplateResponse(name="index.html", context={"request": request})


@additional.get("/about")
async def about(request: Request) -> str:
    return templates.TemplateResponse(name="about.html", context={"request": request})


@additional.get("/contacts")
async def contacts(request: Request) -> str:
    return templates.TemplateResponse(name="contacts.html", context={"request": request})
