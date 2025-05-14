from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

number_to_guess = random.randint(1, 100)

@app.route("/start", methods=["GET"])
def start_game():
    global number_to_guess
    number_to_guess = random.randint(1, 100)
    return jsonify({"message": "New game started. Guess a number between 1 and 100!"})

@app.route("/guess", methods=["POST"])
def guess_number():
    data = request.get_json()
    guess = data.get("guess")
    if not guess:
        return jsonify({"result": "Please enter a number."})
    if guess < number_to_guess:
        return jsonify({"result": "Too low!"})
    elif guess > number_to_guess:
        return jsonify({"result": "Too high!"})
    else:
        return jsonify({"result": f"Correct! The number was {number_to_guess} 🎉"})

if __name__ == "__main__":
    app.run(debug=True)
