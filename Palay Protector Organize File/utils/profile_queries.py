# utils/profile_queries.py
from config import supabase

def get_user_profile_stats(user_id):
    try:
        # Get recent activity
        recent_activity = supabase.table("history").select(
            "result, date_detected"
        ).eq("user_id", user_id).order("date_detected", desc=True).limit(5).execute().data
        
        # Get user info
        user_info = supabase.table("users").select(
            "username, email, user_type, created_at"
        ).eq("id", user_id).execute().data
        
        return {
            "recent_activity": recent_activity,
            "user_info": user_info[0] if user_info else {}
        }
    except Exception as e:
        print(f"Error getting user profile stats: {e}")
        return {"recent_activity": [], "user_info": {}} 
