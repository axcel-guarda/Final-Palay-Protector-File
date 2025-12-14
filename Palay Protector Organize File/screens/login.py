# screens/login.py
import streamlit as st
import hashlib
import time
from config import supabase
from components.header import show_header

def show_login():
    show_header()



    

    # USERNAME INPUT
    username = st.text_input("Username", placeholder="Enter your username")

    # PASSWORD INPUT
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    # FORGOT PASSWORD — placed RIGHT side using columns
    col1, col2 = st.columns([5, 2])
    with col2:
        if st.button("Forgot Password?"):
            st.session_state.page = "forgot_password"
            st.rerun()

    # LOGIN BUTTON
    if st.button("LOG IN", use_container_width=True):
        if not username or not password:
            st.warning("⚠️ Please enter both username and password.")
        else:
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()

            try:
                res = (
                    supabase.table("users")
                    .select("id, username, user_type")
                    .eq("username", username)
                    .eq("password", hashed_pw)
                    .execute()
                )

                if res.data:
                    user = res.data[0]
                    st.session_state.user_id = user["id"]
                    st.session_state.logged_user = user["username"]
                    st.session_state.user_type = user["user_type"]
                    st.session_state.login_time = time.strftime("%Y-%m-%d %H:%M:%S")

                    if user["user_type"] == "admin":
                        st.session_state.page = "admin_dashboard"
                    else:
                        st.session_state.page = "home"

                    st.rerun()

                else:
                    st.error("❌ Invalid username or password.")

            except Exception as e:
                st.error(f"⚠️ Database query error: {e}")

    # SIGN-UP BUTTON
    if st.button("SIGN UP", use_container_width=True):
        st.session_state.page = "signup"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

