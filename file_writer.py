import os
import csv
import json

def write_to_csv(data, filename="weather_data.csv"):
    if not data:
        print("No data to write to CSV.")
        return
    keys = data[0].keys()
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Data written to {filename}")

def write_to_json(data, filename="weather_data.json"):
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Data written to {filename}")
