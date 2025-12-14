# utils/helpers.py
import random
import string
import smtplib
import re
from email.message import EmailMessage
from inference_sdk import InferenceHTTPClient
from config import INFERENCE_API_KEY, INFERENCE_API_URL

def generate_otp(length=6):
    return ''.join(random.choices(string.digits, k=length))

def send_otp_email(receiver_email, otp):
    try:
        msg = EmailMessage()
        msg['Subject'] = "Palay Protector - Your OTP Code"
        msg['From'] = "palayprotector@gmail.com"
        msg['To'] = receiver_email
        msg.set_content(f"Your OTP code is: {otp}\nValid for 5 minutes only.")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("palayprotector@gmail.com", "dfhzpiitlsgkptmg")
            server.send_message(msg)
        return True
    except Exception as e:
        print("Failed to send OTP:", e)
        return False

def init_client():
    return InferenceHTTPClient(
        api_url=INFERENCE_API_URL, 
        api_key=INFERENCE_API_KEY
    )

def is_valid_gmail(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    return re.match(pattern, email.strip()) is not None
