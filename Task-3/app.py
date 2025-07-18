import streamlit as st
import os
import sys
sys.path.append(os.path.abspath('../Task-2'))
from chatbot.chatbot import generate_rag_response

st.set_page_config(page_title="Chat", page_icon="💬")
st.title("Wellness Assistant")

user_input = st.text_input("Ask something or say how you're feeling:")
if user_input:
    response = generate_rag_response(user_input)
    st.markdown("### Response")
    st.write(response)
