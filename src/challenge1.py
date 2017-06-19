"""Simple HTTP Server Set up"""
import socketserver
import http.server


# ASSIGN PORT
PORT = 8000


# Create an request handler / listener
Handler = http.server.BaseHTTPRequestHandler

class Mo(http.server.BaseHTTPRequestHandler)


# Open the server on the selected port, and make it listen perpetually.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server running on port:", PORT)
    # print(dir(Handler))
    # print(Handler.do_GET)
    httpd.serve_forever()

