def generate_explanation(label, score, context=None):
    if label == "Fake":
        return "This content shows patterns common in misinformation, such as sensational language or unreliable sources."
    elif label == "Real":
        return "This content does not show strong signs of misinformation."
    elif label == "AI-Generated":
        return "The text has characteristics typical of AI-generated content."
    else:
        return "No specific explanation available."
