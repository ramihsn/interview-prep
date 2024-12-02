from fastapi.middleware.cors import CORSMiddleware
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

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)
