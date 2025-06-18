# TODO: Import aiohttp, asyncio, and config

import aiohttp
import asyncio
from config import OPENWEATHER_API_KEY, WEATHERAPI_API_KEY

async def fetch_openweather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                data["_source"] = "openweather"
                return data
            else:
                return {"city": city, "_source": "openweather", "error": f"HTTP {response.status}"}

async def fetch_weatherapi(city):
    url = f"https://api.weatherapi.com/v1/current.json?key={WEATHERAPI_API_KEY}&q={city}&aqi=no"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                data["_source"] = "weatherapi"
                return data
            else:
                return {"city": city, "_source": "weatherapi", "error": f"HTTP {response.status}"}

async def fetch_all_weather(cities):
    tasks = []
    for city in cities:
        tasks.append(fetch_openweather(city))
        tasks.append(fetch_weatherapi(city))
    results = await asyncio.gather(*tasks)
    return results
