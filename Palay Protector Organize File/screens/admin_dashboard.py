# screens/admin_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from config import supabase

def show_admin_dashboard():
    # Verify Admin Access
    if st.session_state.user_type != "admin":
        st.error("Access Denied! Admin privileges required.")
        st.session_state.page = "home"
        st.rerun()

    # Custom CSS for FULL WIDTH TABS and buttons
    st.markdown("""
    <style>
    /* MAIN CONTAINER FULL WIDTH */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    /* MALALAKING TABS - FULL WIDTH */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1px;
        width: 100%;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 80px;
        white-space: pre-wrap;
        background-color: #F0F2F6;
        border-radius: 4px 4px 0px 0px;
        padding: 25px 5px;
        font-size: 24px;
        font-weight: bold;
        flex: 1;
        width: 25%;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2E7D32;
        color: white;
    }
    
    /* MALALAKING BUTTONS */
    .stButton button {
        height: 60px;
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Summary Cards
    try:
        total_farmers = len(supabase.table("users").select("*").eq("user_type", "farmer").execute().data)
        total_admins = len(supabase.table("users").select("*").eq("user_type", "admin").execute().data)
        total_detections = len(supabase.table("history").select("*").execute().data)
    except Exception as e:
        st.error(f"❌ Failed to load summary data: {e}")
        st.stop()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div style="background:white;padding:20px;border-radius:10px;text-align:center;box-shadow:0 2px 5px rgba(0,0,0,0.1)">
                <img src="https://cdn-icons-png.flaticon.com/128/1886/1886915.png" width="40" style="margin-bottom:10px">
                <div style="font-size:24px;font-weight:bold;color:#2E7D32">{total_farmers}</div>
                <div style="color:#555">Total Farmers</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div style="background:white;padding:20px;border-radius:10px;text-align:center;box-shadow:0 2px 5px rgba(0,0,0,0.1)">
                <img src="https://cdn-icons-png.flaticon.com/128/3135/3135715.png" width="40" style="margin-bottom:10px">
                <div style="font-size:24px;font-weight:bold;color:#2E7D32">{total_admins}</div>
                <div style="color:#555">Total Admins</div>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div style="background:white;padding:20px;border-radius:10px;text-align:center;box-shadow:0 2px 5px rgba(0,0,0,0.1)">
                <img src="https://cdn-icons-png.flaticon.com/128/18742/18742558.png" width="40" style="margin-bottom:10px">
                <div style="font-size:24px;font-weight:bold;color:#2E7D32">{total_detections}</div>
                <div style="color:#555">Total Detections</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Tabs - FULL WIDTH NA
    tab1, tab2, tab3, tab4 = st.tabs(["USERS", "DETECTION HISTORY", "SETTINGS", "VISUALIZATIONS"])

    # TAB 1: USERS
    with tab1:
        st.subheader("Registered Users")
        try:
            users_data = supabase.table("users").select(
                "id, username, email, phone, user_type, province, municipality, barangay, created_at"
            ).order("created_at", desc=True).execute().data
            users_df = pd.DataFrame(users_data)
        except Exception as e:
            st.error(f"❌ Failed to fetch users: {e}")
            users_df = pd.DataFrame()

        if users_df.empty:
            st.info("No registered users found.")
        else:
            users_df["Address"] = users_df["province"].fillna('') + ", " + users_df["municipality"].fillna('') + ", " + users_df["barangay"].fillna('')
            users_df = users_df.drop(columns=["province", "municipality", "barangay"])
            st.dataframe(users_df, use_container_width=True)

    # TAB 2: DETECTION HISTORY
    with tab2:
        st.subheader("Recent Detection History")
        try:
            history_data = supabase.table("history").select("id, user_id, result, date_detected").order("date_detected", desc=True).limit(50).execute().data
            user_data = supabase.table("users").select("id, username").execute().data
            users_map = {u["id"]: u["username"] for u in user_data}
            for h in history_data:
                h["Username"] = users_map.get(h["user_id"], "Unknown")
            history_df = pd.DataFrame(history_data)
        except Exception as e:
            st.error(f"❌ Failed to fetch history: {e}")
            history_df = pd.DataFrame()

        if history_df.empty:
            st.info("No detection records found.")
        else:
            st.dataframe(history_df, use_container_width=True)
            del_history_id = st.number_input("Enter Detection ID to Delete", min_value=1, step=1)
            if st.button("DELETE DETECTION RECORD", use_container_width=True):
                try:
                    supabase.table("history").delete().eq("id", del_history_id).execute()
                    st.success(f"Detection record #{del_history_id} deleted successfully.")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error deleting record: {e}")

    # TAB 3: SETTINGS (Delete Users)
    with tab3:
        st.subheader("User Management")
        try:
            all_users_data = supabase.table("users").select("id, username, email, user_type, created_at").order("created_at", desc=True).execute().data
            all_users_df = pd.DataFrame(all_users_data)
        except Exception as e:
            st.error(f"❌ Failed to fetch user list: {e}")
            all_users_df = pd.DataFrame()

        if not all_users_df.empty:
            st.dataframe(all_users_df, use_container_width=True)
            del_id = st.number_input("Enter User ID to Delete", min_value=1, step=1)
            if st.button("DELETE USER", use_container_width=True):
                try:
                    supabase.table("history").delete().eq("user_id", del_id).execute()
                    supabase.table("users").delete().eq("id", del_id).execute()
                    st.success(f"User #{del_id} and related detections deleted successfully.")
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Failed to delete user: {e}")
        else:
            st.info("No users available for deletion.")

    # TAB 4: VISUALIZATIONS - WITH BETTER COLORS
    with tab4:
        st.markdown("""
            <style>
            .viz-header { text-align: center; margin-bottom: 20px; }
            .viz-header h2 { color: #1B5E20; font-weight: 800; font-size: 32px; }
            .viz-header p { color: #444; font-size: 16px; margin-top: -8px; }
            .chart-card {
                background-color: #ffffff;
                border-radius: 16px;
                padding: 25px;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
                margin-bottom: 25px;
                width: 100%;
            }
            .chart-title {
                text-align: center;
                font-weight: 700;
                color: #2E7D32;
                font-size: 20px;
                margin-bottom: 15px;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class='viz-header'>
                <h2>Detection Insights Dashboard</h2>
                <p>Visual summary of disease detections and trends</p>
            </div>
        """, unsafe_allow_html=True)

        try:
            viz_data = supabase.table("history").select("result, date_detected").execute().data
            viz_df = pd.DataFrame(viz_data)
        except Exception as e:
            st.error(f"❌ Failed to load visualization data: {e}")
            viz_df = pd.DataFrame()

        if viz_df.empty:
            st.info("No detection data available for visualization.")
        else:
            viz_df["date_detected"] = pd.to_datetime(viz_df["date_detected"], errors="coerce")

            # PIE CHART - VIBRANT COLORS
            st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
            st.markdown("<div class='chart-title'>Most Detected Diseases</div>", unsafe_allow_html=True)
            disease_counts = viz_df["result"].value_counts().reset_index()
            disease_counts.columns = ["Disease", "Count"]
            
            # Vibrant color palette
            colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9']
            
            pie_fig = px.pie(
                disease_counts,
                values="Count",
                names="Disease",
                color_discrete_sequence=colors,
                hole=0.4
            )
            pie_fig.update_traces(
                textinfo="percent+label", 
                pull=[0.05]*len(disease_counts),
                marker=dict(line=dict(color='#000000', width=1))
            )
            pie_fig.update_layout(
                font=dict(size=14),
                showlegend=True,
                height=500
            )
            st.plotly_chart(pie_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # LINE CHART - RED COLOR
            st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
            st.markdown("<div class='chart-title'>Detection Trend Over Time</div>", unsafe_allow_html=True)
            trend_df = viz_df.groupby(viz_df["date_detected"].dt.date)["result"].count().reset_index()
            trend_df.columns = ["Date", "Total Detections"]
            
            line_fig = px.line(
                trend_df, 
                x="Date", 
                y="Total Detections", 
                markers=True, 
                line_shape="spline",
                color_discrete_sequence=["#FF6B6B"]
            )
            line_fig.update_traces(
                line=dict(width=4),
                marker=dict(size=8)
            )
            line_fig.update_layout(
                xaxis_title="Date",
                yaxis_title="Number of Detections",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=400
            )
            st.plotly_chart(line_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

            # BAR CHART - VIRIDIS COLOR SCALE
            st.markdown("<div class='chart-card'>", unsafe_allow_html=True)
            st.markdown("<div class='chart-title'>📊 Weekly Detection Summary</div>", unsafe_allow_html=True)
            viz_df["Week"] = viz_df["date_detected"].dt.strftime("%Y-%U")
            week_df = viz_df.groupby("Week")["result"].count().reset_index()
            week_df.columns = ["Week", "Total Detections"]
            
            bar_fig = px.bar(
                week_df,
                x="Week",
                y="Total Detections",
                text="Total Detections",
                color="Total Detections",
                color_continuous_scale="Viridis"
            )
            bar_fig.update_traces(
                textposition="outside",
                marker=dict(line=dict(color='#000000', width=1))
            )
            bar_fig.update_layout(
                xaxis_title="Week",
                yaxis_title="Number of Detections",
                coloraxis_showscale=False,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                height=400
            )
            st.plotly_chart(bar_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    # MALAKING LOGOUT BUTTON
    st.markdown("---")
    if st.button("LOGOUT", key="admin_logout", use_container_width=True):
        st.session_state.clear()
        st.session_state.page = "login"
        st.rerun()