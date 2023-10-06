# Python Server (server.py)

from flask import Flask, request, jsonify, render_template
import subprocess
import random

app = Flask(__name__)

prompts = [
    "watch",
    "tiger",
    "car",
    "salt",
    "umbrella",
    "candle",
    "pizza",
    "guitar",
    "ocean",
    "moon",
    "shoe",
    "bicycle",
    "book",
    "tree",
    "coffee",
    "key",
    "flower",
    "hat",
    "globe",
    "camera",
    "lamp",
    "apple",
    "chair",
    "pen",
    "phone",
    "cloud",
    "dog",
    "cat",
    "door",
    "window",
    # Add more items as needed
]
@app.route('/generate_prompt')
def generate_prompt():
    # Choose a random prompt from the list
    random_prompt = random.choice(prompts)
    return jsonify({"prompt": random_prompt})

@app.route('/', methods=['POST'])
def run_script():
    try:
        subprocess.Popen(['python', 'your_script.py'])  # Replace 'your_script.py' with your script's path
    except Exception as e:
        print (e)
    
@app.route('/', methods=["GET"])
def index():
    return render_template('./index.html')  # Replace 'your_html_file.html' with the actual filename

if __name__ == '__main__':
    app.run(debug=True)
