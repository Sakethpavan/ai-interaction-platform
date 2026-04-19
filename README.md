# ⚡ AI Interaction Platform (Phase 0)

An energy-efficient, modular AI platform designed to go beyond traditional voice assistants by enabling **context-aware conversations and real-world actions**.

---

## 🚀 Vision

This project aims to build a **privacy-first, energy-efficient AI system** that:

* Understands natural language (not intent-based)
* Executes actions (tools)
* Maintains conversational context
* Runs locally with optional GPU acceleration

> Unlike Alexa/Google Assistant, this system is designed as a **platform**, not just a voice interface.

---

## 🧠 Features (Phase 0)

* 💬 Chat-based interaction (API-driven)
* 🧠 LLM integration (via Ollama)
* 🗂️ Conversation memory (session-based)
* 🛠️ Tool execution (open apps, search, etc.)
* ⚡ Lightweight & modular architecture

---

## 🧱 Architecture

```
User → FastAPI → AI Core → LLM (Ollama)
                         ↓
                    Tool Engine
                         ↓
                      Response
```

---

## 🛠️ Tech Stack

* Backend: FastAPI
* AI Layer: Python
* LLM: Ollama
* Model: llama3
* Memory: In-memory (Phase 0)

---

## 📂 Project Structure

```
ai-platform/
├── app/
│   ├── main.py        # API entry point
│   ├── llm.py         # LLM integration
│   ├── memory.py      # session memory
│   ├── tools.py       # action execution
│   └── schemas.py     # request/response models
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run

### 1. Install Ollama

Install and start:

* Ollama

Pull model:

```
ollama run llama3
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run server

```
uvicorn app.main:app --reload
```

---

### 4. Test API

```
POST /chat
```

Example:

```json
{
  "userId": "1",
  "message": "open chrome",
  "session_id": "abc"
}
```

---

## 🔄 Flow

1. User sends message
2. System fetches conversation history
3. Prompt is built with context
4. LLM decides:

   * Normal response OR
   * Tool execution
5. Response returned & stored

---

## 🛠️ Example Tools

* `open_app(app_name)`
* `search_google(query)`

---

## ⚠️ Limitations (Phase 0)

* Memory is not persistent
* Tool calling depends on LLM reliability
* No authentication
* No streaming responses
* No voice interface yet

---

## 🗺️ Roadmap

### Phase 1

* Persistent memory (PostgreSQL)
* Structured tool calling
* Better routing (CPU vs GPU)

### Phase 2

* Voice interface (Whisper + TTS)

### Phase 3

* Edge device (ESP32)

### Phase 4

* Energy optimization (GPU on-demand)

---

## 💡 Key Design Principles

* ⚡ Energy-efficient AI (GPU only when needed)
* 🔌 Modular architecture (plug-and-play services)
* 🧠 Context-first (not intent-based)
* 🔒 Privacy-focused (local-first design)

---

## 📌 Why This Project?

Most assistants:

* Are intent-based ❌
* Depend on cloud ❌
* Lack extensibility ❌

This project:

* Enables real AI reasoning ✅
* Supports local execution ✅
* Acts as a platform for automation ✅

---

## 👨‍💻 Author

Saketh Pavan Goti  

This project is being developed as a foundation for a **scalable AI interaction platform**, exploring:
- hybrid AI architectures (edge + local GPU)
- real-time conversational systems
- action-driven AI (beyond chat)

The long-term goal is to evolve this into a **production-grade AI system for interaction and automation**.

---

## 🤝 Acknowledgements

AI-assisted development was used throughout this project for system design, problem-solving, and iterative refinement of components.
