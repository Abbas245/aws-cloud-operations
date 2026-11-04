from http.server import BaseHTTPRequestHandler, HTTPServer


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Private App Server is RUNNING!")


server = HTTPServer(("0.0.0.0", 8080), AppHandler)
print("Application listening on port 8080", flush=True)
server.serve_forever()
