from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize FastAPI app
app = FastAPI()

# HTML Form Template
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Language Translator</title>
</head>
<body style="text-align:center; padding:50px;">
    <h1>🌍 Language Translator</h1>
    <form method="post" action="/translate/">
        <textarea name="text" rows="5" cols="50" placeholder="Enter text to translate" required></textarea><br><br>
        <input type="text" name="source_language" placeholder="Source language (e.g., French)" required><br><br>
        <input type="text" name="target_language" placeholder="Target language (e.g., English)" required><br><br>
        <input type="submit" value="Translate">
    </form>
</body>
</html>
"""

# Route to render the form
@app.get("/", response_class=HTMLResponse)
async def read_form():
    return html_form

# POST route to process the translation
@app.post("/translate/", response_class=HTMLResponse)
async def translate_text(
    request: Request,
    text: str = Form(...),
    source_language: str = Form(...),
    target_language: str = Form(...)
):
    try:
        prompt = (
            f"Translate the following text from {source_language} to {target_language}: \n\n{text}\n\n"
            "Only return the translated text, without any additional explanation."
        )
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional language translator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )
        
        translated_text = response.choices[0].message.content.strip()
        
        # Render the result
        result_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Translation Result</title>
        </head>
        <body style="text-align:center; padding:50px;">
            <h1>🌎 Translation Result</h1>
            <p><strong>Original Text:</strong> {text}</p>
            <p><strong>Source Language:</strong> {source_language}</p>
            <p><strong>Target Language:</strong> {target_language}</p>
            <h2>Translated Text:</h2>
            <p>{translated_text}</p>
            <br><br>
            <a href="/">🔙 Translate Another</a>
        </body>
        </html>
        """
        return HTMLResponse(content=result_html)
    
    except Exception as e:
        return HTMLResponse(content=f"<h1>❌ Translation Error:</h1><p>{str(e)}</p>")

