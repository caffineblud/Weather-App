import tkinter as tk

from weather.api import get_weather
from weather.formatter import format_weather


def search_weather():
    city = city_entry.get()

    data = get_weather(city)

    result_label.config(text=format_weather(data))


root = tk.Tk()
root.title("Weather App")
root.geometry("450x300")

title = tk.Label(
    root,
    text="Weather App",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

search_btn = tk.Button(
    root,
    text="Get Weather",
    command=search_weather
)
search_btn.pack()

result_label = tk.Label(
    root,
    text="",
    justify="left",
    font=("Arial", 12)
)
result_label.pack(pady=20)

root.mainloop()