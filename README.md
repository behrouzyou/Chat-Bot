# 🤖 Chat-Bot — Terminal LLM Assistant

A lightweight, terminal-based chatbot that connects to an OpenAI-compatible API (`https://api.gapgpt.app/v1`) and uses the **GPT-4o** model. It keeps conversation context, tracks token usage, and enforces a concise-answer system prompt.

---

## 📌 Features

- 💬 **Interactive terminal chat** — simple `input()` loop, no UI dependencies
- 🧠 **Context-aware** — keeps the last few messages so the model remembers recent turns
- 💰 **Token tracking** — shows per-message and cumulative token usage
- ✂️ **Concise responses** — system prompt enforces short, bullet-point answers
- 🔐 **Secure API key** — loaded from a `.env` file, never hardcoded
- 🛑 **Graceful exit** — type `exit`, `end`, `quit`, or `خروج` to stop
- ⚠️ **Error recovery** — failed requests don't break the conversation loop

---

## 🗂️ Repository Structure
Chat-Bot/
├── main.py # Main chatbot script
├── .env # Local secrets (NOT committed)
├── .env.example # Template for required env vars
├── .gitignore
├── requirements.txt
└── README.md

text

---

## ⚙️ Requirements

- Python **3.9+**
- [`openai`](https://pypi.org/project/openai/) SDK (v1.x)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)

Install:

```bash
pip install openai python-dotenv
Or, if you add a requirements.txt:

bash
pip install -r requirements.txt
🔐 Environment Setup
Create a .env file in the project root:

env
HF_TOKEN=your_api_key_here
The variable is named HF_TOKEN in the code, but any valid API key for the gapgpt.app OpenAI-compatible endpoint will work. Rename it in both main.py and .env if you prefer OPENAI_API_KEY.

Never commit .env to Git. Make sure your .gitignore includes it.

🚀 Usage
Clone the repo

bash
git clone https://github.com/behrouzyou/Chat-Bot.git
cd Chat-Bot
Set up environment

bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt
cp .env.example .env            # then edit .env and add your key
Run the bot

bash
python main.py
Chat

text
you:
What is the capital of France?

Assistant:
Paris.

==========================================
current token use 42
total token usage: 42
===========================================
Type exit (or end, quit, خروج) to stop.

🧠 How It Works
Component	Details
API client	OpenAI(base_url='https://api.gapgpt.app/v1', api_key=...)
Model	gpt-4o
System prompt	Enforces concise, bullet-point answers; limits replies to 3–5 sentences
Context window	Last 6 messages kept (messages = messages[-6:])
Token counter	Accumulates response.usage.total_tokens across the session
Error handling	On API failure, prints error and pops the last user message to keep history clean
📝 Notes & Limitations
The context truncation (messages[-6:]) keeps only the 3 most recent user-assistant pairs — good for cost control, but long conversations lose older context.

The bot does not stream responses — you wait for the full reply before it prints.

Token usage is reported per-turn and cumulatively; useful for cost tracking.

The system prompt is intentionally strict. Edit it in main.py if you want longer or more detailed answers.

🛠️ Possible Improvements
□ Add streaming output (stream=True)
□ Support configurable model name via env var
□ Persist conversation history to disk
□ Add a --max-tokens CLI flag
□ Colored terminal output (rich / colorama)
□ Optional summary of context instead of hard truncation
📄 License
Released for educational and personal use. Modify freely.

🙏 Acknowledgements
OpenAI Python SDK

python-dotenv

gapgpt.app — OpenAI-compatible API provider

Author: behrouzyou
