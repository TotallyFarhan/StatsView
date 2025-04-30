from graphs import create_graph
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/submit', methods=['POST'])
def get_data():
    data = request.get_json()
    imageUrl = create_graph(data["stat"], data["limit"], data["ascending"])
    return jsonify({"image": imageUrl})

@app.route('/graphs/<path:filename>')
def get_graph_image(filename):
    return send_from_directory(os.path.join('graphs'), filename)

if __name__ == "__main__":
    app.run(debug=True)