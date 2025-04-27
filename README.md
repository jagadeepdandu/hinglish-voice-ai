# hinglish-voice-ai

Welcome to the Hinglish Voice AI project! 👋

This project is all about building a friendly, modern chatbot that understands and replies in Hinglish (a mix of Hindi and English). It's powered by a LoRA-finetuned Phi model and comes with a clean, professional web interface. Whether you want to chat, test, or deploy your own Hinglish assistant, you're in the right place!

## What is this?
- A web-based chatbot with a natural, conversational UI (inspired by top platforms like Claude/Anthropic)
- Uses a powerful language model (Phi) with LoRA fine-tuning for Hinglish
- Easy to run locally or deploy to the cloud (Render)

## Features
- **Clear conversation** button to reset the chat
- **REST API** endpoint for programmatic access (`/generate`)
- **Production-ready**: Gunicorn, Procfile, and render.yaml included

## How to get started
1. **Clone this repo and install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run locally:**
   ```bash
   gunicorn app:app
   # or, for development:
   python app.py
   ```

## Project layout
```
phi model/
├── app.py                # Flask backend with model loading and API
├── requirements.txt      # Python dependencies (incl. gunicorn)
├── hinglish_data.json    # Example Hinglish chat dataset
├── Procfile              # For Render deployment
├── render.yaml           # Render config
├── templates/
│   └── index.html        # The main chat UI
└── phi1_5_hinglish_lora/ # Your LoRA adapter directory
```

## API usage
- **POST** `/generate`
  - Request: `{ "prompt": "User: <your message>\nAssistant:" }`
  - Response: `{ "response": "<assistant reply>" }`


---
Feel free to customize, fork, or contribute!
