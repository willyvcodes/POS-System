from ast import main
from math import prod
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from routes.base import main_router

app = FastAPI(
    title="POS SYSTEM API",
    version="1.0"
)
app.include_router(main_router)

app.mount("/", StaticFiles(directory="site/", html=True), name="site")
app.mount("/build", StaticFiles(directory="site/build"), name="build")

@app.get("/", tags=['Root'])
async def read_root():
    return RedirectResponse("/")