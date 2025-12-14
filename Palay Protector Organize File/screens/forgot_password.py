import streamlit as st
import time
from utils.otp import generate_otp, send_otp_email
from config import supabase

def forgot_password():
    # ===== REMOVE STREAMLIT DEFAULT GREEN BACKGROUND =====
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: white !important;
    }
    .main > div {
        background: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    
    # ===== CUSTOM CSS =====
    st.markdown("""
    <style>
    .otp-card {
        max-width: 420px;
        margin: auto;
        background: #ffffff;
        padding: 35px;
        border-radius: 16px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.12);
        margin-top: 40px;
        animation: fadeIn 0.5s ease;
    }
    .otp-icon { text-align: center; margin-bottom: 10px; }
    .otp-title { text-align: center; font-size: 26px; color: #1b5e20; font-weight: 800; }
    .otp-subtitle { text-align: center; font-size: 15px; color: #6c757d; margin-bottom: 20px; }

    /* IMPORTANTE: I-force ang white background sa buong page */
    .stApp {
        background-color: white !important;
    }
    html, body, [data-testid="stAppViewContainer"] {
        background-color: white !important;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='otp-card'>", unsafe_allow_html=True)

    # ICON
    st.markdown("""
    <div class="otp-icon">
        <img src="https://cdn-icons-png.flaticon.com/128/6195/6195699.png" width="80">
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='otp-title'>Forgot Password</div>", unsafe_allow_html=True)
    st.markdown("<div class='otp-subtitle'>Enter your email to receive a verification code</div>", unsafe_allow_html=True)

    email = st.text_input("Email Address", placeholder="your.email@gmail.com")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Send OTP", type="primary", use_container_width=True):
            if not email.strip():
                st.warning("Please enter your email.")
            else:
                try:
                    res = supabase.table("users").select("*").eq("email", email).execute()

                    if not res.data:
                        st.error("Email not found.")
                    else:
                        otp = generate_otp()
                        ok = send_otp_email(email, otp)

                        if ok:
                            st.session_state.generated_otp = otp
                            st.session_state.otp_email = email
                            st.session_state.otp_start_time = time.time()
                            st.session_state.page = "otp_verification"
                            st.rerun()
                        else:
                            st.error("Failed to send OTP.")

                except Exception as e:
                    st.error(f"Supabase error: {e}")

    with col2:
        if st.button("Back", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)