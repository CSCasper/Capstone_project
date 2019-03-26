from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8080


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        print("Post Request!")


httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
print('Serving port: ', PORT)
httpd.serve_forever()

