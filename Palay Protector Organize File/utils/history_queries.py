# utils/history_queries.py
from config import supabase

def get_user_detection_history(user_id, limit=None):
    try:
        query = supabase.table("history").select(
            "date_detected, result, severity, confidence"
        ).eq("user_id", user_id).order("date_detected", desc=True)
        
        if limit:
            query = query.limit(limit)
            
        res = query.execute()
        return res.data
    except Exception as e:
        print(f"Error getting user detection history: {e}")
        return []
