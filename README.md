# 🎓 Chat with YouTube – RAG-Based Learning Assistant

Chat with any **YouTube educational video** and get answers **strictly from that video’s content**.
This project uses **Retrieval-Augmented Generation (RAG)** to turn long lectures into an interactive Q&A experience.

Designed especially for **students, teachers, and self-learners** who want to save time while studying.

---

## 🚀 What This Project Does

1. User pastes a **YouTube video link**
2. The app:

   * Extracts the video transcript
   * Splits it into meaningful chunks
   * Converts text into embeddings
   * Stores them in a vector database
3. User asks questions
4. The system retrieves **relevant video context only**
5. The LLM generates an answer **based strictly on the video knowledge**

❌ No outside information
❌ No hallucinations
✅ Context-aware answers

---

## 🧠 Why RAG?

Large Language Models can hallucinate when answering freely.
This project uses **RAG (Retrieval-Augmented Generation)** to ensure:

* Answers are **grounded in source data**
* The model **cannot go beyond the video**
* Results are **transparent and trustworthy**

This is critical for **educational applications**.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – UI
* **LangChain**
* **FAISS** – Vector database
* **YouTube Transcript API**
* **OpenRouter API**
* **Free LLMs & Embeddings**
* **dotenv** – Environment management

---

## 📂 Project Structure

```
├── app.py                # Streamlit UI
├── rag_pipeline.py       # RAG logic (retrieval + generation)
├── embeddings.py         # OpenRouter embedding wrapper
├── llm_config.py         # LLM configuration
├── requirements.txt
├── .env                  # API keys (not committed)
└── README.md
```
---

## 💬 Usage

1. Paste a **YouTube educational video URL**
2. Click **Process Video**
3. Ask questions like:

   * *What is the main concept explained?*
   * *Explain this topic in simple words*
   * *What examples were discussed?*

Even if you **don’t say “according to the video”**, the system will always answer **only from the video content**.

---

## 🎯 Use Cases

* 📚 Exam revision
* 🎓 Lecture summarization
* 👩‍🏫 Teacher content review
* 🧠 Self-paced learning
* 🕒 Time-saving study assistant

---

## 🔒 Limitations

* Depends on availability of YouTube transcripts
* Best results with **educational / lecture-style videos**
* Not intended for entertainment videos

---

## 🌱 Future Improvements

* Multi-video knowledge base
* Timestamp-based answers
* PDF notes generation
* Chat history & memory
* Deployment on cloud

---

## 🤝 Contributions

Contributions, suggestions, and feedback are welcome.
Feel free to open an issue or submit a pull request.

---

## 👨‍💻 Author

**Ahmed Iqbal**
Software Engineer | Data Science & AI Enthusiast

📌 LinkedIn: *www.linkedin.com/in/ahmed-iqbal-393234301*

---

## ⭐ Final Note

This project was built to **solve a real learning problem** using modern AI practices.
If you find it useful, consider giving it a ⭐ — it helps a lot!

---


