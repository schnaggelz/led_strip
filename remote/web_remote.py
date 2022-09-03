import http.server as http
import os

import led

class LedRequestHandler(http.BaseHTTPRequestHandler):

    def __init__(self, display):
        self._display = display

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        html = '''
            <html>
            <body style="width:960px; margin: 20px auto;">
            <h1>Hallöle Miez und Bebes</h1>
            <p>Die Systemtemperatur ist {}</p>
            <p>LED <a href="/on">AN</a> <a href="/off">AUS</a></p>
            <div id="led-status"></div>
            <script>
                document.getElementById("led-status").innerHTML="{}";
            </script>
            </body>
            </html>
        '''
        temp = os.popen("vcgencmd measure_temp").read()
        self.do_HEAD()
        status = ''
        if self.path=='/':
            pass
        elif self.path=='/on':
            self._display.test_all_characters()
            status='LED ist AN'
        elif self.path=='/off':
            status='LED ist AUS'
        self.wfile.write(html.format(temp[5:], status).encode("utf-8"))

class WebRemote:

    def __init__(self, display, host_name, host_port=8080):
        self._display = display

        request_handler = LedRequestHandler(display)
        self._server = http.HTTPServer((host_name, host_port), LedRequestHandler)

    def start(self):
        try:
            self._server.serve_forever()

        except KeyboardInterrupt:
            self._server.server_close()
        
