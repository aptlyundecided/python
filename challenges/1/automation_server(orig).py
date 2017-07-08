"""Challenge 1 Server"""


# Dependencies
import http.server
import subprocess


# Create the HTTP Server
HTTPSERVER = http.server.HTTPServer


# Create a wicked sweet request handler class
class SweetHandler(http.server.BaseHTTPRequestHandler):
    """My HTTP Request Handler"""


    # set request headers
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()


    # set GET request handling
    def do_GET(self): #pylint: disable=C0103
        """Handle GET requests"""
        self._set_headers()
        filename = self.path.replace('/', '')
        if self.path == '/':
            print('INDEX.  This should handle serving html files.')
        else:
            print(filename + 'Route not found')
            print('Route: ' + self.path)


    # set POST request handling
    def do_POST(self): #pylint: disable=C0103
        """Handle POST requests"""
        self._set_headers()
        filename = self.path.replace('/', '')
        if self.path == '/hi_temp_message':
            return subprocess.run(['python', filename + '.py'], shell=True)
        else:
            print(filename + 'Route not found')
            print('Route: ' + self.path)


    # call to header setting function, via expected do_HEAD method.
    def do_HEAD(self): #pylint: disable=C0103
        """Handle HEAD ... requests?"""
        self._set_headers()


def run(server_class=HTTPSERVER, handler_class=SweetHandler, port=8000):
    """Run my HTTP Server"""


    # set the local address of the server
    server_address = ('', port)


    # here we are instantiating an object, prototyped as a handler class.
    httpd = server_class(server_address, handler_class)


    # show that server is attempting to run
    print('Automation server running on port 8000')


    # tell server to run indefinitely
    httpd.serve_forever()


# Run the server.
run()
