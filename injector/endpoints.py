import os

from starlette.requests import Request
from starlette.responses import Response
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="dist")
templates.env.variable_start_string = "[["
templates.env.variable_end_string = "]]"

vue_env_vars = {k: v for k, v in os.environ.items() if k.startswith("VUE_APP_")}


async def index_html(request: Request) -> Response:
    # use Jinja2 to inject any environment variable starting with 'VUE_APP_' into the template.
    print(os.environ)
    context = {"request": request, **vue_env_vars}
    return templates.TemplateResponse("index.html", context)
