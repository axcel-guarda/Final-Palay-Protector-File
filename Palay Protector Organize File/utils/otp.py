
# utils/otp.py
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp(length=6):
    """Generate a random OTP"""
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def send_otp_email(email, otp):
    """Send OTP to email"""
    try:
        # Email configuration (palitan ng iyong SMTP details)
        sender_email = "palayprotector@gmail.com"
        sender_password = "lesp ipuj azui omzj"  # Use App Password for Gmail
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Your OTP Code"
        
        # Email body
        body = f"""
        <html>
        <body>
            <h2>OTP Verification</h2>
            <p>Your OTP code is: <strong>{otp}</strong></p>
            <p>This code will expire in 3 minutes.</p>
            <p>If you didn't request this, please ignore this email.</p>
        </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        # Send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        print(f"OTP sent to {email}: {otp}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return False