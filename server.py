
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from app import greet


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        name = parse_qs(urlparse(self.path).query).get("name", ["world"])[0]
        body = greet(name).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
