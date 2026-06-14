def format_weather(data):
    if not data:
        return "City not found"

    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    return (
        f"City: {city}\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Condition: {condition.title()}"
    )