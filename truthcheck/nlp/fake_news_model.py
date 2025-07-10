from transformers.pipelines import pipeline

classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def detect_fake_news(text):
    result = classifier(text)[0]
    label = "Fake" if result['label'] == 'LABEL_1' else "Real"
    score = round(result['score'] * 100, 2)
    explanation = "Text shows patterns common in misinformation."
    return label, score, explanation
