import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
from flask import Flask, request, jsonify, render_template

# --- Model setup ---
# These variables point to the base model and the directory containing your LoRA adapter.
MODEL_NAME = "microsoft/phi-1_5"
LORA_DIR = "./phi1_5_hinglish_lora/phi1_5_hinglish_lora"

# Attempt to load the tokenizer, base model, and LoRA adapter.
# If anything fails, print a traceback and exit.
try:
    print("[INFO] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    print("[INFO] Tokenizer loaded.")

    print("[INFO] Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    print("[INFO] Base model loaded.")

    print("[INFO] Applying LoRA adapter...")
    model = PeftModel.from_pretrained(base_model, LORA_DIR)
    print("[INFO] LoRA adapter successfully loaded and merged.")
except Exception as e:
    print("[ERROR] Failed to initialize model or tokenizer:", e)
    import traceback; traceback.print_exc()
    exit(1)

# --- Flask app setup ---
app = Flask(__name__)

@app.route('/')
def index():
    # Serve the main chat UI
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    # This endpoint receives a prompt and returns the model's response as JSON.
    data = request.get_json()
    prompt = data.get('prompt', '')
    if not prompt:
        # If the prompt is missing, return a 400 error.
        return jsonify({'error': 'No prompt provided.'}), 400
    try:
        # Tokenize the prompt and generate a response using the model.
        inputs = tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(**inputs, max_length=100, temperature=0.7)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract only the assistant's part of the response, if present.
        response = response.split('Assistant:')[-1].strip()
        return jsonify({'response': response})
    except Exception as e:
        # If something goes wrong, return a 500 error with the exception message.
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    # Start the Flask app in debug mode for development.
    app.run(host="0.0.0.0", port=5000, debug=True)
