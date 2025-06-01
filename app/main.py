
import socket
import subprocess

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")



def get_git_commit_hash() -> str:
    try:
        commit_hash = subprocess.check_output(
            ['git', 'rev-parse', '--short','HEAD']
        ).decode('utf-8').strip()
        return commit_hash
    except Exception as e:
        return "unknown"

def get_hostname():
    try:
        with open("/host_hostname","r") as f:
            return f.read().strip()
    except Exception as e:
        return socket.gethostname()

@app.get("/",response_class=HTMLResponse)
def read_root(request: Request):
    hostname = get_hostname()
    commit_hash = get_git_commit_hash()
    return templates.TemplateResponse(
        "index.html",{
            "request": request,
            "hostname": hostname,
            "commit_hash": commit_hash
        }
    )
