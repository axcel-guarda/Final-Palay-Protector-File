# screens/home.py
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime, timedelta
from components.header import show_header
from components.navigation import show_bottom_nav

def show_home():
    # Page styling
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
            
            * {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            }
            
            .main .block-container {
                max-width: 1100px;
                padding: 2rem 1.5rem;
            }
            
            /* FULL WIDTH BUTTONS FOR STREAMLIT */
            .stButton > button {
                width: 100% !important;
                background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%) !important;
                color: white !important;
                border: none !important;
                border-radius: 14px !important;
                padding: 16px 24px !important;
                font-size: 16px !important;
                font-weight: 600 !important;
                cursor: pointer !important;
                transition: all 0.3s ease !important;
                text-align: center !important;
                box-shadow: 0 4px 12px rgba(46, 125, 50, 0.3) !important;
                margin-top: 10px !important;
                display: block !important;
                min-height: 54px !important;
            }
            
            .stButton > button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 16px rgba(46, 125, 50, 0.4) !important;
                background: linear-gradient(135deg, #1b5e20 0%, #2e7d32 100%) !important;
            }
            
            .hero-section {
                text-align: center;
                padding: 2rem 0 2.5rem;
                position: relative;
            }
            
            .avatar-container {
                margin-bottom: 1.5rem;
                position: relative;
                display: inline-block;
            }
            
            .avatar-circle {
                width: 90px;
                height: 90px;
                background: linear-gradient(135deg, #A8E6A1 0%, #7BC96F 100%);
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto;
                box-shadow: 0 8px 24px rgba(46, 125, 50, 0.2);
                position: relative;
                animation: pulse-subtle 3s ease-in-out infinite;
            }
            
            @keyframes pulse-subtle {
                0%,100% { box-shadow: 0 8px 24px rgba(46, 125, 50, 0.2); }
                50% { box-shadow: 0 8px 32px rgba(46, 125, 50, 0.3); }
            }
            
            .avatar-icon {
                font-size: 48px;
            }
            
            .welcome-header {
                font-size: 32px;
                font-weight: 800;
                background: linear-gradient(135deg, #2e7d32 0%, #1b5e20 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 0.5rem;
                letter-spacing: -0.5px;
            }
            
            .welcome-username {
                background: linear-gradient(135deg, #4CAF50 0%, #2e7d32 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .welcome-subtitle {
                font-size: 16px;
                color: #6c757d;
                font-weight: 400;
                margin-top: 0.5rem;
            }
            
            .features-section {
                margin: 2.5rem 0;
            }
            
            /* GREEN FEATURE CARDS */
            .feature-card-modern {
                background: linear-gradient(135deg, #A8E6A3 0%, #66BB6A 100%);
                border-radius: 20px;
                padding: 2rem;
                box-shadow: 0 8px 24px rgba(46, 125, 50, 0.15);
                transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
                border: 1px solid rgba(255, 255, 255, 0.5);
                position: relative;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                min-height: 320px;
                margin-bottom: 1.5rem;
            }
            
            .feature-card-modern:hover {
                transform: translateY(-8px);
                box-shadow: 0 16px 40px rgba(46, 125, 50, 0.25);
            }
            
            .feature-card-container {
                display: flex;
                flex-direction: column;
                height: 100%;
            }
            
            .feature-icon-wrapper {
                width: 80px;
                height: 80px;
                background: white;
                border-radius: 18px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 0 auto 1.25rem;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
            
            .feature-icon-wrapper img {
                width: 45px;
                height: 45px;
            }
            
            .feature-title {
                font-size: 22px;
                font-weight: 700;
                color: #1b5e20;
                margin-bottom: 0.75rem;
                text-align: center;
            }
            
            .feature-description {
                font-size: 15px;
                color: #2d5016;
                text-align: center;
                margin-bottom: 1.5rem;
                line-height: 1.6;
                flex-grow: 1;
            }
            
            .insights-section {
                background: linear-gradient(135deg, #ffffff 0%, #f1f8e9 100%);
                border-radius: 20px;
                padding: 2rem;
                margin: 2rem 0;
                border-left: 5px solid #4CAF50;
                box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
            }
            
            .insights-header {
                display: flex;
                align-items: center;
                gap: 12px;
                margin-bottom: 1rem;
            }
            
            .insights-icon {
                width: 40px;
                height: 40px;
                background: linear-gradient(135deg, #4CAF50, #2e7d32);
                border-radius: 10px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 20px;
                color: white;
            }
            
            .insights-title {
                font-size: 22px;
                font-weight: 700;
                color: #2e7d32;
                margin: 0;
            }
            
            .insights-content {
                font-size: 16px;
                color: #555;
                line-height: 1.7;
                margin-bottom: 1.5rem;
            }
            
            .insights-highlight {
                background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
                padding: 4px 12px;
                border-radius: 8px;
                font-weight: 700;
                color: #f57f17;
            }
            
            .stats-badge {
                display: inline-flex;
                align-items: center;
                gap: 6px;
                background: white;
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: 600;
                color: #2e7d32;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
                margin-right: 1rem;
                border: 1px solid #c8e6c9;
            }
        </style>
    """, unsafe_allow_html=True)

    # Hero Section
    show_header()

    # Weather Forecast Section
    CITY = "Sorsogon"
    COUNTRY = "Philippines"

    def get_7day_forecast(city):
        today = datetime.now()
        temp_ranges = [
            {"max": 32, "min": 25, "icon": "01d"},
            {"max": 31, "min": 24, "icon": "02d"},
            {"max": 33, "min": 26, "icon": "03d"},
            {"max": 30, "min": 25, "icon": "10d"},
            {"max": 32, "min": 26, "icon": "01d"},
            {"max": 31, "min": 25, "icon": "02d"},
            {"max": 29, "min": 24, "icon": "04d"}
        ]
        forecast_data = []
        for i in range(7):
            current_date = today + timedelta(days=i)
            forecast_data.append({
                "day_short": current_date.strftime("%a"),
                "temp_max": temp_ranges[i]["max"],
                "temp_min": temp_ranges[i]["min"],
                "icon": temp_ranges[i]["icon"]
            })
        return forecast_data

    forecast = get_7day_forecast(CITY)

    if forecast:
        weather_html = f"""
        <style>
        .weather-box {{
            background: linear-gradient(135deg, #f6fff8 0%, #ffffff 100%);
            border-radius: 36px;
            padding: 2.5rem 2rem;
            margin: 2rem auto;
            max-width: 900px;
            border: 3px solid rgba(46,125,50,0.35);
            box-shadow: 0 15px 35px rgba(46,125,50,0.2);
        }}

        .weather-title {{
            font-size: 18px;
            font-weight: 700;
            color: #2e7d32;
            text-align: center;
            margin-bottom: 1.4rem;
        }}

        .forecast-container {{
            display: flex;
            gap: 14px;
            padding: 1rem;
            overflow-x: auto;
            overflow-y: hidden;
            justify-content: flex-start;
        }}

        .forecast-container::-webkit-scrollbar {{
            height: 8px;
        }}

        .forecast-container::-webkit-scrollbar-thumb {{
            background: #4CAF50;
            border-radius: 10px;
        }}

        .forecast-card {{
            background: #ffffff;
            border-radius: 22px;
            padding: 1rem;
            min-width: 95px;
            text-align: center;
            border: 2px solid #5fbf68;
            box-shadow: 0 4px 14px rgba(46,125,50,0.15);
            transition: 0.3s ease;
            flex-shrink: 0;
        }}

        .forecast-card:hover {{
            transform: translateY(-5px);
            border-color: #2e7d32;
        }}

        .forecast-card img {{
            width: 44px;
            height: 44px;
            margin: 6px auto;
        }}

        .forecast-day {{
            font-size: 13px;
            font-weight: 700;
            color: #2e7d32;
        }}

        .forecast-temp {{
            font-size: 12px;
            font-weight: 600;
            color: #333;
            margin-top: 5px;
        }}
        </style>

        <div class="weather-box">
            <div class="weather-title">
                7-Day Forecast ({CITY}, {COUNTRY})
            </div>
            <div class="forecast-container">
        """

        for day in forecast:
            icon_url = f"https://openweathermap.org/img/wn/{day['icon']}@2x.png"
            weather_html += f"""
            <div class="forecast-card">
                <div class="forecast-day">{day['day_short']}</div>
                <img src="{icon_url}">
                <div class="forecast-temp">{day['temp_max']}° / {day['temp_min']}°</div>
            </div>
            """

        weather_html += """
            </div>
        </div>
        """
        components.html(weather_html, height=320, scrolling=False)

    # Feature Cards Section - WITH GREEN BOXES AND FULL-WIDTH BUTTONS
    st.markdown('<div class="features-section">', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")

    with col1:
        # Detect Disease Card
        st.markdown("""
        <div class="feature-card-modern">
            <div class="feature-card-container">
                <div class="feature-icon-wrapper">
                    <img src="https://cdn-icons-png.flaticon.com/512/1150/1150652.png" alt="Detect Disease">
                </div>
                <div class="feature-title">Detect Disease</div>
                <div class="feature-description">
                    Upload images of your palay plants and get instant AI-powered disease detection results to protect your crops.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Full-width button
        if st.button("Start Detection", key="detect_button"):
            st.session_state.page = "detect"
            st.rerun()

    with col2:
        # View History Card
        st.markdown("""
        <div class="feature-card-modern">
            <div class="feature-card-container">
                <div class="feature-icon-wrapper">
                    <img src="https://cdn-icons-png.flaticon.com/512/12901/12901923.png" alt="View History">
                </div>
                <div class="feature-title">View History</div>
                <div class="feature-description">
                    Access your complete scan history and track disease patterns over time for better crop management and yield optimization.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Full-width button
        if st.button("View Records", key="history_button"):
            st.session_state.page = "history"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Expert Insights Section
    st.markdown("""
    <div class="insights-section">
        <div class="insights-header">
            <div class="insights-icon">💡</div>
            <div class="insights-title">Expert Insight</div>
        </div>
        <div class="insights-content">
            Early detection of palay diseases can increase your yield by up to 
            <span class="insights-highlight">30%</span>. Regular monitoring and weekly image uploads 
            ensure optimal crop health and maximum productivity.
        </div>
        <div>
            <span class="stats-badge">✓ AI-Powered Analysis</span>
            <span class="stats-badge">✓ Real-time Results</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Bottom Navigation
    show_bottom_nav('home')