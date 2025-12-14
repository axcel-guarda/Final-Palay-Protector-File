import streamlit as st
import time
from utils.otp import generate_otp, send_otp_email

def otp_verification():
    # REMOVE DEFAULT UI + BACKGROUND
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 0 !important;
        margin: 0 !important;
    }

    .block-container {
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* Hide Streamlit's default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

    # CARD STYLE
    st.markdown("""
    <style>
    .otp-card {
        max-width: 420px;
        margin: 80px auto;
        background: white;
        padding: 35px;
        border-radius: 18px;
        box-shadow: 0px 12px 32px rgba(0,0,0,0.25);
        animation: fadeIn 0.5s ease;
    }
    .otp-title { 
        text-align: center; 
        font-size: 26px; 
        font-weight: 800; 
        color: #1b5e20; 
        margin-bottom: 10px;
    }
    .otp-subtitle { 
        text-align: center; 
        color: #555; 
        margin-bottom: 10px; 
        font-size: 14px;
    }
    .otp-icon { text-align: center; margin-bottom: 10px; }

    .timer-text {
        text-align: center;
        font-size: 34px;
        font-weight: 900;
        margin-top: 10px;
        margin-bottom: 20px;
        color: #1b5e20;
        animation: glow 1.8s ease-in-out infinite;
    }

    .expired-text {
        text-align: center;
        font-size: 34px;
        font-weight: 900;
        color: #d32f2f;
        margin-bottom: 20px;
    }
    
    /* Style for OTP input */
    .stTextInput input {
        text-align: center;
        font-size: 24px;
        letter-spacing: 8px;
        font-weight: bold;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @keyframes glow {
        0% { text-shadow: 0px 0px 5px rgba(76,175,80,0.3); }
        50% { text-shadow: 0px 0px 15px rgba(76,175,80,0.7); }
        100% { text-shadow: 0px 0px 5px rgba(76,175,80,0.3); }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='otp-card'>", unsafe_allow_html=True)

    # ICON
    st.markdown("""
    <div class="otp-icon">
        <img src="https://cdn-icons-png.flaticon.com/128/732/732200.png" width="80">
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="otp-title">Verify OTP</div>', unsafe_allow_html=True)
    
    # Check if email exists in session state
    if 'otp_email' not in st.session_state:
        st.session_state.otp_email = "simansano32@gmail.com"  # Default email
    
    st.markdown(
        f'<div class="otp-subtitle">Code sent to <b>{st.session_state.otp_email}</b></div>',
        unsafe_allow_html=True
    )

    # ---------- TIMER ----------
    timer_placeholder = st.empty()

    # Initialize timer if not exists
    if 'otp_start_time' not in st.session_state:
        st.session_state.otp_start_time = time.time()
    
    # Initialize OTP if not exists
    if 'generated_otp' not in st.session_state:
        st.session_state.generated_otp = generate_otp()
        send_otp_email(st.session_state.otp_email, st.session_state.generated_otp)

    current_time = time.time()
    elapsed_time = current_time - st.session_state.otp_start_time
    remaining = max(0, 180 - int(elapsed_time))

    if remaining > 0:
        m = remaining // 60
        s = remaining % 60
        timer_placeholder.markdown(
            f"<div class='timer-text'>⏳ {m:02d}:{s:02d}</div>", unsafe_allow_html=True
        )
    else:
        timer_placeholder.markdown(
            "<div class='expired-text'>EXPIRED</div>", unsafe_allow_html=True
        )

    # OTP Input
    otp = st.text_input("Enter 6-digit OTP", max_chars=6, placeholder="000000", key="otp_input")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit", type="primary", use_container_width=True):
            current_time = time.time()
            elapsed_time = current_time - st.session_state.otp_start_time
            remaining = max(0, 180 - int(elapsed_time))

            if not otp:
                st.error("Enter your OTP first.")
            elif remaining <= 0:
                st.error("OTP expired. Please resend.")
            elif len(otp) != 6 or not otp.isdigit():
                st.error("Please enter a valid 6-digit OTP.")
            elif otp == st.session_state.generated_otp:
                st.success("OTP verified!")
                st.session_state.page = "change_password"
                st.rerun()
            else:
                st.error("Invalid OTP.")

    with col2:
        if st.button("Resend OTP", use_container_width=True):
            new_otp = generate_otp()
            st.session_state.generated_otp = new_otp
            st.session_state.otp_start_time = time.time()
            
            # Send OTP via email
            success = send_otp_email(st.session_state.otp_email, new_otp)
            if success:
                st.success("New OTP sent!")
            else:
                st.error("Failed to send OTP. Please try again.")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # AUTO REFRESH for timer
    if remaining > 0:
        time.sleep(1)
        st.rerun()