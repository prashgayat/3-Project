from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)  # ✅ Disable Swagger docs

# Initialize OpenAI client
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# ✅ Serve Home Page with a form
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Story Generator</title>
        </head>
        <body style="text-align:center; font-family: Arial, sans-serif; margin-top:50px;">
            <h1>Story Generator</h1>
            <form method="post" action="/story">
                <input type="text" name="title" placeholder="Enter a title" style="width:300px; padding:10px;" required>
                <br><br>
                <input type="submit" value="Generate Story" style="padding:10px 20px;">
            </form>
        </body>
    </html>
    """

# ✅ Handle Story Generation and show the result
@app.post("/story", response_class=HTMLResponse)
async def generate_story(title: str = Form(...)):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative story writer."},
            {"role": "user", "content": f"Write a very short story about a {title}."}
        ],
        temperature=0.7,
        max_tokens=300
    )
    story = response.choices[0].message.content.strip()

    return f"""
    <html>
        <head>
            <title>Story Generated</title>
        </head>
        <body style="text-align:center; font-family: Arial, sans-serif; margin-top:50px;">
            <h1>Story for: "{title}"</h1>
            <p style="width:60%; margin:auto; text-align:justify;">{story}</p>
            <br><br>
            <a href="/" style="text-decoration:none; color:blue;">Generate Another Story</a>
        </body>
    </html>
    """
