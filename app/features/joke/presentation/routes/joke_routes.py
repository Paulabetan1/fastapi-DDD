"""
    joke router
    https://github.com/tiangolo/fastapi/issues/2916#issuecomment-818260637
"""
from app.features.joke.presentation.routes.delete_joke_route import delete_joke
from app.features.joke.presentation.routes.update_joke_route import update_joke
from app.features.joke.presentation.routes.create_joke_route import create_joke
from app.features.joke.presentation.routes.get_joke_route import get_joke
from app.features.joke.presentation.routes.get_jokes_route import get_jokes, router

joke_router = router
