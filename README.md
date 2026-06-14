# 🌦️ Weather App v2.0

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Version](https://img.shields.io/badge/Version-2.0-success)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

A modern weather application built with Python that provides real-time weather information through both a **Command Line Interface (CLI)** and a **Graphical User Interface (GUI)**. The project follows a modular architecture, making it easy to maintain, extend, and contribute to.

---

## ✨ Features

### 🌍 Weather Information

* Real-time weather data
* Temperature in Celsius
* Humidity percentage
* Weather condition description
* City-based weather search

### 💻 CLI Version

* Fast and lightweight
* Simple terminal interface
* Easy to use

### 🖥️ GUI Version

* Built with Tkinter
* User-friendly interface
* Instant weather lookup
* Clean and responsive layout

### 🏗️ Developer-Friendly

* Modular architecture
* Environment variable support
* Easy API replacement
* GitHub-ready project structure

---

## 📸 Screenshots

### GUI Interface

```text id="q5z4dn"
[ Add your GUI screenshot here ]

screenshots/
└── gui.png
```

After adding screenshots:

```markdown id="5mrjvh"
![GUI Preview](screenshots/gui.png)
```

---

## 📂 Project Structure

```text id="e8gg9g"
weather-app/
│
├── weather/
│   ├── __init__.py
│   ├── api.py
│   ├── config.py
│   └── formatter.py
│
├── cli.py
├── gui.py
│
├── screenshots/
│   └── gui.png
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash id="g44b5o"
git clone https://github.com/caffineblud/weather-app.git
cd weather-app
```

### Create Virtual Environment

```bash id="on2g4t"
python -m venv venv
```

### Activate Environment

**Windows**

```bash id="q55vjv"
venv\Scripts\activate
```

**Linux/macOS**

```bash id="dbvfpg"
source venv/bin/activate
```

### Install Dependencies

```bash id="vgsbh7"
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file:

```env id="g8fkrv"
API_KEY=YOUR_API_KEY_HERE
```

Example `.env.example`:

```env id="l4k37n"
API_KEY=YOUR_API_KEY_HERE
```

---

## 🚀 Running the Application

### CLI Version

```bash id="gf4ig4"
python cli.py
```

### GUI Version

```bash id="igce9k"
python gui.py
```

---

## 🧠 Architecture

```text id="vbkhrm"
User
 │
 ▼
CLI / GUI
 │
 ▼
Formatter Layer
 │
 ▼
API Layer
 │
 ▼
OpenWeatherMap API
```

This separation ensures:

* Better maintainability
* Easier testing
* Faster feature additions
* Cleaner codebase

---

## 🛠️ Technologies Used

* Python
* Tkinter
* Requests
* Python Dotenv
* OpenWeatherMap API

---

## 📋 Requirements

```text id="m2xkdd"
requests
python-dotenv
```

---

## 🚧 Roadmap

### v2.0

* [x] CLI Weather Application
* [x] Tkinter GUI
* [x] API Integration
* [x] Modular Structure
* [x] Environment Variables

### v3.0

* [ ] Weather Icons
* [ ] Search History
* [ ] Auto Detect Location
* [ ] Theme Switching

### v4.0

* [ ] 5-Day Forecast
* [ ] Sunrise & Sunset Data
* [ ] Wind Speed Information
* [ ] Feels Like Temperature

### v5.0

* [ ] CustomTkinter UI
* [ ] Charts & Graphs
* [ ] Export Reports
* [ ] Weather Analytics Dashboard

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License.

---

## 👨‍💻 Author

**Yash Kumar Singh**

If you like this project, consider giving it a ⭐ on GitHub.
