import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

async def getWeather(city, apiKey):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?q={city}"
        f"&appid={apiKey}&units=metric"
    )

    try:
        request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urlopen(request) as response:
            data = json.load(response)

        return (
            f"<h3>{data['name']}</h3>"
            f"<p>Temperature: {data['main']['temp']} °C</p>"
            f"<p>Weather: {data['weather'][0]['description']}</p>"
            f"<p>Humidity: {data['main']['humidity']}%</p>"
        )
    except (HTTPError, URLError, KeyError):
        return "City not found!"
