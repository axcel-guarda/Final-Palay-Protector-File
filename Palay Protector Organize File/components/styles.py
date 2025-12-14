import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>

    /* GLOBAL BACKGROUND */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(
            135deg,
            #cfe8d6 0%,
            #dff2e5 50%,
            #c8e1d0 100%
        ) !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* REMOVE HEADER FOR ALL PAGES */
    header, [data-testid="stHeader"] {
        display: none !important;
    }

    /* REMOVE TOP SPACING */
    .block-container, .main {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }

    /* LOGIN ONLY */
    #login-container {
        background: rgba(255, 255, 255, 0.92);
        backdrop-filter: blur(6px);
        border-radius: 18px;
        padding: 25px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
    }

    /* INPUTS */
    .stTextInput input {
        background: #f3faf4 !important;
        border: 1px solid #c7dec9 !important;
        border-radius: 10px !important;
    }

    /* BUTTONS */
    .stButton button {
        background-color: #2e7d32 !important;
        color: white !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 10px 0 !important;
        transition: 0.2s ease;
    }
    .stButton button:hover {
        background-color: #256528 !important;
        transform: translateY(-2px);
    }

    </style>
    """, unsafe_allow_html=True)



def show_splash_screen():
    splash_html = """
    <style>
    .splash-container {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: linear-gradient(135deg, #1b5e20, #66bb6a);
        display: flex; align-items: center; justify-content: center;
        flex-direction: column;
        z-index: 9999;
        animation: fadeOut 4s forwards;
    }
    .splash-logo {
        width: 120px;
        animation: float 2s infinite;
    }
    .splash-title {
        color: white; font-size: 32px; font-weight: 800;
        margin-top: 20px; letter-spacing: 2px;
        opacity: 0; animation: fadeIn 2s forwards 0.8s;
    }
    .loader {
        margin-top: 30px;
        width: 50px; height: 50px;
        border: 5px solid rgba(255,255,255,0.3);
        border-top: 5px solid #fff;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }

    @keyframes spin { to { transform: rotate(360deg); } }
    @keyframes float { 50% { transform: translateY(-10px); } }
    @keyframes fadeIn { to { opacity: 1; } }
    @keyframes fadeOut { 100% { opacity: 0; visibility: hidden; } }
    </style>

    <div class="splash-container">
        <img src="https://cdn-icons-png.flaticon.com/128/2095/2095652.png" class="splash-logo">
        <div class="splash-title">PALAY PROTECTOR</div>
        <div class="loader"></div>
    </div>
    """
    st.markdown(splash_html, unsafe_allow_html=True)
