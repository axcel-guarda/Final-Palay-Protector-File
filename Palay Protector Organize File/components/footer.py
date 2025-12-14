# components/footer.py
import streamlit as st

def show_footer():
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: #2e7d32;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        z-index: 1000;
    }
    </style>
    
    <div class="footer">
        © 2024 Palay Protector - Rice Disease Detection System
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:40px;'></div>", unsafe_allow_html=True)  # Spacer to avoid content overlap