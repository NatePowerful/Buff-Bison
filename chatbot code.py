from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_knowledge_base():
    try:
        with open('knowledge_trial.json', "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    knowledge_base = load_knowledge_base()

    # Placeholder for a more sophisticated response mechanism
    response_message = "I'm not sure how to respond to that."
    for item in knowledge_base.get("questions", []):
        if user_message.lower() in item["question"].lower():
            response_message = item["answer"]
            break

    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_knowledge_base():
    try:
        with open('knowledge_trial.json', "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    knowledge_base = load_knowledge_base()

    # Placeholder for a more sophisticated response mechanism
    response_message = "I'm not sure how to respond to that."
    for item in knowledge_base.get("questions", []):
        if user_message.lower() in item["question"].lower():
            response_message = item["answer"]
            break

    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_knowledge_base():
    try:
        with open('knowledge_trial.json', "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    knowledge_base = load_knowledge_base()

    # Placeholder for a more sophisticated response mechanism
    response_message = "I'm not sure how to respond to that."
    for item in knowledge_base.get("questions", []):
        if user_message.lower() in item["question"].lower():
            response_message = item["answer"]
            break

    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def load_knowledge_base():
    try:
        with open('knowledge_trial.json', "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"questions": []}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    knowledge_base = load_knowledge_base()

    # Placeholder for a more sophisticated response mechanism
    response_message = "I'm not sure how to respond to that."
    for item in knowledge_base.get("questions", []):
        if user_message.lower() in item["question"].lower():
            response_message = item["answer"]
            break

    return jsonify({"message": response_message})

if __name__ == '__main__':
    app.run(debug=True)
