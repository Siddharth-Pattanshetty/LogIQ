import streamlit as st
import requests

st.set_page_config(page_title="LogIQ", page_icon="🧠", layout="wide")

st.title("🧠 LogIQ - Log Analyzer")

API_URL = "http://127.0.0.1:8000/api/v1"

log = st.text_area("Enter log")

if st.button("Analyze"):
    if not log.strip():
        st.warning("Please enter a log message.")
    else:
        try:
            res = requests.post(
                f"{API_URL}/predict-log",
                json={"log": log}
            ).json()

            st.json(res)
        except requests.exceptions.ConnectionError:
            st.error("⚠️ Could not connect to the backend. Make sure the API is running.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")