# app.py - MAIN ENTRY POINT
import streamlit as st
import time
from components.styles import apply_custom_styles, show_splash_screen

# Import all screen handlers
from screens import (
    show_login, show_signup, show_forgot_password, 
    show_change_password, show_otp_verification,
    show_home, show_detect, show_history, 
    show_profile, show_library, show_admin_dashboard
)


def initialize_session_state():
    """Initialize all session state variables"""
    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "user_id" not in st.session_state:
        st.session_state.user_id = None
    if "logged_user" not in st.session_state:
        st.session_state.logged_user = None
    if "user_type" not in st.session_state:
        st.session_state.user_type = None
    if "result_lang" not in st.session_state:
        st.session_state.result_lang = "english"
    if "translations" not in st.session_state:
        st.session_state.translations = {}
    if "splash_shown" not in st.session_state:
        st.session_state.splash_shown = False


def main():
    """Main application function"""

    initialize_session_state()
    apply_custom_styles()

    # Show splash screen only once
    if not st.session_state.splash_shown:
        st.session_state.splash_shown = True
        show_splash_screen()
        time.sleep(4)
        st.rerun()

    # PAGE ROUTING
    if st.session_state.page == "login":
        show_login()
    elif st.session_state.page == "signup":
        show_signup()
    elif st.session_state.page == "forgot_password":
        show_forgot_password()
    elif st.session_state.page == "otp_verification":
        show_otp_verification()
    elif st.session_state.page == "change_password":
        show_change_password()
    elif st.session_state.page == "admin_dashboard":
        show_admin_dashboard()
    elif st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "detect":
        show_detect()
    elif st.session_state.page == "history":
        show_history()
    elif st.session_state.page == "profile":
        show_profile()
    elif st.session_state.page == "library":
        show_library()


# Run the app
if __name__ == "__main__":
    main()
