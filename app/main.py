from typing import Optional

from fastapi import FastAPI
from .resources import ner

app = FastAPI()

app.include_router(ner.router)

@app.get("/")
def read_root():
    return {"Hello": "World!"}

