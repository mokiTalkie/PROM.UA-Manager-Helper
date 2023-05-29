from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from routes import templates

additional = APIRouter(prefix="", default_response_class=HTMLResponse)


@additional.get("/")
async def index(request: Request) -> str:
    """
    Render the index page.
    """
    return templates.TemplateResponse(name="index.html", context={"request": request})


@additional.get("/about")
async def about(request: Request) -> str:
    """
    Render the about page.
    """
    return templates.TemplateResponse(name="about.html", context={"request": request})


@additional.get("/contacts")
async def contacts(request: Request) -> str:
    """
    Render the contacts page.
    """
    return templates.TemplateResponse(
        name="contacts.html", context={"request": request}
    )
