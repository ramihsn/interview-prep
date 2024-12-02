from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi import docs as fastapi_docs
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from multiprocessing import Queue
from fastapi import FastAPI
import logging_loki
import logging
import dotenv

from app import api
from app.core import lifespan

dotenv.load_dotenv()
handler = logging_loki.LokiQueueHandler(
    Queue(-1),
    url="http://loki:3100/loki/api/v1/push",
    tags={"job": "backend", "host": "backend"},
    # auth=("username", "password"),
    version="1",
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Logs to a file
        logging.StreamHandler(),         # Logs to stdout
        handler,
    ],
)

app = FastAPI(lifespan=lifespan, docs_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)


# Route to serve the favicon
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")


# override the default swagger UI to include the favicon
@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return fastapi_docs.get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="[BE] Interview Prep API",
        swagger_favicon_url="/favicon.ico",
    )
