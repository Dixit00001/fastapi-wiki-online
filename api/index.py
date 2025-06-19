#index.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
from starlette.responses import Response
from starlette.routing import Mount
from mangum import Mangum  # needed for AWS-style handlers

app = FastAPI()

@app.get("/api/outline")
def get_outline(country: str):
    return {"message": f"Outline for {country}"}

handler = Mangum(app)

