import requests
import multiprocessing as mp

from flask import Flask, request, jsonify
from werkzeug.serving import make_server

from led import Color

from .display_server import DisplayServer

class WebRemote:
    app = Flask(__name__)

    def __init__(self):
        self._server = None
        global display
        # display = DisplayServer(brightness=128)
        # display.start()

    @app.route('/api/set_text/<uuid>', methods=['GET', 'POST'])
    def set_text(uuid):
        
        content = request.json
        id = int(content['id'])
        text = content['text']

        fg_color_R = int(content['fg_color_R'])
        fg_color_G = int(content['fg_color_G'])
        fg_color_B = int(content['fg_color_B'])
        bg_color_R = int(content['bg_color_R'])
        bg_color_G = int(content['bg_color_G'])
        bg_color_B = int(content['bg_color_B'])

        print(text)

        if id == 1:
            global display
            #display.send(text.upper())
            # display.print_string(text.upper(), 0, 0,
            #     fg_color=Color(fg_color_R, fg_color_G, fg_color_B), 
            #     bg_color=Color(bg_color_R, bg_color_G, bg_color_B))

        return jsonify({"uuid":uuid})

    def start(self):
        if self._server is None:
            self._server = mp.Process(target=WebRemote.app.run, kwargs={'host':'0.0.0.0'})
            self._server.start()

    def stop(self):
        if self._server is not None:
            self._server.terminate()
            self._server.join()
            self._server = None
