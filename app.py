import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

st.title("🧠 DeepSeek Code Companion")
st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    selected_model = st.selectbox(
        "Choose Model",
        ["deepseek-r1:1.5b", "deepseek-r1:3b"],
        index=0
    )

# Initiate the chat engine
llm_engine = ChatOllama(
    model=selected_model,
    base_url="http://localhost:11434",
    temperature=0.3
)

# System prompt configuration
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an expert AI coding assistant. Provide concise, correct solutions "
    "with strategic print statements for debugging. Always respond in English."
)

# Session state management
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat input and processing
user_query = st.chat_input("Type your coding question here...")

def generate_ai_response_stream(prompt_chain):
    """Streams AI response token by token"""
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.stream({})

def build_prompt_chain():
    prompt_sequence = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(prompt_sequence)

if user_query:
    # Save the new query in session_state so it shows immediately
    st.session_state.pending_query = user_query
    st.session_state.message_log.append({"role": "user", "content": user_query})
    st.rerun()

if "pending_query" in st.session_state:
    with st.chat_message("ai"):
        response_container = st.empty()  # Placeholder for streaming response
        full_response = ""

        with st.spinner("🧠 Processing..."):
            prompt_chain = build_prompt_chain()
            for chunk in generate_ai_response_stream(prompt_chain):
                full_response += chunk
                response_container.markdown(full_response)  # Update message live

        # Store final AI response
        st.session_state.message_log.append({"role": "ai", "content": full_response})
    
    # Clear the pending flag
    del st.session_state.pending_query
    st.rerun()
