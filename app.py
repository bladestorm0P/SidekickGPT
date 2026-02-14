import streamlit as st
import logic  # This connects to your code

st.set_page_config(page_title="SidekickGPT", layout="wide")

# --- 1. THE BRAIN'S RULES ---
# We create a "System" message that stays in memory
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are SidekickGPT. You must ALWAYS call the user 'Boss'. You are loyal and helpful."}
    ]

# --- 2. SIDEBAR (ChatGPT Style) ---
with st.sidebar:
    st.title("💥 SidekickGPT")
    if st.button("➕ New Chat"):
        st.session_state.messages = [
            {"role": "system", "content": "You are SidekickGPT. You must ALWAYS call the user 'Boss'."}
        ]
        st.rerun()

# --- 3. SHOW THE CHAT ---
for message in st.session_state.messages:
    if message["role"] != "system": # Hide the secret rules from the screen
        avatar = "💥" if message["role"] == "assistant" else "👤"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# --- 4. THE INPUT ---
if prompt := st.chat_input("Ready for orders, Boss?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # We send the WHOLE memory to your logic so it remembers the "Boss" rule
    response = logic.process_chat(st.session_state.messages)

    with st.chat_message("assistant", avatar="💥"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

