# config.py
from supabase import create_client
import os

# Supabase Configuration
SUPABASE_URL = "https://sgaicxkbbbgyblfiudum.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNnYWljeGtiYmJneWJsZml1ZHVtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI1ODgyNzAsImV4cCI6MjA3ODE2NDI3MH0.yoHhNjsxPq2equ6-2ZKBW2KmXmvNSKWhD4JlB0TeNHM"

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Application Secrets
ADMIN_SECRET_KEY = "palay_secret_2025"
AGRI_SECRET_KEY = "agri_secret_2025"

# API Keys
INFERENCE_API_KEY = "8U0LHhVH4qxKTqcd4KO9"
INFERENCE_API_URL = "https://serverless.roboflow.com"

# Email Configuration
EMAIL_SENDER = "palayprotector@gmail.com"
EMAIL_PASSWORD = "lesp ipuj azui omzj"
