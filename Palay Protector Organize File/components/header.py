# components/header.py
import streamlit as st

def show_header():
    st.markdown("""
        <div class="header-container">
            <img src=""
                 width="100" style="margin-bottom: 10px;">
            <h3 style="color:#2e7d32; font-weight:700;">PALAY PROTECTOR</h3>
        </div>
    """, unsafe_allow_html=True)
