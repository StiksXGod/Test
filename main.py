from fastapi import FastAPI
from prometheus_client import start_http_server, Summary, generate_latest
from starlette.responses import Response

app = FastAPI()

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}