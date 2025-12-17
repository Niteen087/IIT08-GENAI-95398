import streamlit as st
import dotenv
import requests
import json
import tornado.web
import os
dotenv.load_dotenv()

if 'messages' not in st.session_state:
    st.session_state.messages = []

api_key = os.getenv("groq-key")
url = "https://api.groq.com/openai/v1/chat/completions" 
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

st.title("Chat & Ask")
user_input = st.chat_input("Ask: ")
st.session_state.messages.append(user_input)
if user_input:
    req_data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            { "role": "user", "content": user_input },
        ],
    }
    response = requests.post(url, data=json.dumps(req_data), headers=headers)
    resp = response.json()
    
    st.session_state.messages.append(resp['choices'][0]['message']['content'])
    for idx, message in enumerate(st.session_state.messages):
        if message:
            role = "user" if idx % 2 == 0 else "assistant"
            with st.chat_message(role):
                st.write(message)
    