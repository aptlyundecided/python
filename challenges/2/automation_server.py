"""Challenge 2 Server"""

# Dependencies
import http.server
import subprocess
import json

# Create the HTTP Server
HTTPSERVER = http.server.HTTPServer

# Create a request handler class
class SweetHandler(http.server.BaseHTTPRequestHandler):
    """My HTTP Request Handler"""

    # set request headers
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.data_string = self.rfile.read(int(self.headers['Content-Length'])) # pylint: disable=W0201
        self.end_headers()

    # POST request handling
    def do_POST(self): #pylint: disable=C0103
        """Handle POST requests"""

        #First run set headers.  The client will fault if no response is sent!
        self._set_headers()

        # Path handling, for executing .py files.
        filename = self.path.replace('/', '')

        # DO tasks.  THESE WILL BE IN BROKEN UP INTO MODULES.
        if self.path == '/hi_temp_message':
            return subprocess.run(['python', filename + '.py'], shell=True)

        elif self.path == '/rh_measurements':
            # parse data from JSON to a dictionary
            data = json.loads(self.data_string)

            # Roll that beautiful bean footage.
            print(data['rh_measurements'])

        else:
            print(filename + 'Route not found')
            print('Route: ' + self.path)

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
