# 🧠 Smart Personal Assistant (Jarvis-Style AI Assistant)
### Built with LangGraph, LLMs, Appium, ADB, Automation Tools & Voice Interface  
#### 👨‍💻 Made by: [Thasin Khan](https://www.linkedin.com/in/thasin-khan-055bb924a/)

---

## 🚀 Overview

This project is an advanced **AI-powered personal assistant** that understands your voice, selects the correct tool automatically, and performs actions on your smartphone or laptop.

You can talk naturally, like:

- “Open Instagram and post a story.”
- “Send a WhatsApp message to Aman saying *I'm coming*.”
- “Call Rahul from my contacts.”
- “What meetings do I have tomorrow?”

The assistant listens → understands → decides the tool → executes.

---

## ✨ Features

### 🎙️ Voice Interaction
- Converts your speech to text
- Supports Whisper / Google Speech-to-Text

---

### 🧠 LangGraph Multi-Tool Agent
The core intelligence:
- Automatically chooses the correct tool (call, message, calendar, contact search, app open, etc.)
- Implements autonomous reasoning
- Uses memory + context + tool routing

---

### 📱 Smartphone Automation (Appium + ADB)
You can control **any app** on your phone:

- Open apps (Instagram, WhatsApp, YouTube, etc.)
- Navigate screens
- Type messages
- Automate UI elements
- Trigger actions using Android UIAutomator

Example Voice Command:
> “Open WhatsApp and message Aman *I’m coming*.”

---

### 📅 Calendar Tool (Google Calendar API)
- Reads upcoming events
- Checks availability
- Answers questions like:
  - “Do I have a meeting tomorrow?”
  - “What’s scheduled next Monday?”

---

### 📞 Call & Contacts Tool
- Reads local contacts (with permission)
- Recognizes names
- Handles natural queries like:
  - “Call Sandeep”
  - “Does Aman have two numbers?”
  - “Message mom on WhatsApp”

---

### 🤖 App Control Tool
Control OS + apps using:
- Appium  
- ADB commands  
- UIAutomator2

Examples:
- Open Instagram  
- Post a story (with prompt to choose an image)
- Open camera
- Play music
- Turn on WiFi / Bluetooth / Flashlight

---

## 🧩 Tech Stack

| Component | Technologies Used |
|----------|--------------------|
| **LLM Engine** | OpenAI GPT, LangChain, LangGraph |
| **Voice Input** | Whisper / Google STT |
| **Phone Automation** | Appium, ADB, UIAutomator |
| **Backend** | Python, FastAPI / Flask |
| **Routing Logic** | LangGraph State Machine |
| **Calendar** | Google Calendar API |
| **Contacts** | Local phone contacts (via provider API) |
| **Deployment** | Local, Cloud, or Device-based |

---

## 🛠️ Installation

### 1️⃣ Install Dependencies
```bash
pip install langgraph langchain openai appium-python-client fastapi uvicorn google-api-python-client
npm install -g appium
appium

👨‍💻 Author

Thasin Khan
AI & Data Science Engineer
LinkedIn:
👉 https://www.linkedin.com/in/thasin-khan-055bb924a/