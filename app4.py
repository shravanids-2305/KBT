import streamlit as st
import time

st.title("Simple Chatbot")

question = st.text_input("Ask me anything")

if st.button("Send"):
    st.write("You asked:", question)
    st.write("Chatbot is on process... reply soon ⏳")
    
    
    