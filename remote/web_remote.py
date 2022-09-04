import requests
from flask import Flask, request, jsonify

class WebRemote:
    app = Flask(__name__)
    display = None

    def __init__(self, display):
        self.display = display

    @app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
    def add_message(uuid):
        content = request.json
        print(content['text'])
        return jsonify({"uuid":uuid})

    def start(self):
        self.app.run(host= '0.0.0.0',debug=True)
