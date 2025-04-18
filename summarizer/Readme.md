# Summarizer - FastAPI + OpenAI

This is a lightweight text summarization API built with **FastAPI** and **OpenAI GPT** models.  
It allows users to send a long text and receive a professionally summarized version.

---

## 📂 Project Structure

```
3-Project/
└── summarizer/
    ├── app.py
    ├── .env
    └── __pycache__/
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/3-Project.git
   cd 3-Project
   ```

2. **Create a virtual environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key**
   - Inside the `summarizer/` folder, create a `.env` file (already created).
   - Add your API key like this:
     ```
     OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     ```

5. **Run the FastAPI app**
   ```bash
   uvicorn summarizer.app:app --host 0.0.0.0 --port 8000 --reload
   ```

---

## 🚀 How to Use

- After running, open your browser at:
  ```
  http://localhost:8000/docs
  ```

- You can interact with the API using the Swagger UI.

- **Endpoint:**
  - `POST /summarize`
  - **Request Body:**
    ```json
    {
      "story": "Paste your long text here."
    }
    ```

- **Response:**
  ```json
  {
    "original_text": "Your full text",
    "summary": "Short professional summary"
  }
  ```

---

## 🛠️ Technologies Used

- FastAPI
- Uvicorn
- OpenAI GPT
- Python-Dotenv

---

## 📢 Notes

- Make sure your OpenAI API key has access to `gpt-3.5-turbo` or `gpt-4`.
- Keep `.env` secure and do not push it to GitHub.

---

## 📜 License

This project is licensed for academic and personal use.

---