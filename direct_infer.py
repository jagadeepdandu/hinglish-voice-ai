print("[DEBUG] Starting direct_infer.py")
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "microsoft/phi-1_5"
lora_model_path = "./phi1_5_hinglish_lora"
try:
    print("[DEBUG] Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("[DEBUG] Tokenizer loaded.")
    print("[DEBUG] Loading model...")
    model = AutoModelForCausalLM.from_pretrained(lora_model_path)
    print("[DEBUG] Model loaded.")
    prompt = "User: Namaste, aap kaise ho?\nAssistant:"
    print("[DEBUG] Running inference...")
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("[DEBUG] Inference complete.")
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
except Exception as e:
    print(f"[ERROR] {e}")
    import traceback; traceback.print_exc()
    exit(1)
