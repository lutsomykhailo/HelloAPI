from fastapi import FastAPI
import os
from app.config import settings
app = FastAPI()

@app.get("/")
def main():
    return {"message": f" HelloAPI -- version: {settings.api_version}", "api_key": os.environ.get("API_KEY","")}
