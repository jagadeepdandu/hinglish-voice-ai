# hinglish-voice-ai

# Hinglish Chatbot (LoRA-finetuned Phi Model)

A professional web-based chatbot UI powered by a LoRA-finetuned Phi model, supporting Hinglish conversations. The app features a modern, branded interface inspired by top AI chat platforms and is production-ready for deployment on Render.

## Features
- **Modern UI:** Clean, responsive, and professional chat interface (Anthropic/Claude-inspired)
- **Branding:** Customizable logo, name, and tagline
- **Clear Button:** Instantly clear conversation history
- **REST API:** `/generate` endpoint for model inference
- **LoRA Adapter:** Efficient model adaptation using PEFT
- **Production Ready:** Deployable on Render with Gunicorn

## Project Structure
```
phi model/
├── app.py                # Flask backend with model loading and API
├── requirements.txt      # Python dependencies (incl. gunicorn)
├── Procfile              # Render process file
├── render.yaml           # (Optional) Render infrastructure-as-code
├── templates/
│   └── index.html        # Main chat UI
└── phi1_5_hinglish_lora/ # Your LoRA adapter directory
```

## Getting Started
1. **Clone the repo and install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run locally:**
   ```bash
   gunicorn app:app
   ```
   Or for development:
   ```bash
   python app.py
   ```
3. **Deploy on Render:**
   - Push your code to GitHub
   - Connect the repo to Render and create a new Web Service
   - Render will use the `Procfile` and `requirements.txt` automatically

## Model & Adapter
- The app loads the base Phi model and applies your LoRA adapter for Hinglish chat.
- Make sure your LoRA adapter files are present in the repo or accessible to Render.

## API Usage
- **POST** `/generate`
  - Request JSON: `{ "prompt": "User: <your message>\nAssistant:" }`
  - Response JSON: `{ "response": "<assistant reply>" }`

## Credits
- Built using [Flask](https://flask.palletsprojects.com/), [transformers](https://huggingface.co/docs/transformers/index), [PEFT](https://github.com/huggingface/peft), and [Gunicorn](https://gunicorn.org/).

---

### What Was Done
- Switched from Gradio to Flask for a more customizable/professional UI
- Built a modern, branded chat interface (with clear button, logo, tagline)
- Integrated LoRA-finetuned Phi model for Hinglish chat
- Added REST API endpoint for chat generation
- Prepared the codebase for production deployment on Render (Procfile, gunicorn, render.yaml)
- Added realistic, human-style code comments and organization

---
Feel free to customize the UI, branding, or add new features!
