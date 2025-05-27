import os
import socket

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class Item(BaseModel):
    text: str
    is_done: bool = False


@app.get("/")
async def root():
    return {"message": "Hello World"}


items = []


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items


@app.get("/items/{item_id}",response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

@app.get("/get_hash",response_class=HTMLResponse)
def read_root(request: Request):
    hostname = socket.gethostname()
    commit_hash = os.getenv("COMMIT_HASH","unknown")
    return templates.TemplateResponse(
        "index.html",{
            "request": request,
            "hostname": hostname,
            "commit_hash": commit_hash
        }
    )
