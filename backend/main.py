from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from routes.base import main_router

app = FastAPI(
    title="POS",
    version="1.0"
)
app.include_router(main_router)

app.mount("/", StaticFiles(directory="site/", html=True), name="site")
app.mount("/build", StaticFiles(directory="site/build"), name="build")

@app.get("/", tags=['Root'])
async def root():
    return RedirectResponse("/")