# utils/admin_queries.py
from config import supabase

def get_admin_stats():
    try:
        total_farmers = len(supabase.table("users").select("*").eq("user_type", "farmer").execute().data)
        total_admins = len(supabase.table("users").select("*").eq("user_type", "admin").execute().data)
        total_detections = len(supabase.table("history").select("*").execute().data)
        
        return {
            "total_farmers": total_farmers,
            "total_admins": total_admins,
            "total_detections": total_detections
        }
    except Exception as e:
        print(f"Error getting admin stats: {e}")
        return {"total_farmers": 0, "total_admins": 0, "total_detections": 0}

def get_all_users():
    try:
        users_data = supabase.table("users").select(
            "id, username, email, phone, user_type, province, municipality, barangay, created_at"
        ).order("created_at", desc=True).execute().data
        return users_data
    except Exception as e:
        print(f"Error getting all users: {e}")
        return []

def get_detection_history(limit=50):
    try:
        history_data = supabase.table("history").select(
            "id, user_id, result, date_detected"
        ).order("date_detected", desc=True).limit(limit).execute().data
        return history_data
    except Exception as e:
        print(f"Error getting detection history: {e}")
        return []
