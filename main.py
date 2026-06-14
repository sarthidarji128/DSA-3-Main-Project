from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("index.html", "rb") as f:
            self.wfile.write(f.read())

server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Server running at http://localhost:8000")
server.serve_forever()
