import streamlit as st
import base64
import io
import tempfile
from datetime import datetime
from PIL import Image
from config import supabase
from components.header import show_header
from components.navigation import show_bottom_nav
from utils.helpers import init_client
from utils.detection_data import DISEASE_INFO, normalize_disease_name

def show_detect():
    # Initialize translation state for detection result
    if 'result_lang' not in st.session_state:
        st.session_state.result_lang = "english"

   

    # Page UI - ALL GREEN BUTTONS
    st.markdown("""
        <style>
            .stApp { 
                background: linear-gradient(135deg, #e8f5e9 0%, #ffffff 100%) !important; 
                padding-bottom: 80px;
            }
            
            /* HIDE STREAMLIT DEFAULT UPLOADER TEXT */
            [data-testid="stFileUploader"] div:last-child { display: none !important; }
            .stCameraInput > div:first-child { display: none !important; }
            
            /* ALL BUTTONS GREEN */
            div.stButton > button {
                width: 100% !important;
                border-radius: 16px !important;
                padding: 18px 28px !important;
                font-size: 18px !important;
                font-weight: 700 !important;
                cursor: pointer !important;
                transition: all 0.3s ease !important;
                text-align: center !important;
                margin: 12px 0 !important;
                border: none !important;
                letter-spacing: 0.5px;
                background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%) !important;
                color: white !important;
                box-shadow: 0 6px 20px rgba(76, 175, 80, 0.4) !important;
            }
            
            div.stButton > button:hover {
                transform: translateY(-3px) !important;
                box-shadow: 0 10px 25px rgba(76, 175, 80, 0.5) !important;
                background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%) !important;
            }
            
            /* ANALYZE IMAGE BUTTON - EXTRA LARGE */
            div.stButton > button[kind="primary"] {
                font-size: 20px !important;
                padding: 20px 32px !important;
            }
            
            /* CLEAR IMAGE BUTTON - SAME GREEN */
            div.stButton > button:not([kind="primary"]) {
                font-size: 16px !important;
                padding: 16px 24px !important;
            }
            
            /* LANGUAGE BUTTONS - GREEN */
            .language-btn {
                background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%) !important;
                color: white !important;
                border: none !important;
                border-radius: 12px !important;
                padding: 12px 24px !important;
                font-size: 15px !important;
                font-weight: 600 !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 12px rgba(76, 175, 80, 0.3) !important;
                margin: 8px 4px !important;
            }
            
            .language-btn:hover {
                background: linear-gradient(135deg, #2E7D32 0%, #4CAF50 100%) !important;
                transform: translateY(-2px) !important;
                box-shadow: 0 6px 18px rgba(76, 175, 80, 0.4) !important;
            }
            
            /* HEADER STYLING */
            .page-header {
                text-align: center;
                margin-bottom: 2rem;
                padding: 0 1rem;
            }
            
            .page-title {
                color: #2e7d32;
                font-size: 2.5rem;
                font-weight: 800;
                margin-bottom: 0.5rem;
            }
            
            .page-subtitle {
                color: #6c757d;
                font-size: 1.1rem;
                font-weight: 500;
            }
        </style>
    """, unsafe_allow_html=True)

    # BEAUTIFUL PAGE HEADER
    st.markdown("""
        <div class='page-header'>
            <h1 class='page-title'> Disease Detection</h1>
            <p class='page-subtitle'>Upload rice leaf image for instant analysis</p>
        </div>
    """, unsafe_allow_html=True)

    # Image Upload - FIXED SESSION STATE MANAGEMENT
    if 'preview_image' not in st.session_state:
        st.session_state.preview_image = None
    if 'file_upload_key' not in st.session_state:
        st.session_state.file_upload_key = 0
    if 'camera_key' not in st.session_state:
        st.session_state.camera_key = 0

    # Use keys to force reset of file uploader and camera
    uploaded_file = st.file_uploader(" ", type=["jpg", "jpeg", "png"], key=f"file_upload_{st.session_state.file_upload_key}", label_visibility="collapsed")
    
    if uploaded_file:
        st.session_state.preview_image = uploaded_file

    if st.session_state.preview_image is None:
        camera_photo = st.camera_input(" ", key=f"camera_input_{st.session_state.camera_key}", label_visibility="collapsed")
        if camera_photo:
            st.session_state.preview_image = camera_photo

    # Image Preview
    if st.session_state.preview_image:
        try:
            image = Image.open(st.session_state.preview_image)
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            st.markdown(f"""
            <div class="upload-section">
                <img src="https://cdn-icons-png.flaticon.com/128/2659/2659360.png" width="60" style="margin-bottom: 15px;">
                <div class="upload-text">Image Ready for Analysis</div>
                <div class="upload-subtext">Your rice leaf image is loaded and ready</div>
                <img src="data:image/png;base64,{img_str}" class="preview-image" width="320">
            </div>
            """, unsafe_allow_html=True)

            # ACTION BUTTONS SECTION
            col1, col2 = st.columns(2)
            
            with col1:
                # Clear Button - GREEN
                if st.button("Clear Image", key="clear_btn", use_container_width=True):
                    st.session_state.preview_image = None
                    st.session_state.file_upload_key += 1
                    st.session_state.camera_key += 1
                    if 'detection_result' in st.session_state:
                        del st.session_state.detection_result
                    st.rerun()
            
            with col2:
                # Detect Button - GREEN
                if st.button("ANALYZE IMAGE", key="detect_btn", use_container_width=True, type="primary"):
                    if not st.session_state.preview_image:
                        st.error("Please upload an image or take a photo first.")
                    else:
                        with st.spinner("Analyzing image for diseases..."):
                            try:
                                image = Image.open(st.session_state.preview_image)
                                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                                    image.save(tmp_file, format="JPEG")
                                    tmp_file_path = tmp_file.name

                                client = init_client()
                                result = client.infer(tmp_file_path, model_id="palay-protector-y599v/1")

                                if result.get("predictions"):
                                    prediction = result["predictions"][0]
                                    disease = prediction["class"]
                                    confidence = prediction["confidence"] * 100
                                    normalized_name = normalize_disease_name(disease)

                                    if normalized_name in DISEASE_INFO:
                                        data = DISEASE_INFO[normalized_name]

                                        # Save to history (if not non-plant)
                                        if not data.get("is_non_plant", False):
                                            supabase.table("history").insert({
                                                "user_id": st.session_state.user_id,
                                                "result": normalized_name,
                                                "severity": data["severity"],
                                                "confidence": round(confidence, 2),
                                                "date_detected": datetime.now().isoformat()
                                            }).execute()

                                        # Store detection data for persistent display
                                        st.session_state.detection_result = {
                                            "normalized_name": normalized_name,
                                            "confidence": confidence,
                                            "data": data
                                        }

                                    else:
                                        st.warning("Unknown disease detected.")
                                else:
                                    st.error("No predictions returned from the model.")
                            except Exception as e:
                                st.error(f"Error during detection: {e}")
                
        except Exception as e:
            st.error("❌ Error loading image. Please upload a new one.")
            st.session_state.preview_image = None
            st.session_state.file_upload_key += 1
            st.session_state.camera_key += 1
            st.rerun()
    else:
        # DEFAULT UPLOAD SECTION - BEAUTIFUL DESIGN
        st.markdown("""
        <div class="upload-section">
            <img src="https://cdn-icons-png.flaticon.com/128/1829/1829589.png" width="80" style="margin-bottom: 20px;">
            <div class="upload-text">Upload Rice Leaf Image</div>
            <div class="upload-subtext">Choose a file or use your camera to capture a photo</div>
            <div style="margin-top: 20px; color: #888; font-size: 13px;">
                ⚡ Supports JPG, JPEG, PNG formats
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Display Detection Result
    if 'detection_result' in st.session_state and st.session_state.detection_result:
        result_data = st.session_state.detection_result
        normalized_name = result_data["normalized_name"]
        confidence = result_data["confidence"]
        data = result_data["data"]

        # Get translated content based on current language
        is_tagalog = st.session_state.result_lang == "tagalog"
        
        if is_tagalog:
            result_title = "Resulta ng Pagtuklas"
            severity_label = "Kalubhaan"
            about_label = "Tungkol sa sakit na ito:"
            description = data["tagalog"]["description"]
            severity_text = data["tagalog"]["severity"]
        else:
            result_title = "Detection Result"
            severity_label = "Severity"
            about_label = "About this disease:"
            description = data["description"]
            severity_text = data["severity"]

        # Display result card with CSS classes
        st.markdown(f"""
            <div class='result-card'>
                <h2 class='result-title'>{result_title}</h2>
                <h3 class='disease-name'>{normalized_name}</h3>
                <h4 class='confidence-score'>{confidence:.1f}% Confidence</h4>
                <div class='severity-badge' style='background-color:{data["severity_color"]}'>
                    {severity_label}: {severity_text}
                </div>
                <div class='confidence-bar'>
                    <div class='confidence-fill' style='width:{confidence}%'></div>
                </div>
                <div class='disease-info'>
                    <b>{about_label}</b><br>{description}
                </div>
        """, unsafe_allow_html=True)

        # Language toggle buttons - GREEN
        st.markdown("<div style='text-align: center; margin: 20px 0;'>", unsafe_allow_html=True)
        st.markdown("<p style='color: #666; margin-bottom: 10px; font-weight: 600;'>🌐 View in:</p>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Filipino", key="btn_tl", use_container_width=True):
                st.session_state.result_lang = "tagalog"
                st.rerun()
        with col3:
            if st.button("English", key="btn_en", use_container_width=True):
                st.session_state.result_lang = "english"
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

    # Bottom Navigation

    show_bottom_nav('detect')
