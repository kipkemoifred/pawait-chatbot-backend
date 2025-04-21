from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

from google import genai

from dotenv import load_dotenv

import os

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ContentRequest(BaseModel):
    content: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/generate")
def generate_from_gemini(request: ContentRequest):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=request.content,
    )

    return {"response": response.text}
