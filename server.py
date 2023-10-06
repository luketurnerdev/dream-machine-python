# Python Server (server.py)

from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

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
