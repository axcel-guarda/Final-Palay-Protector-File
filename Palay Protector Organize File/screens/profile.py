# screens/profile.py
import streamlit as st
from config import supabase
from components.navigation import show_bottom_nav
from utils.database import get_user_stats

def show_profile():
    # Custom Styling
    st.markdown("""
    <style>
    .profile-header {
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(46, 125, 50, 0.25);
    }
    .profile-avatar img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        border: 3px solid white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .stats-row {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: stretch;
        gap: 10px;
        flex-wrap: nowrap;
        overflow-x: auto;
        padding-bottom: 10px;
        scrollbar-width: none;
    }
    .stats-row::-webkit-scrollbar { display: none; }

    .stat-box {
        flex: 0 0 180px;
        background: #fff;
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border-top: 4px solid #4CAF50;
    }
    .stat-box:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 15px rgba(76,175,80,0.25);
    }
    .stat-box img {
        width: 40px;
        height: 40px;
        margin-bottom: 8px;
    }
    .stat-value {
        font-size: 22px;
        font-weight: 800;
        color: #2E7D32;
        margin-bottom: 3px;
    }
    .stat-label {
        color: #555;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.4px;
    }
    .activity-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 12px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        border-left: 5px solid #4CAF50;
        transition: all 0.3s ease;
    }
    .activity-card:hover {
        transform: scale(1.01);
        box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    }
    
    /* BUTTON STYLING - KAGAYA NG IBAng SCREENS */
    div.stButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        cursor: pointer !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3) !important;
        margin: 1rem 0 !important;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 16px rgba(76, 175, 80, 0.4) !important;
        background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Profile Header
    st.markdown(f"""
    <div class="profile-header">
        <div class="profile-avatar">
            <img src="https://cdn-icons-png.flaticon.com/128/3135/3135715.png">
        </div>
        <h2 style="margin: 10px 0;">{st.session_state.logged_user}</h2>
        <p style="opacity: 0.9;">{st.session_state.user_type}@palayprotector.com</p>
        <p style="font-size:13px; opacity:0.8;">Member since October 2024</p>
    </div>
    """, unsafe_allow_html=True)

    # Fetch Stats
    stats = get_user_stats(st.session_state.user_id)
    total_scans = stats["total_scans"]
    healthy_count = stats["healthy_count"]
    detected_count = stats["detected_count"]
    accuracy_rate = stats["accuracy_rate"]

    # Stat Cards
    st.markdown(f"""
    <div class='stats-row'>
        <div class="stat-box">
            <img src="https://cdn-icons-png.flaticon.com/128/1055/1055687.png">
            <div class="stat-value">{total_scans}</div>
            <div class="stat-label">Total Scans</div>
        </div>
        <div class="stat-box">
            <img src="https://cdn-icons-png.flaticon.com/128/5610/5610944.png">
            <div class="stat-value">{healthy_count}</div>
            <div class="stat-label">Healthy Plants</div>
        </div>
        <div class="stat-box">
            <img src="https://cdn-icons-png.flaticon.com/128/564/564619.png">
            <div class="stat-value">{detected_count}</div>
            <div class="stat-label">Diseases Found</div>
        </div>
        <div class="stat-box">
            <img src="https://cdn-icons-png.flaticon.com/128/2593/2593635.png">
            <div class="stat-value">{accuracy_rate:.1f}%</div>
            <div class="stat-label">Accuracy Rate</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Recent Activity Section
    st.markdown("<h3 style='text-align:center;color:#2E7D32;margin-top:2rem;'>Recent Activity</h3>", unsafe_allow_html=True)

    try:
        recent = supabase.table("history").select("result, date_detected").eq("user_id", st.session_state.user_id).order("date_detected", desc=True).limit(5).execute().data
        if recent:
            for scan in recent:
                result = scan["result"]
                color = "#4CAF50" if "Healthy" in result else "#f44336"
                icon = "https://cdn-icons-png.flaticon.com/128/5610/5610944.png" if "Healthy" in result else "https://cdn-icons-png.flaticon.com/128/564/564619.png"
                
                # Date formatting
                date_str = scan["date_detected"]
                if "T" in date_str:
                    date_part, time_part = date_str.split("T")
                    date_part = date_part.replace("-", ".")
                    time_part = time_part[:5]  # Get only HH:MM
                    formatted_date = f"{date_part}:{time_part}"
                else:
                    formatted_date = date_str[:16].replace("-", ".").replace(" ", ":")
                
                st.markdown(f"""
                <div class="activity-card">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <div style="display:flex;align-items:center;gap:10px;">
                            <img src="{icon}" width="40">
                            <div>
                                <div style="font-weight:700;color:#333;font-size:15px;">{result}</div>
                                <div style="font-size:12px;color:#777;font-family:monospace;">{formatted_date}</div>
                            </div>
                        </div>
                        <div style="background:{color};color:white;padding:6px 12px;border-radius:20px;font-weight:600;font-size:12px;">
                            {'Healthy' if 'Healthy' in result else 'Disease'}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No recent detections yet.")
    except Exception as e:
        st.warning(f"Could not load recent scans: {e}")

    # Logout Button - BAGONG STYLING KAGAYA NG IBAng SCREENS
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Logout", use_container_width=True, type="primary"):
            st.session_state.clear()
            st.session_state.page = "login"
            st.rerun()

    show_bottom_nav("profile")