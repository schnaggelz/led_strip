import requests
import multiprocessing as mp

from flask import Flask, request, jsonify
from werkzeug.serving import make_server

from .display_server import DisplayServer

class WebRemote:
    app = Flask(__name__)

    def __init__(self):
        self._server = None
        self._display = DisplayServer(brightness=128)

        global display
        display = self._display

    @app.route('/api/set_text/<uuid>', methods=['GET', 'POST'])
    def set_text(uuid):
        
        content = request.json
        index = int(content['id']) - 1
        text = content['text']

        fg_color_R = int(content['fg_color_R'])
        fg_color_G = int(content['fg_color_G'])
        fg_color_B = int(content['fg_color_B'])
        bg_color_R = int(content['bg_color_R'])
        bg_color_G = int(content['bg_color_G'])
        bg_color_B = int(content['bg_color_B'])

        print("Printing '{}' to display at index {}".format(text, index))

        global display
        display.send(index, text.upper(),
            fg_color=(fg_color_R, fg_color_G, fg_color_B), 
            bg_color=(bg_color_R, bg_color_G, bg_color_B))

        return jsonify({"uuid":uuid})

    def start(self):
        if self._server is None:
            self._server = mp.Process(target=WebRemote.app.run, kwargs={'host':'0.0.0.0'})
            self._server.start()
        self._display.start()

    def stop(self):
        if self._server is not None:
            self._server.terminate()
            self._server.join()
            self._server = None
        self._display.stop()
