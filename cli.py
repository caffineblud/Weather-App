from weather.api import get_weather
from weather.formatter import format_weather


def main():
    city = input("Enter city: ")

    data = get_weather(city)

    print("\nWeather Report")
    print("-" * 30)
    print(format_weather(data))


if __name__ == "__main__":
    main()