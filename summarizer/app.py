from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

import os

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configure OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Define request body model
class SummarizeRequest(BaseModel):
    story: str

# Define POST endpoint
@app.post("/summarize")
async def summarize_text(request: SummarizeRequest):
    try:
        prompt = f"Please professionally summarize the following text:\n\n{request.story}"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a professional text summarizer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )

        summary = response.choices[0].message.content.strip()

        return {
            "original_text": request.story,
            "summary": summary
        }
    except Exception as e:
        return {"error": str(e)}

from fastapi.responses import RedirectResponse

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
