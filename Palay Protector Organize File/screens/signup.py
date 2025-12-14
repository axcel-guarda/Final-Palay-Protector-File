# screens/signup.py
import streamlit as st
import hashlib
import time
from config import supabase, ADMIN_SECRET_KEY, AGRI_SECRET_KEY
from components.header import show_header
from utils.helpers import is_valid_gmail

def show_signup():
    show_header()
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown("### Create New Account")

    # BASIC INFO
    username = st.text_input("Username *", key="signup_username", placeholder="Choose a username")
    email = st.text_input("Email *", key="signup_email", placeholder="your.email@gmail.com")
    phone = st.text_input("Phone Number *", key="signup_phone", placeholder="+63 XXX XXX XXXX")
    password = st.text_input("Password *", type="password", key="signup_password", placeholder="Create a strong password")
    confirm_password = st.text_input("Confirm Password *", type="password", key="signup_confirm_password", placeholder="Re-enter your password")

    # LOCATION INFO
    PROVINCES = [
        "Abra", "Agusan del Norte", "Agusan del Sur", "Aklan", "Albay", "Antique", "Apayao", "Aurora",
        "Basilan", "Bataan", "Batanes", "Batangas", "Benguet", "Biliran", "Bohol", "Bukidnon", "Bulacan",
        "Cagayan", "Camarines Norte", "Camarines Sur", "Cebu", "Davao del Sur", "Iloilo", "Laguna",
        "Pampanga", "Quezon", "Sorsogon", "Zambales", "Metro Manila"
    ]

    SORSOGON_MUNICIPALITIES = [
        "Barcelona", "Bulan", "Bulusan", "Casiguran", "Castilla", "Donsol", "Gubat",
        "Irosin", "Juban", "Magallanes", "Matnog", "Pilar", "Prieto Diaz", "Santa Magdalena", "Sorsogon City"
    ]

    BULAN_BARANGAYS = [
        "A. Bonifacio (Tinurilan)", "Abad Santos (Kambal)", "Aguinaldo (Lipata Dako)",
        "Antipolo", "Aquino (Imelda)", "Bical", "Beguin", "Bonga", "Butag",
        "Cadandanan", "Calomagon", "Calpi", "Cocok-Cabitan", "Daganas", "Danao",
        "Dolos", "E. Quirino (Pinangomhan)", "Fabrica", "G. Del Pilar (Tanga)", "Gate",
        "Inararan", "J. Gerona (Biton)", "J.P. Laurel (Pon-od)", "Jamorawon", "Libertad (Calle Putol)",
        "Lajong", "Magsaysay (Bongog)", "Managa-naga", "Marinab", "Nasuje", "Montecalvario",
        "N. Roque (Calayugan)", "Namo", "Obrero", "Osmeña (Lipata Saday)", "Otavi",
        "Padre Diaz", "Palale", "Quezon (Cabarawan)", "R. Gerona (Butag)", "Recto", "Roxas (Busay)",
        "Sagrada", "San Francisco (Polot)", "San Isidro (Cabugaan)", "San Juan Bag-o", "San Juan Daan",
        "San Rafael (Togbongon)", "San Ramon", "San Vicente", "Santa Remedios", "Santa Teresita (Trece)",
        "Sigad", "Somagongsong", "Tarhan", "Taromata", "Zone 1 (Ilawod)", "Zone 2 (Sabang)",
        "Zone 3 (Central)", "Zone 4 (CBD)", "Zone 5 (Canipaan)", "Zone 6 (Baybay)", "Zone 7 (Iraya)",
        "Zone 8 (Loyo)"
    ]

    province = st.selectbox("Province *", ["-- Select Province --"] + PROVINCES)
    if province == "Sorsogon":
        municipality = st.selectbox("Municipality / City *", ["-- Select Municipality --"] + SORSOGON_MUNICIPALITIES)
    else:
        municipality = st.selectbox("Municipality / City *", ["-- Select Province First --"], disabled=True)

    if province == "Sorsogon" and municipality == "Bulan":
        barangay = st.selectbox("Barangay *", ["-- Select Barangay --"] + BULAN_BARANGAYS)
    elif province == "Sorsogon":
        barangay = st.text_input("Barangay *", placeholder="Enter your barangay (list unavailable)")
    else:
        barangay = st.text_input("Barangay *", placeholder="Enter your barangay")

    street = st.text_input("Street / Purok (Optional)", placeholder="e.g., Purok 1, Main Street, etc.")
    st.markdown('</div>', unsafe_allow_html=True)

    # ROLE SETTINGS
    st.markdown("---")
    show_admin_key = st.checkbox("🔽 Show advanced setup (Admin / Agriculturist)")
    
    role_option = "Farmer"
    admin_key = ""
    agri_key = ""

    if show_admin_key:
        role_option = st.radio("Select Role to Register As:", ["Admin", "Agriculturist"], horizontal=True)
        if role_option == "Admin":
            admin_key = st.text_input(" Admin Access Key", type="password")
        elif role_option == "Agriculturist":
            agri_key = st.text_input(" Agriculturist Access Key", type="password")

    st.markdown("---")

    # ACCOUNT CREATION LOGIC
    if st.button("✅ Create Account", use_container_width=True, type="primary"):
        if not username.strip():
            st.error("❌ Please enter your Username.")
        elif not email.strip() or not is_valid_gmail(email):
            st.error("❌ Please enter a valid Gmail address (must end with @gmail.com).")
        elif not phone.strip():
            st.error("❌ Please enter your Phone Number.")
        elif not password or not confirm_password:
            st.error("❌ Please enter and confirm your Password.")
        elif password != confirm_password:
            st.error("❌ Passwords do not match.")
        elif len(password) < 6:
            st.error("❌ Password must be at least 6 characters long.")
        elif province == "-- Select Province --":
            st.error("❌ Please select a Province.")
        elif not municipality.strip():
            st.error("❌ Please enter your Municipality or City.")
        else:
            try:
                check_username = supabase.table("users").select("*").eq("username", username).execute()
                check_email = supabase.table("users").select("*").eq("email", email).execute()

                if check_username.data:
                    st.warning("⚠️ Username already exists. Please choose another.")
                elif check_email.data:
                    st.warning("⚠️ Email already registered. Try logging in instead.")
                else:
                    if role_option == "Admin":
                        if admin_key.strip() == ADMIN_SECRET_KEY:
                            user_type = "admin"
                        else:
                            st.error("❌ Invalid Admin Access Key.")
                            return
                    elif role_option == "Agriculturist":
                        if agri_key.strip() == AGRI_SECRET_KEY:
                            user_type = "agriculturist"
                        else:
                            st.error("❌ Invalid Agriculturist Access Key.")
                            return
                    else:
                        user_type = "farmer"

                    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
                    full_address = f"{street}, {barangay}" if street else barangay

                    data = {
                        "username": username,
                        "email": email.lower().strip(),
                        "phone": phone,
                        "password": hashed_pw,
                        "province": province,
                        "municipality": municipality,
                        "barangay": full_address,
                        "user_type": user_type,
                    }

                    supabase.table("users").insert(data).execute()
                    st.success(f"🎉 {user_type.capitalize()} account created successfully!")
                    st.balloons()

                    time.sleep(2)
                    st.session_state.page = "login"
                    st.rerun()

            except Exception as e:
                st.error(f"❌ Database error: {e}")

    if st.button("← Back to Login", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
