import streamlit as st
import requests

st.set_page_config(page_title="Chattrix AI", page_icon="🧠", layout="centered")

# --- Styling ---
st.markdown("""
    <style>
    .stTextArea textarea {
        height: 100px !important;
        border-radius: 10px;
    }
    .user-bubble {
        background-color: #DCF8C6;
        color: black;
        padding: 10px;
        border-radius: 10px;
        max-width: 75%;
        float: right;
    }
    .bot-bubble {
        background-color: #F1F0F0;
        color: black;
        padding: 10px;
        border-radius: 10px;
        max-width: 75%;
        float: left;
    }
    .clear-float {
        clear: both;
    }
    .title {
        font-size: 28px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 20px;
    }
    .stButton > button {
        background-color: #006600;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px 24px;
        margin-top: 10px;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Headers ---
st.markdown('<div class="title">🧠 Chattrix</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything! Powered by Kimi-K2 Instruct.</div>', unsafe_allow_html=True)

# --- API Setup ---
API_URL = "https://api.together.xyz/v1/completions"
API_KEY = "Bearer 775d336aa3c87fcf60da8cc3ca3ef62d23a1a86b3c01f88e4b3a89a783b7093a"

def generate_text(user_prompt):
    wrapped_prompt = f"[INST] You are a helpful and polite AI assistant. {user_prompt} [/INST]"
    payload = {
        "model": "moonshotai/Kimi-K2-Instruct",
        "prompt": wrapped_prompt,
        "max_tokens": 200,
        "temperature": 0.7,
        "top_p": 0.9,
        "stop": None
    }
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['text'].strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- Session Setup ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Chat Display ---
chat_container = st.container()
with chat_container:
    for sender, msg in st.session_state.history:
        if sender == "user":
            st.markdown(f'<div class="user-bubble">{msg}</div><div class="clear-float"></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-bubble">{msg}</div><div class="clear-float"></div>', unsafe_allow_html=True)

# --- Divider ---
st.markdown("---")

# --- Input at Bottom ---
input_container = st.container()
with input_container:
    user_input = st.text_area("💬 Type your message:", placeholder="Start typing...", key="input", label_visibility="collapsed")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🚀 Ask", use_container_width=True):
            if user_input.strip() != "":
                with st.spinner("Thinking..."):
                    bot_response = generate_text(user_input)
                st.session_state.history.append(("user", user_input))
                st.session_state.history.append(("bot", bot_response))
                st.rerun()
            else:
                st.warning("⚠️ Please enter a prompt.")
