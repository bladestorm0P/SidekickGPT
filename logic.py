import requests
import json

def process_chat(chat_history):
    # This is the local address where your llama-server is listening
    URL = "http://127.0.0.1:8080/v1/chat/completions"
    
    # We prepare the data to send to SidekickGPT's brain
    payload = {
        "messages": chat_history,
        "temperature": 0.7,
        "stream": False
    }
    
    try:
        # Send the "Boss's" message to the local server
        response = requests.post(URL, json=payload, timeout=30)
        
        if response.status_code == 200:
            # Pick out just the text answer from the AI
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"💥 Boss, the engine is acting up! (Error: {response.status_code})"
            
    except requests.exceptions.ConnectionError:
        return "💥 Boss, I can't find the engine! Did you start the llama-server in the terminal?"

