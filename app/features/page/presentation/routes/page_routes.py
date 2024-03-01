"""
    page router
    https://github.com/tiangolo/fastapi/issues/2916#issuecomment-818260637
"""
from app.features.page.presentation.routes.create_page_route import create_page
from app.features.page.presentation.routes.delete_page_route import delete_page
from app.features.page.presentation.routes.get_page_route import get_page
from app.features.page.presentation.routes.get_pages_route import get_pages
from app.features.page.presentation.routes.update_page_route import update_page, router

page_router = router