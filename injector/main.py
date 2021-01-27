from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from .endpoints import index_html
from . import settings

app = Starlette(
    routes=[
        Route("/", index_html, name="index"),
        Mount(
            "/",
            StaticFiles(directory="dist", html=True),
            name="static_files",
        ),
    ],
)

# middleware
app.add_middleware(ProxyHeadersMiddleware)
if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.CORS_ORIGINS],
    )
