# app.py

import streamlit as st

# Your language model code or chatbot code
from agent import generate_response

def main():
    st.title("Language Model Chatbot")

    user_input = st.text_input("Enter your text:")
    
    if st.button("Submit"):
        response = generate_response(user_input)
        st.text("Bot: " + response)

if __name__ == "__main__":
    main()
