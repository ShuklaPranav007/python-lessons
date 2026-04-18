import python_weather
import asyncio

async def getweather():
    # Declare the client
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # Fetch weather for a city
        weather = await client.get('New York')
        print(f"Current temp: {weather.temperature}°C")

asyncio.run(getweather())