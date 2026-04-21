import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Simple ML App")

x = st.number_input("Enter value")

if st.button("Predict"):
    result = model.predict([[x]])
    st.success(result[0])