import streamlit as st
import requests

st.title("🧠 LogIQ - Log Analyzer")

log = st.text_area("Enter log")

if st.button("Analyze"):
    res = requests.post(
        "http://127.0.0.1:8000/predict-log",
        json={"log": log}
    ).json()

    st.json(res)