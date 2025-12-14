import streamlit as st
import time
import hashlib
from config import supabase

def change_password():
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: white !important;
    }
    </style>
    """, unsafe_allow_html=True)



def change_password():

    st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"]

        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .otp-card {
            max-width: 420px;
            margin: 70px auto;
            background: white;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0px 12px 32px rgba(0,0,0,0.25);
            animation: fadeIn 0.5s ease;
        }
        .otp-title { text-align:center; color:#1b5e20; font-size:26px; font-weight:800; }
        .otp-subtitle { text-align:center; color:#555; }

        @keyframes fadeIn {
            from { opacity:0; transform:translateY(20px); }
            to { opacity:1; transform:translateY(0); }
        }
    </style>
    """, unsafe_allow_html=True)


    st.markdown("<div class='otp-card'>", unsafe_allow_html=True)

    st.markdown("""
    <div class="otp-icon" style="text-align:center;">
        <img src="https://cdn-icons-png.flaticon.com/128/2889/2889676.png" width="80">
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="otp-title">Create New Password</div>', unsafe_allow_html=True)
    st.markdown('<div class="otp-subtitle">Enter a secure password</div>', unsafe_allow_html=True)

    new_pw = st.text_input("New Password", type="password")
    confirm_pw = st.text_input("Confirm Password", type="password")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Save", type="primary", use_container_width=True):
            if not new_pw or not confirm_pw:
                st.error("Fill out both fields.")
            elif new_pw != confirm_pw:
                st.error("Passwords do not match.")
            elif len(new_pw) < 6:
                st.error("Password must be at least 6 characters.")
            else:
                hashed = hashlib.sha256(new_pw.encode()).hexdigest()

                supabase.table("users").update(
                    {"password": hashed}
                ).eq("email", st.session_state.otp_email).execute()

                st.success("Password updated!")

                # CLEAR SESSION STATE
                for k in ['generated_otp', 'otp_start_time', 'otp_email']:
                    st.session_state.pop(k, None)

                time.sleep(1)
                st.session_state.page = "login"
                st.rerun()

    with col2:
        if st.button("Cancel", use_container_width=True):
            st.session_state.page = "login"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
