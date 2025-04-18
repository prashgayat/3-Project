# Translator App - FastAPI + OpenAI GPT-3.5 Turbo

This project is a **language translator** built using **FastAPI** and **OpenAI GPT-3.5 Turbo** model.

It allows you to **translate text** from one language to another easily using a web form — no need to manually interact with JSON or APIs.

## ✨ Features

- Built with **FastAPI** (high-speed, minimal web framework)
- Powered by **OpenAI GPT-3.5 Turbo** for accurate and fast translations
- Clean, user-friendly HTML web page
- No `/docs` page interaction needed
- API key securely loaded from `.env` file
- Quick and easy deployment

## 🛠 Installation

1. Clone the repository:
   ```
   git clone https://github.com/prashgayat/3-Project.git
   ```
2. Navigate into the translator folder:
   ```
   cd 3-Project/translator
   ```
3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
4. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Create a `.env` file inside the `translator/` folder with your OpenAI key:
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## 🚀 Running the App

Start the FastAPI server:

```
uvicorn translator.app:app --host 0.0.0.0 --port 8000 --reload
```

Open your browser and visit:

```
http://localhost:8000/translate
```

(or use your forwarded Codespace URL)

## 📚 How It Works

- Input the **text**, **source language**, and **target language**.
- The app will send the request to OpenAI and return a **translated** version.
- Displays a neat webpage showing original and translated text.

## 🤖 Model Selection Rationale

We replaced the original Gemini model with **OpenAI GPT-3.5 Turbo** because:

- It’s **faster** and **cheaper** compared to GPT-4.
- Very good **multilingual** understanding.
- **Lower cost per token** for a translation-focused app.
- Well supported in production environments.

## 📂 Project Structure

```
translator/
├── app.py
├── requirements.txt
├── .env (gitignored)
└── README.md
```

## 📋 Example Usage

Input:

- Text: Hier soir, un incendie s'est déclaré dans un immeuble du centre-ville de Lyon.
- Source: French
- Target: English

Output:

- Last night, a fire broke out in a building in downtown Lyon. Firefighters quickly intervened and managed to control the fire in less than an hour.

## 🔒 Important

- `.env` file is **ignored** by Git (`.gitignore`).
- Make sure you have enough **API quota** for OpenAI.

## 👨‍💻 Developed by

- **Prashanth**

---

# ✨

