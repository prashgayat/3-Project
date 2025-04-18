# 📚 Text Generator using FastAPI and OpenAI GPT-3.5

This project is a simple text story generator built with FastAPI and OpenAI's GPT-3.5 Turbo model.

---

## 🚀 Features

- User inputs a **title**.
- Application generates a **very short story** based on the title.
- Powered by **OpenAI GPT-3.5-Turbo**, optimized for fast and creative text generation.
- Clean web UI without any Swagger documentation.
- Fast, minimal, beginner-friendly!

---

## ⚡ Why GPT-3.5-Turbo?

- **Creativity**: Perfect for generating short imaginative stories.
- **Speed**: Fast response time.
- **Cost**: Lower cost compared to GPT-4, making it ideal for lightweight applications.
- **Availability**: Easy API integration via OpenAI.

---

## 🛠 Requirements

- Python 3.8 or higher
- OpenAI API Key

Install required packages using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Setup Instructions

1. **Clone the Repository**\
   (You already have it.)

2. **Create a ****`.env`**** file** inside the `text_generator/` folder:

   ```
   OPENAI_API_KEY=your-real-openai-key-here
   ```

3. **Run the application**:

```bash
uvicorn text_generator.app:app --host 0.0.0.0 --port 8000 --reload
```

4. **Access the application**:\
   Open your browser and visit:

```
http://localhost:8000/
```

✅ Enter a title and generate a beautiful short story!

---

## 📂 Project Structure

```
3-Project/
└── text_generator/
    ├── app.py
    ├── .env
    ├── README.md
    └── requirements.txt
```

---

## 👨‍💻 Developed by

- **Prashanth**

---

# ✨

