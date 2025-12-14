from datetime import datetime, timedelta

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
