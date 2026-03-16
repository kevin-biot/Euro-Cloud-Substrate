#!/usr/bin/env python3
import argparse
import hashlib
from http.server import BaseHTTPRequestHandler, HTTPServer


STORE = {}


def etag(data: bytes) -> str:
    return '"' + hashlib.md5(data).hexdigest() + '"'


class Handler(BaseHTTPRequestHandler):
    def _key(self) -> str:
        return self.path

    def do_PUT(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length) if length else b""
        STORE[self._key()] = body
        self.send_response(200)
        self.send_header("ETag", etag(body))
        self.end_headers()

    def do_GET(self):
        key = self._key()
        if key not in STORE:
            self.send_response(404)
            self.end_headers()
            return
        body = STORE[key]
        self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("ETag", etag(body))
        self.end_headers()
        self.wfile.write(body)

    def do_HEAD(self):
        key = self._key()
        if key not in STORE:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("ETag", etag(STORE[key]))
        self.end_headers()

    def do_DELETE(self):
        key = self._key()
        existed = key in STORE
        if existed:
            del STORE[key]
        self.send_response(204 if existed else 404)
        self.end_headers()


def main() -> None:
    parser = argparse.ArgumentParser(description="Mock object backend for ECS runtime demo")
    parser.add_argument("--listen", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=19090)
    args = parser.parse_args()

    server = HTTPServer((args.listen, args.port), Handler)
    print(f"mock backend listening on {args.listen}:{args.port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
