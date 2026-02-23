import streamlit as st

st.title("Welcome to Basic Streamlit App")


age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Delhi", "Mumbai", "Nashik", "Pune"])


if st.button("Show Details"):
    st.write("Age:", age)
    st.write("City:", city)