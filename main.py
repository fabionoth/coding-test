import asyncio
from weather_fetcher import fetch_all_weather
from data_transformer import normalize_responses
from file_writer import write_to_csv, write_to_json

CITIES = ["London", "New York", "Tokyo", "São Paulo", "Johannesburg"]

async def main():
    # TODO: Fetch raw weather data for each city asynchronously
    raw_data = await fetch_all_weather(CITIES)

    # TODO: Normalize responses to a common format
    transformed_data = normalize_responses(raw_data)

    # TODO: Save data to CSV and JSON
    write_to_csv(transformed_data)
    write_to_json(transformed_data)

if __name__ == "__main__":
    asyncio.run(main())
