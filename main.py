from fastapi import FastAPI
from prometheus_client import start_http_server, Summary, generate_latest
from starlette.responses import Response
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}