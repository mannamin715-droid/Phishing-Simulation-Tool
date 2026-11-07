
from flask import Flask, render_template, request, jsonify
from database import init_db, record_event, get_statistics, get_recent_events
app = Flask(__name__)

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulation")
def simulation():
    return render_template("simulation.html")


@app.route("/record-event", methods=["POST"])
def save_event():
    data = request.get_json(silent=True) or {}
    event_type = data.get("event_type")

    if event_type not in ("clicked", "reported"):
        return jsonify({"error": "Invalid event type"}), 400

    record_event(event_type)

    return jsonify({
        "success": True,
        "message": "Simulation event recorded"
    })


@app.route("/statistics")
def statistics():
    return jsonify(get_statistics())
@app.route("/history")
def history():
    return jsonify(get_recent_events())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


