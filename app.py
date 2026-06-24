
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

coffees = [
    {"id": 1, "name": "Ethiopian Yirgacheffe", "votes": 125},
    {"id": 2, "name": "Sumatra Mandheling", "votes": 150},
    {"id": 3, "name": "Cold Brew Nitro", "votes": 98},
    {"id": 4, "name": "Vanilla Latte", "votes": 125},
    {"id": 5, "name": "Mexican Chiapas", "votes": 120}
]

@app.route("/")
def home():
    return render_template("index.html", coffees=coffees)

@app.route("/vote/<int:coffee_id>", methods=["POST"])
def vote(coffee_id):
    for coffee in coffees:
        if coffee["id"] == coffee_id:
            coffee["votes"] += 1
            return jsonify({"votes": coffee["votes"]})
    return jsonify({"error":"Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
