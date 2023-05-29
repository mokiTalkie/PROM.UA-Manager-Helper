from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.additional import additional
from routes.tools import tools

app = FastAPI(debug=False, title="PromCat")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(additional)
app.include_router(tools)
