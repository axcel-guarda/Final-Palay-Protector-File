# utils/database.py
from config import supabase
from datetime import datetime

def get_user_history(user_id):
    try:
        res = supabase.table("history") \
            .select("date_detected, result, severity, confidence") \
            .eq("user_id", user_id) \
            .order("date_detected", desc=True) \
            .execute()
        return res.data
    except Exception as e:
        print(f"Database error: {e}")
        return []

def save_detection(user_id, result, severity, confidence):
    try:
        supabase.table("history").insert({
            "user_id": user_id,
            "result": result,
            "severity": severity,
            "confidence": confidence,
            "date_detected": datetime.now().isoformat()
        }).execute()
        return True
    except Exception as e:
        print(f"Error saving detection: {e}")
        return False

def get_user_stats(user_id):
    try:
        res = supabase.table("history").select("result").eq("user_id", user_id).execute()
        data = res.data
        total_scans = len(data)
        healthy_count = sum(1 for d in data if "Healthy" in d["result"])
        detected_count = total_scans - healthy_count
        accuracy_rate = (healthy_count / total_scans * 100) if total_scans > 0 else 0
        
        return {
            "total_scans": total_scans,
            "healthy_count": healthy_count,
            "detected_count": detected_count,
            "accuracy_rate": accuracy_rate
        }
    except Exception as e:
        print(f"Error getting user stats: {e}")
        return {"total_scans": 0, "healthy_count": 0, "detected_count": 0, "accuracy_rate": 0}
