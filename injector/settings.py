from typing import List

from starlette.config import Config

config = Config(".env")

CORS_ORIGINS = config("STARLETTE_CORS_ORIGINS", cast=List[str], default=None)
