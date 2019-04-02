from http.server import HTTPServer, BaseHTTPRequestHandler
import codecs
from io import BytesIO

PORT = 8080


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        file = codecs.open("index.html", 'r')
        html = file.read()

        self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is a POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('', PORT), Handler)
print('Serving port: ', PORT)
httpd.serve_forever()
