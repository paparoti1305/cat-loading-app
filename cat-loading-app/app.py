import streamlit as st
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="Loading Cat", page_icon="🐱", layout="centered")

def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_cat = load_lottie("cat.json")

st.markdown("<h2 style='text-align: center;'>🐾 Loading... Please wait 🐾</h2>", unsafe_allow_html=True)
st_lottie(lottie_cat, height=300, width=300, speed=1, loop=True, quality="high")
