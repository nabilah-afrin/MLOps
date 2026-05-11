from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "FastAPI Lab 1"))

@app.get('/')
def home():
    return {
        "message": "Welcome to FastAPI"
    }

@app.get('/ping')
def ping():
    return {
        "status": "ok",
        "message": "pong"
    }

@app.get('/hello/{name}')
def hello(name: str, greeting: str = 'Hello'):
    return {
        'message': f"{greeting}, {name}!"
    }