import requests
from flask import Flask, request, jsonify

class WebRemote:
    app = Flask(__name__)
    display = None

    def __init__(self, display):
        self._display = display
        WebRemote.display = display

    @app.route('/api/set_text/<uuid>', methods=['GET', 'POST'])
    def set_text(uuid):
        content = request.json
        text = content['text']

        WebRemote.display.print_string(text)
        WebRemote.display.show()

        return jsonify({"uuid":uuid})

    def start(self):
        self.app.run(host= '0.0.0.0',debug=True)
