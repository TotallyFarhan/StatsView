from graphs import create_graph
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

# Initializes flask server
app = Flask(__name__)
# Allows any type of data to be sent through requests
CORS(app, resources={r"/*": {"origins": "*"}})

# Function for the POST request received from the frontend form submission with the stat, limit and whether they want to see the graph in ascending or descending order
@app.route('/submit', methods=['POST'])
def get_data():
    data = request.get_json() # Retrieves the form data from the JSON object sent from the frontend
    imageBuffer = create_graph(data["stat"], data["limit"], data["ascending"]) # Sends the form data to the create_graph function to create a bar graph and save the image path to the imageUrl variable
    return send_file(imageBuffer, mimetype='image/png') # Sends the imageUrl path back in a JSON object

# Run the flask app
if __name__ == "__main__":
    app.run(debug=True)