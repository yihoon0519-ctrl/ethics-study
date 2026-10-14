import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
st.set_page_config(page_title="통합사회2 윤리 암기 학습", page_icon="📚", layout="wide")
html = Path(__file__).with_name("통합사회2_윤리_암기학습.html").read_text(encoding="utf-8")
components.html(html, height=2200, scrolling=True)
