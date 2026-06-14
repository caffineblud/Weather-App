# 🌦️ Weather App v1.0

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Version](https://img.shields.io/badge/Version-1.0-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Requests](https://img.shields.io/badge/Requests-Library-orange)

A simple and beginner-friendly weather application built with Python. This project fetches real-time weather data using the OpenWeatherMap API and displays useful weather information directly in the terminal.

---

## ✨ Features

* 🌡️ Current temperature
* 💧 Humidity information
* ☁️ Weather conditions
* 🔍 Search weather by city name
* 🛠️ Clean and modular code structure
* 📦 Easy to extend for future GUI versions

---

## 📂 Project Structure

```text
weather-app/
│
├── weather/
│   ├── __init__.py
│   ├── api.py
│   ├── config.py
│   └── formatter.py
│
├── cli.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/caffineblud/weather-app.git
cd weather-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Setup

Create a `.env` file in the project root:

```env
API_KEY=YOUR_API_KEY_HERE
```

Get a free API key from OpenWeatherMap.

---

## ▶️ Running the Application

```bash
python cli.py
```

Example:

```text
Enter city: Delhi

Weather Report
------------------------------
City: Delhi
Temperature: 35°C
Humidity: 60%
Condition: Clear Sky
```

---

## 🧰 Technologies Used

* Python
* Requests
* OpenWeatherMap API
* Python Dotenv

---

## 📈 Roadmap

### Version 1.0

* [x] Terminal Interface
* [x] Real-Time Weather Data
* [x] Error Handling
* [x] Modular Structure

### Version 2.0

* [ ] Tkinter GUI
* [ ] Weather Icons
* [ ] Search History

### Version 3.0

* [ ] 5-Day Forecast
* [ ] Dark Mode
* [ ] Export Weather Report

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the project and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## Author:
***Yash Kumar Singh***

### ⭐ If you found this project useful, consider giving it a star!
