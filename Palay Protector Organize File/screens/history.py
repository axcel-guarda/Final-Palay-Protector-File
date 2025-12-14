# screens/history.py
import streamlit as st
from config import supabase
from components.navigation import show_bottom_nav
from datetime import datetime

def show_history():
    # Add main content padding
    st.markdown("""
    <style>
    .main-content {
        padding-bottom: 80px;
    }
    </style>
    <div class="main-content">
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:linear-gradient(135deg, #e8f5e9, #c8e6c9); color:#1b5e20; 
                padding:20px; border-radius:12px; text-align:center; margin-bottom:20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h1 style="margin:0; font-size:32px; font-weight:700;">🌱 Detection History</h1>
        <p style="margin:5px 0 0 0; font-size:16px; opacity:0.8;">Track your plant health over time</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.get('user_id') is None:
        st.error("🔒 Please log in to view your history.")
    else:
        try:
            # Simple and safe query
            res = supabase.table("history") \
                .select("date_detected, result, severity, confidence") \
                .eq("user_id", st.session_state.user_id) \
                .order("date_detected", desc=True) \
                .execute()
            
            rows = res.data

            if not rows:
                st.info("📊 No history records yet. Start scanning your plants!")
            else:
                # Create summary statistics
                total_scans = len(rows)
                healthy_count = sum(1 for row in rows if str(row.get("result", "")).lower() == "healthy")
                disease_count = total_scans - healthy_count
                
                # Display summary cards - MALALAKI at SIMPLE
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.markdown(f"""
                    <div style="background:white; padding:25px; border-radius:15px; text-align:center; 
                                box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 2px solid #4CAF50; 
                                min-height: 120px; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-size: 42px; font-weight: bold; color: #2E7D32; margin-bottom: 8px;">{total_scans}</div>
                        <div style="font-size: 16px; color: #666; font-weight: 600;">Total Scans</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"""
                    <div style="background:white; padding:25px; border-radius:15px; text-align:center; 
                                box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 2px solid #FF9800;
                                min-height: 120px; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-size: 42px; font-weight: bold; color: #EF6C00; margin-bottom: 8px;">{disease_count}</div>
                        <div style="font-size: 16px; color: #666; font-weight: 600;">Disease Detected</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    st.markdown(f"""
                    <div style="background:white; padding:25px; border-radius:15px; text-align:center; 
                                box-shadow: 0 4px 12px rgba(0,0,0,0.15); border: 2px solid #2196F3;
                                min-height: 120px; display: flex; flex-direction: column; justify-content: center;">
                        <div style="font-size: 42px; font-weight: bold; color: #1565C0; margin-bottom: 8px;">{healthy_count}</div>
                        <div style="font-size: 16px; color: #666; font-weight: 600;">Healthy Plants</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                # Create and display table
                table_html = """
                <style>
                    .history-table {
                        width: 100%;
                        border-collapse: collapse;
                        font-size: 15px;
                        margin: 10px 0;
                        background: white;
                        border-radius: 12px;
                        overflow: hidden;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
                    }
                    .history-table th {
                        background: linear-gradient(135deg, #4CAF50, #2E7D32);
                        color: white;
                        padding: 16px 12px;
                        text-align: center;
                        font-weight: 600;
                        font-size: 16px;
                    }
                    .history-table td {
                        padding: 16px 12px;
                        text-align: center;
                        border-bottom: 1px solid #e0e0e0;
                    }
                    .history-table tr:nth-child(even) {
                        background: #f8f9fa;
                    }
                    .history-table tr:hover {
                        background: #f1f8e9;
                    }
                    .remedy-btn {
                        display: inline-block;
                        background: linear-gradient(135deg, #2E7D32, #1B5E20);
                        color: white !important;
                        padding: 10px 20px;
                        border-radius: 25px;
                        text-decoration: none;
                        font-size: 14px;
                        font-weight: 600;
                        transition: all 0.3s;
                        border: none;
                        cursor: pointer;
                        white-space: nowrap;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }
                    .remedy-btn:hover {
                        background: linear-gradient(135deg, #43A047, #2E7D32);
                        transform: translateY(-2px);
                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                    }
                    .severity-badge {
                        padding: 8px 16px;
                        border-radius: 25px;
                        font-weight: 600;
                        color: white;
                        font-size: 14px;
                        display: inline-block;
                        min-width: 100px;
                    }
                    .high { background: linear-gradient(135deg, #f44336, #c62828); }
                    .moderate { background: linear-gradient(135deg, #ff9800, #ef6C00); }
                    .low { background: linear-gradient(135deg, #4CAF50, #2E7D32); }
                    .none { background: linear-gradient(135deg, #9e9e9e, #757575); }
                    .date-cell {
                        font-weight: 600;
                        color: #333;
                    }
                    .disease-cell {
                        font-weight: 600;
                        color: #2E7D32;
                    }
                </style>

                <table class="history-table">
                    <tr>
                        <th>Date</th>
                        <th>Disease</th>
                        <th>Severity</th>
                        <th>Confidence</th>
                        <th>Action</th>
                    </tr>
                """

                for scan in rows:
                    date_str = scan.get("date_detected", "")
                    # Format date - gaya ng nasa picture: "Nov 30, 2025"
                    try:
                        if "T" in date_str:
                            date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                            formatted_date = date_obj.strftime("%b %d, %Y")  # "Nov 30, 2025" format
                        else:
                            # If already in string format, try to parse
                            date_obj = datetime.strptime(date_str[:10], "%Y-%m-%d")
                            formatted_date = date_obj.strftime("%b %d, %Y")
                    except:
                        formatted_date = date_str[:10] if date_str else "Unknown"
                    
                    disease = scan.get("result", "Unknown")
                    severity = scan.get("severity", "N/A")
                    confidence = scan.get("confidence", None)

                    # Set color class for severity
                    severity_lower = str(severity).lower()
                    if "high" in severity_lower:
                        severity_class = "high"
                    elif "moderate" in severity_lower or "medium" in severity_lower:
                        severity_class = "moderate"
                    elif "low" in severity_lower or "none" in severity_lower or "healthy" in str(disease).lower():
                        severity_class = "low"
                    else:
                        severity_class = "none"
                    
                    # Format confidence
                    try:
                        confidence_display = f"{float(confidence):.1f}%" if confidence is not None else "—"
                    except:
                        confidence_display = "—"

                    # Only show remedy button for disease cases
                    if str(disease).lower() != "healthy":
                        action_button = f'<a href="https://collab-app.com/dashboard?disease={disease}" target="_blank" class="remedy-btn">View Remedy</a>'
                    else:
                        action_button = '<span style="color:#4CAF50; font-weight:600;">Healthy Plant</span>'

                    table_html += f"""
                    <tr>
                        <td class="date-cell">{formatted_date}</td>
                        <td class="disease-cell">{disease}</td>
                        <td><span class="severity-badge {severity_class}">{severity}</span></td>
                        <td style="font-weight:600;">{confidence_display}</td>
                        <td>{action_button}</td>
                    </tr>
                    """

                table_html += "</table>"
                
                # Display the table
                st.components.v1.html(table_html, height=600, scrolling=True)

        except Exception as e:
            st.error(f"❌ Error loading history: {str(e)}")

    st.markdown("</div>", unsafe_allow_html=True)  # Close main-content div
    
    # Bottom Navigation - DITO NA GAGAMITIN ANG BAGONG NAVIGATION
    show_bottom_nav('history')