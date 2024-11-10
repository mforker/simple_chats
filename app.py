# from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(layout="wide")
# load_dotenv()

# api = os.getenv("GEMINI_API_KEY")
api = st.secrets['GEMINI_API_KEY']
genai.configure(api_key=api)


# func to load gemini model
model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

def get_response(query):
    res = chat.send_message(query, stream=True)
    return res

st.title("Gemini Powered Chatbot")

if 'message' not in st.session_state:
    st.session_state['message'] = []

for message in st.session_state['message']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if prompt:= st.chat_input("Text here"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state['message'].append({"role" : "You", "content" : prompt})

    response = get_response(prompt)

    with st.chat_message("Assistant"):
        for chunks in response:
            st.markdown(chunks.text)

    st.session_state['message'].append({"role" : "Bot", "content" : response.text})
