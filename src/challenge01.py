"""FUCK"""
# import socketserver
import http.server
# import urlparse
# import json
import subprocess

HTTPSERVER = http.server.HTTPServer
class SweetHandler(http.server.BaseHTTPRequestHandler):
    """My HTTP Request Handler"""
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self): #pylint: disable=C0103
        """Handle GET requests"""
        self._set_headers()
        filename = self.path.replace('/', '')
        if self.path == '/':
            print('INDEX.  This should handle serving html files.')
        else:
            print(filename + 'Route not found')
            print('Route: ' + self.path)

    def do_POST(self): #pylint: disable=C0103
        """Handle POST requests"""
        self._set_headers()
        filename = self.path.replace('/', '')
        if self.path == '/hi_temp_message':
            return subprocess.run(['python', filename + '.py'], shell=True)
        else:
            print(filename + 'Route not found')
            print('Route: ' + self.path)

    def do_HEAD(self): #pylint: disable=C0103
        """Handle HEAD ... requests?"""
        self._set_headers()

def run(server_class=HTTPSERVER, handler_class=SweetHandler, port=8000):
    """Run my HTTP Server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

# Run the server.
run()
