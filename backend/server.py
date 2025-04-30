from graphs import create_graph
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, origins="*")

@app.route('/submit', methods=['POST'])
def get_data():
    data = request.get_json()
    imageUrl = create_graph(data["stat"], data["limit"], data["ascending"])
    return jsonify({"image": imageUrl})

if __name__ == "__main__":
    app.run(debug=True)