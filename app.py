# import streamlit as st
# import pickle

# model = pickle.load(open("model.pkl", "rb"))

# st.title("Simple ML App")

# x = st.number_input("Enter value")

# if st.button("Predict"):
#     result = model.predict([[x]])
#     st.success(result[0])
# print("APP STARTING...")

# import streamlit as st

# st.title("Azure test app working 🚀")
# st.write("If you see this, Streamlit is running correctly")
import streamlit as st
import pickle
import os

st.title("Simple ML App")

# safe model loading
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))

x = st.number_input("Enter value")

if st.button("Predict"):
    result = model.predict([[x]])
    st.success(result[0])
