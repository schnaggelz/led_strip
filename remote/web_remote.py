import requests
from flask import Flask, request, jsonify

from led import Color
from led import LedDisplay

class WebRemote:
    app = Flask(__name__)

    def __init__(self):
        global display 
        display = LedDisplay()
        display.init()
        display.set_brightness(128)

    @app.route('/api/set_text/<uuid>', methods=['GET', 'POST'])
    def set_text(uuid):
        global display

        content = request.json
        id = int(content['id'])
        text = content['text']

        fg_color_R = int(content['fg_color_R'])
        fg_color_G = int(content['fg_color_G'])
        fg_color_B = int(content['fg_color_B'])
        bg_color_R = int(content['bg_color_R'])
        bg_color_G = int(content['bg_color_G'])
        bg_color_B = int(content['bg_color_B'])

        if id == 1:
            display.print_string(text.upper(), 0, 0,
                fg_color=Color(fg_color_R, fg_color_G, fg_color_B), 
                bg_color=Color(bg_color_R, bg_color_G, bg_color_B))

            display.show()

        return jsonify({"uuid":uuid})

    def start(self):
        self.app.run(host= '0.0.0.0', debug=True)
