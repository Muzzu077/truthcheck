# TruthCheck: AI-Based Fake News & Deepfake Detector

TruthCheck is an AI-powered web app to detect fake news, AI-generated text, and deepfake images/videos. Paste text or URLs, upload images or videos, and get instant results with probability scores and explanations.

## Features
- Paste text or URL: Detects fake/real/AI-generated news.
- Upload image/video: Detects deepfakes.
- Probability scores and explanations.

## How to Use
1. Choose analysis type (Text/URL, Image, Video).
2. Paste or upload your content.
3. Get instant results with explanations.

## Tech Stack
- Streamlit
- HuggingFace Transformers
- DeepFace
- OpenCV
- Newspaper3k

## Running Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment
Deploy easily on [Streamlit Cloud](https://streamlit.io/cloud) or your own server.

## License
MIT
