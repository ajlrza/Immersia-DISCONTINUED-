import uvicorn
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import html

app = FastAPI()

def run_engine(action: str) -> dict:
    