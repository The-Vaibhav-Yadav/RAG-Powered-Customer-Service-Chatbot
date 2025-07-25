import streamlit as st
import requests

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("Customer Service Chatbot")

# Input for user query
query = st.text_input("Ask a question:", key="query_input")
col1, col2 = st.columns([1, 1]) 
with col1:
    if st.button("Submit"):
        if query:
            # Send query to FastAPI backend
            response = requests.post("http://localhost:8000/chat", json={"text": query})
            if response.status_code == 200:
                # Add query and response to chat history
                st.session_state.chat_history.append({"user": query, "bot": response.json()["response"]})
            else:
                st.error("Error processing query")
        else:
            st.warning("Please enter a question")
with col2:
    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Display chat history with styled text boxes
for i, chat in enumerate(st.session_state.chat_history):
    # User input box
    st.markdown(
        f"""
        <div style='background-color: #2E3033; padding: 10px; border-radius: 5px; margin: 5px 0;'>
            <strong>User:</strong> {chat["user"]}
        </div>
        """,
        unsafe_allow_html=True
    )
    # Bot response box
    st.markdown(
        f"""
        <div style='background-color: #171819; padding: 10px; border-radius: 5px; margin: 5px 0;'>
            <strong>Bot:</strong> {chat["bot"]}
        </div>
        """,
        unsafe_allow_html=True
    )

# Download chat history as text file
if st.session_state.chat_history:
    chat_text = "\n".join([f"User: {chat['user']}\nBot: {chat['bot']}" for chat in st.session_state.chat_history])
    st.download_button(
        label="💾 Download Chat",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain"
    )