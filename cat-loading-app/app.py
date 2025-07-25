import streamlit as st
from streamlit_lottie import st_lottie
import json
import time

st.set_page_config(page_title="Loading Cat", page_icon="🐱", layout="centered")

# Load Lottie animation JSON
def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_cat = load_lottie("cat.json")

# Căn lệch nhẹ mèo sang phải bằng cách dùng columns
left, center, right = st.columns([1, 2, 1])  # Chỉnh tỉ lệ lệch phải tại đây
with right:
    st_lottie(lottie_cat, height=300, width=300, speed=1, loop=True, quality="high")

# Loading động phía dưới
loading_text = st.empty()
dots = ["", ".", "..", "..."]
for i in range(20):  # khoảng 5 giây
    loading_text.markdown(f"<h2 style='text-align:center;'>🐾 Loading{dots[i % 4]} </h2>", unsafe_allow_html=True)
    time.sleep(0.25)
