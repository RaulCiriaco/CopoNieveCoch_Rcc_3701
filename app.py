from flask import Flask, send_file, request
from koch import generate_snowflake
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("static/index.html")

@app.route("/koch")
def koch():
    depth = int(request.args.get("depth", 3))
    half = request.args.get("half", "false").lower() == "true"
    filename = "half.png" if half else "full.png"
    path = generate_snowflake(depth=depth, half=half, filename=filename)
    return send_file(path, mimetype='image/png')

if __name__ == "__main__":
    os.makedirs("static/images", exist_ok=True)
    app.run(debug=True)
