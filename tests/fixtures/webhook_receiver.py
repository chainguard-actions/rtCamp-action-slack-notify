#!/usr/bin/env python3
"""Minimal local Slack-webhook receiver: saves each POST body to a file and replies 200 ok."""
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(sys.argv[1])
OUT = sys.argv[2]


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length)
        with open(OUT, "wb") as f:
            f.write(body)
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"ok")

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"alive")

    def log_message(self, fmt, *args):
        sys.stderr.write("receiver: " + (fmt % args) + "\n")


HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
