from fastapi import FastAPI

from app.core.database.postgres.database import engine
from app.core.models.postgres import models
from app.features.joke.presentation.routes.joke_routes import joke_router
from app.features.page.presentation.routes.page_routes import page_router

app = FastAPI()
app.include_router(joke_router)
app.include_router(page_router)


@app.on_event('startup')
def startup_event():
    models.Base.metadata.create_all(bind=engine)


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
