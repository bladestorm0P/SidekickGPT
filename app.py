import streamlit as st

# This gives your app a name at the top
st.set_page_config(page_title="SidekickGPT")
st.title("🦸‍♂️ SidekickGPT")
st.caption("Your loyal AI hero-in-training")

# 1. This part remembers what you said (The Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. This shows your old chat bubbles
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. This is the text box where you type
if prompt := st.chat_input("How can I help, Boss?"):
    # Add your message to the screen
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- YOUR AI LOGIC GOES HERE ---
    # For now, SidekickGPT will just repeat what you say.
    # We can add a "Real Brain" here later!
    response = f"SidekickGPT is ready! You said: {prompt}"
    # -------------------------------

    # Show the AI's answer
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
  
