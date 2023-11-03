from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates")

class UserInput(BaseModel):
    input: str
    target: str | None