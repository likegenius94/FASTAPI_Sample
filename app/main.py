from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello World Docker!"}

@app.get("/{name}")
def read_root(name):
    return {"Message":"Hello "  + name }