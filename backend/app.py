from flask import Flask, jsonify, request
from flask_cors import CORS
import config
import aiapi

app= Flask(__name__)
app.config.from_object(config.config['development'])
CORS(app)
@app.route("/", methods= ['POST', 'GET'])
def home():
    if request.method == 'POST':
        prompt = request.get_json()['message']
        res={
            'sender': "Doc",
            'message': ""
        }
        res['message']= aiapi.generateChatResponse(prompt)
        return jsonify(res),200
    
    #python -m flask --app .\app.py run