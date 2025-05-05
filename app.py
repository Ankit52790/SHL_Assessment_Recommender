# app.py
from flask import Flask, request, jsonify, render_template
from recommender import Recommender

app = Flask(__name__)
engine = Recommender()

# Preload data & recommendations
engine.load_data()
engine.recommend_assessments()

@app.route("/", methods=["GET"])
def home():
    # A simple form to enter a user ID
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    user_id = request.form["user_id"]
    recs = engine.recommendations.get(user_id)
    if not recs:
        return jsonify({"error": "User not found"}), 404
    return jsonify({user_id: recs})

if __name__ == "__main__":
    app.run(debug=True)
