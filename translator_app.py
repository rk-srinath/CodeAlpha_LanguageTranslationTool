import streamlit as st
from deep_translator import GoogleTranslator

# Page config
st.set_page_config(page_title="AI Language Translator", page_icon="🌐", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main-title {
            font-size: 2.8rem;
            font-weight: 700;
            color: #1f3b4d;
            text-align: center;
            margin-top: 20px;
        }
        .sub-title {
            text-align: center;
            font-size: 1.1rem;
            color: #5a5a5a;
            margin-bottom: 30px;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #0099f7;
            color: white;
            border-radius: 5px;
            padding: 0.5em 1em;
        }
        .stButton>button:hover {
            background-color: #007acc;
        }
        footer {
            text-align: center;
            font-size: 12px;
            color: #999;
            margin-top: 3rem;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌐 AI Language Translator</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Translate text instantly between languages using AI. Powered by Deep Translator.</div>", unsafe_allow_html=True)
st.markdown("---")

# Language list
language_dict = {
    'English': 'english',
    'French': 'french',
    'German': 'german',
    'Hindi': 'hindi',
    'Tamil': 'tamil',
    'Spanish': 'spanish',
    'Chinese (Simplified)': 'chinese (simplified)',
    'Chinese (Traditional)': 'chinese (traditional)',
    'Japanese': 'japanese',
    'Russian': 'russian',
    'Arabic': 'arabic',
    'Urdu': 'urdu',
    'Korean': 'korean',
    'Italian': 'italian',
    'Portuguese': 'portuguese',
    'Turkish': 'turkish',
    'Vietnamese': 'vietnamese'
}

with st.form("translator_form"):
    text_input = st.text_area("✏️ Enter text to translate", height=150)

    col1, col2 = st.columns(2)
    with col1:
        source_lang = st.selectbox("🔤 Translate from", list(language_dict.keys()), index=0)
    with col2:
        target_lang = st.selectbox("🌍 Translate to", list(language_dict.keys()), index=1)

    submitted = st.form_submit_button("🚀 Translate Now")

if submitted:
    if not text_input.strip():
        st.warning("⚠️ Please enter some text.")
    elif source_lang == target_lang:
        st.info("ℹ️ Source and target languages are the same.")
    else:
        try:
            translated = GoogleTranslator(
                source=language_dict[source_lang],
                target=language_dict[target_lang]
            ).translate(text_input)
            st.success("✅ Translation Output")
            st.text_area("📄 Translated Text", value=translated, height=150)
        except Exception as e:
            st.error(f"❌ Translation Error: {str(e)}")

st.markdown("""
    <footer>
        Made with ❤️ by Srinath | Internship Project @ CodeAlpha<br>
        Built using Streamlit + Deep Translator
    </footer>
""", unsafe_allow_html=True)
