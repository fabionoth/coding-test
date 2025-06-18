import asyncio
import sys
import os
from weather_fetcher import fetch_all_weather
from data_transformer import normalize_responses
from file_writer import write_to_csv, write_to_json

CITIES = ["London", "New York", "Tokyo", "São Paulo", "Johannesburg"]

async def main():
    # Parse command-line arguments
    print_csv = "--csv" in sys.argv
    print_json = "--json" in sys.argv
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    csv_path = os.path.join(output_dir, "weather_data.csv")
    json_path = os.path.join(output_dir, "weather_data.json")

    raw_data = await fetch_all_weather(CITIES)
    transformed_data = normalize_responses(raw_data)
    write_to_csv(transformed_data, filename=csv_path)
    write_to_json(transformed_data, filename=json_path)

    if print_csv:
        with open(csv_path, "r", encoding="utf-8") as f:
            print("\n--- CSV Output ---")
            print(f.read())
    if print_json:
        with open(json_path, "r", encoding="utf-8") as f:
            print("\n--- JSON Output ---")
            print(f.read())

if __name__ == "__main__":
    asyncio.run(main())
