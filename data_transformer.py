from datetime import datetime

def normalize_openweather(data):
    if "error" in data:
        return {"city": data.get("city", ""), "source": "openweather", "error": data["error"]}
    return {
        "city": data.get("name", ""),
        "country": data.get("sys", {}).get("country", ""),
        "temp_c": data.get("main", {}).get("temp", None),
        "condition": data.get("weather", [{}])[0].get("description", ""),
        "humidity": data.get("main", {}).get("humidity", None),
        "wind_kph": round(data.get("wind", {}).get("speed", 0) * 3.6, 2) if data.get("wind", {}).get("speed") is not None else None,
        "source": "openweather"
    }

def normalize_weatherapi(data):
    if "error" in data:
        return {"city": data.get("city", ""), "source": "weatherapi", "error": data["error"]}
    return {
        "city": data.get("location", {}).get("name", ""),
        "country": data.get("location", {}).get("country", ""),
        "temp_c": data.get("current", {}).get("temp_c", None),
        "condition": data.get("current", {}).get("condition", {}).get("text", ""),
        "humidity": data.get("current", {}).get("humidity", None),
        "wind_kph": data.get("current", {}).get("wind_kph", None),
        "source": "weatherapi"
    }

def normalize_responses(response_list):
    normalized = []
    for data in response_list:
        if data.get("_source") == "openweather":
            normalized.append(normalize_openweather(data))
        elif data.get("_source") == "weatherapi":
            normalized.append(normalize_weatherapi(data))
        else:
            normalized.append({"error": "Unknown source", **data})
    return normalized
