from flask import Flask, jsonify
import random

app = Flask(__name__)

BUZZWORDS = [
    "unlocking synergistic adjacencies",
    "driving operational leverage",
    "monetizing data exhaust",
    "accelerating digital transformation",
    "capturing whitespace opportunities",
    "enhancing go-to-market alignment",
    "optimizing capital efficiency",
    "expanding recurring revenue base",
    "streamlining organizational design",
    "realizing integration synergies"
]

@app.route("/")
def index():
    phrase = random.choice(BUZZWORDS)
    return jsonify({"message": f"We’re {phrase} to maximize stakeholder value."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)