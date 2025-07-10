from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the OpenAI GPT-2 Output Detector model from HuggingFace
# This is a simple, open-source detector for demonstration purposes
MODEL_NAME = "roberta-base-openai-detector"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def detect_ai_generated(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.softmax(logits, dim=1).cpu().numpy()[0]
        ai_score = float(probs[1])  # 1 = AI-generated, 0 = human
    label = "AI-Generated" if ai_score > 0.5 else "Likely Human"
    explanation = f"This text is {ai_score*100:.1f}% likely to be AI-generated."
    return label, ai_score, explanation
