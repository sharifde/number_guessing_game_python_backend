# 🎯 Number Guessing Game

This is a simple Number Guessing Game implemented in two versions:

- 🖥️ **Web Version** using Flask (API-based)
- 🕹️ **Console Version** using pure Python

The game generates a random number between 1 and 100. The user keeps guessing until the correct number is guessed. Each guess receives feedback whether it's too high or too low.

---

## 🚀 Web Version (Flask API)

### 📂 Structure

- `app.py`: Flask API that handles the game logic
- Supports CORS for frontend integration

### 📦 Requirements

- Python 3.x
- Flask
- flask-cors

Install dependencies:

```bash
pip install flask flask-cors
