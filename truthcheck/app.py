import streamlit as st
from nlp.fake_news_model import detect_fake_news
from nlp.detectgpt import detect_ai_generated
from cv.deepfake_image import analyze_image
from cv.deepfake_video import analyze_video
from utils.scraper import extract_text_from_url

st.set_page_config(page_title="TruthCheck", page_icon="🧠", layout="centered")
st.markdown("""
<style>
.big-score { font-size: 2.5em; font-weight: bold; color: #222; }
.result-box { padding: 1em; border-radius: 10px; margin-bottom: 1em; background-color: #f0f2f6; color: #222; }
.result-score { font-weight: bold; color: #2a5cff; font-size: 1.1em; }
.result-explanation { color: #333; font-size: 1em; }
</style>
""", unsafe_allow_html=True)

st.title("🧠 TruthCheck: AI Fake News & Deepfake Detector")
st.caption("Detect fake news, AI-generated text, and deepfakes with instant explanations and scores.")

st.info("""
**How to interpret the results:**
- **Fake News Score:** Judges if the text is likely to be misinformation or not. 'Real' means it doesn't look like fake news, but it could still be AI-generated.
- **AI Probability:** Judges if the text was written by an AI, regardless of whether it's true or false.
""")

option = st.radio("What would you like to analyze?", ["Text or URL", "Image", "Video"], horizontal=True)

if option == "Text or URL":
    user_input = st.text_area("Paste news text or URL:", height=150)
    if st.button("Analyze", type="primary"):
        with st.spinner("Analyzing..."):
            if user_input.startswith("http"):
                text = extract_text_from_url(user_input)
            else:
                text = user_input
            label, score, explanation = detect_fake_news(text)
            ai_label, ai_score, ai_explanation = detect_ai_generated(text)

        # Show warning/info if results disagree
        if (label == "Real" and ai_score > 0.8) or (label == "Fake" and ai_score < 0.2):
            st.warning("""
**Note:**
- The Fake News detector and AI detector are separate. This text is likely AI-generated, but does not show signs of being fake news (or vice versa).
- Always use your own judgment and check multiple sources.
""")

        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f'<div class="result-box">'
                        f'<span class="big-score">🧾 {label}</span> '
                        f'<br><span class="result-score">Score: {score}%</span><br>'
                        f'<span class="result-explanation">Why? {explanation}</span>'
                        f'</div>', unsafe_allow_html=True)
        with col2:
            st.metric("AI Probability", f"{int(ai_score*100)}%", delta=None)
            st.progress(ai_score)
            st.caption(ai_explanation)

elif option == "Image":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file and st.button("Analyze", type="primary"):
        with st.spinner("Analyzing image..."):
            result = analyze_image(uploaded_file)
        st.success(result)

elif option == "Video":
    uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi"])
    if uploaded_video and st.button("Analyze", type="primary"):
        with st.spinner("Analyzing video..."):
            result = analyze_video(uploaded_video)
        st.success(result)
