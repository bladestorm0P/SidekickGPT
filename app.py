import streamlit as st
import logic  # This is your brain code file

# 1. Setup the Page (ChatGPT Style)
st.set_page_config(page_title="SidekickGPT", layout="wide")

# 2. Sidebar for History (Like ChatGPT)
with st.sidebar:
    st.title("💥 SidekickGPT")
    st.markdown("---")
    st.button("➕ New Chat", on_click=lambda: st.session_state.messages.clear())
    st.write("Recent Conversations will appear here!")

# 3. Initialize Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. Display the Chat Bubbles
for message in st.session_state.messages:
    # Use 💥 for Sidekick and 👤 for you
    avatar = "💥" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 5. The Chat Input Box
if prompt := st.chat_input("Message SidekickGPT..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # 6. Generate Response from your logic.py
    try:
        # This sends the whole chat history to your code for 'Memory'
        ai_response = logic.your_function(prompt, st.session_state.messages)
    except:
        ai_response = "I'm having trouble thinking... check my logic code!"

    # 7. Show Sidekick's Answer
    with st.chat_message("assistant", avatar="💥"):
        st.markdown(ai_response)
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
