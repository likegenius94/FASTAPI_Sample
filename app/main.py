from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to First CI/CD Pipeline for Python and Docker with Approval Testing via Email - 2"}

@app.get("/{name}")
def read_root(name):
    return {"Message":"Hello "  + name }