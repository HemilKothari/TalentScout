
# 🧠 TalentScout AI Hiring Assistant

An intelligent, locally running AI chatbot that streamlines initial candidate screening by collecting essential information and generating **tech-stack-specific interview questions**. Built using **Streamlit** and **Mistral-7B (Instruct)**.

---

## 🚀 Features

- 📝 Collects candidate info (name, experience, location, tech stack)
- 💡 Auto-generates relevant technical questions for each tech
- 📦 Local LLM (Mistral-7B) via `transformers`
- 🧠 Prompt engineering for coherent context-aware conversations
- ✅ Session-based, GDPR-compliant mock data handling
- 🛡 Optional data encryption and consent checkbox

---

## 📸 Demo

> 🔗 [Insert Loom or YouTube video link here]

---

## 🛠️ Tech Stack

| Component        | Tool/Library                      |
|------------------|-----------------------------------|
| UI Framework     | Streamlit                         |
| Language Model   | Mistral-7B (Instruct) via Hugging Face |
| Prompt Logic     | Custom Python prompts             |
| Storage          | Local file (`candidates.json`)    |
| Security         | Optional encryption via `cryptography` |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/talentscout-ai-chatbot.git
cd talentscout-ai-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Activate:
# Windows:
.env\Scriptsctivate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Model Setup

### 🔐 Option A: Use Mistral-7B via Hugging Face (GPU Recommended)

1. Create an account at [huggingface.co](https://huggingface.co)
2. Visit the model page: [Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
3. Click **"Request Access"**
4. Login via CLI:

```bash
huggingface-cli login
```

5. Run the app (model will auto-download if access is approved)

---

### 🧊 Option B: Use Offline CPU Model (GGUF)

Alternatively, use a `.gguf` quantized model via `llama-cpp-python` (ask for this version if needed)

---

## ▶️ Run the App

```bash
streamlit run app.py
```

App will open in your browser at [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
talentscout_ai_assistant/
│
├── app.py               # Streamlit app
├── chatbot.py           # Core chat + logic manager
├── local_llm.py         # Loads Mistral-7B model
├── prompt_engine.py     # Prompt generation logic
├── utils.py             # Consent, save, and exit detection
├── candidates.json      # Local demo data store
├── requirements.txt
└── README.md
```

---

## 🧠 Prompt Design Strategy

We use prompt chaining to guide Mistral to:

- Understand candidate experience
- Parse tech stack like “Python, Django, React”
- Generate 3–5 technical questions **per tech**
- Maintain professional tone and coherence

---

## 🔐 Privacy & Security

| Concern         | Our Solution                            |
|----------------|------------------------------------------|
| Data Storage    | Local only, no cloud storage             |
| Consent         | Optional checkbox in UI                  |
| Privacy Law     | GDPR-mock compliant (no real data used)  |
| Encryption      | Optional `cryptography`-based file save  |

---

## 🎥 Demo Walkthrough Script

> See `demo_script.md` for a 1-minute video explanation script

---

## ✨ Future Enhancements

- [ ] Sentiment analysis of answers
- [ ] Multilingual support
- [ ] Adaptive difficulty questions
- [ ] Admin dashboard with filtering

---

## 📜 License

MIT License — use freely for learning or prototyping.

---

## 🙋‍♂️ Author

**Hemil Kothari**  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/your-profile)
