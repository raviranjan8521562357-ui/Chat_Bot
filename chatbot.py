from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

# Read API key from environment to avoid committing secrets
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("Missing GOOGLE_API_KEY environment variable. Add it to your .env file and restart.")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",  # or gemini-1.5-flash (faster, cheaper)
    google_api_key=api_key,
    temperature=0.7
)

# Streamlit UI setup
st.title("💬 Ravi's Chatbot")

# Initialize session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Get model response
    response = model.invoke(user_input)
    ai_reply = response.content

    # Add AI message
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.chat_message("assistant").write(ai_reply)
