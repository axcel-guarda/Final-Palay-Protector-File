# components/navigation.py
import streamlit as st

def show_bottom_nav(active_page):
    st.markdown("""
    <style>
    /* BOTTOM NAV CONTAINER */
    .bottom-nav-container {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        background: white;
        border-top: 3px solid #4CAF50;
        padding: 15px 0;
        z-index: 9999;
    }

    /* REMOVE ALL NORMAL STATES */
    .bottom-nav-container .stButton > button {
        background: transparent !important;
        border: none !important;
        color: #666 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        padding: 10px 0 !important;
        width: 100% !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        outline: none !important;
    }

    /* REMOVE HOVER */
    .bottom-nav-container .stButton > button:hover {
        background: transparent !important;
        color: #666 !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* REMOVE ACTIVE STATE */
    .bottom-nav-container .stButton > button:active {
        background: transparent !important;
        color: #666 !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* REMOVE FOCUS */
    .bottom-nav-container .stButton > button:focus {
        background: transparent !important;
        color: #666 !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* REMOVE STREAMLIT BUILT-IN PRESSED + FOCUS GLOW */
    button[kind="secondary"]:focus,
    button[kind="secondary"]:active,
    .stButton > button:focus,
    .stButton > button:active,
    .stButton > button:focus:not(:active),
    .stButton > button:focus-visible {
        background: transparent !important;
        color: #666 !important;
        border: none !important;
        box-shadow: none !important;
        outline: none !important;
    }

    .stButton > button:active:not(:disabled) {
        background: transparent !important;
        box-shadow: none !important;
    }

    button:focus-visible {
        outline: none !important;
        box-shadow: none !important;
    }

    /* ACTIVE PAGE TEXT STYLE */
    .active-nav-text {
        color: #2e7d32 !important;
        font-weight: 700 !important;
        text-decoration: underline;
        text-decoration-thickness: 2px;
        text-underline-offset: 6px;
        text-align: center;
        font-size: 16px;
        padding: 10px 0;
    }

    /* INACTIVE PAGE TEXT */
    .inactive-nav-text {
        color: #666 !important;
        font-weight: 500 !important;
        text-align: center;
        font-size: 16px;
        padding: 10px 0;
    }

    /* EXTRA PAGE BOTTOM SPACE */
    .main .block-container {
        padding-bottom: 80px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="bottom-nav-container">', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if active_page == "home":
            st.markdown('<div class="active-nav-text">Home</div>', unsafe_allow_html=True)
        else:
            if st.button("Home", key="btn_home", use_container_width=True):
                st.session_state.page = "home"
                st.rerun()

    with col2:
        if active_page == "library":
            st.markdown('<div class="active-nav-text">Library</div>', unsafe_allow_html=True)
        else:
            if st.button("Library", key="btn_library", use_container_width=True):
                st.session_state.page = "library"
                st.rerun()

    with col3:
        if active_page == "profile":
            st.markdown('<div class="active-nav-text">Profile</div>', unsafe_allow_html=True)
        else:
            if st.button("Profile", key="btn_profile", use_container_width=True):
                st.session_state.page = "profile"
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


def hide_bottom_nav():
    st.markdown("""
    <style>
    .bottom-nav-container {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
 