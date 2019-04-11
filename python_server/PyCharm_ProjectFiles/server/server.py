from http.server import HTTPServer, BaseHTTPRequestHandler
import table.tableFactory as tbFactory
from io import BytesIO
import codecs
import datetime


PORT = 8080
cssHeader = '''
<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
</style>
</head>
<body>
'''
htmlHeader = '''
<html>
    <body><h1>Trash Sensing Data</h1>
'''
htmlFooter = '''
    </body>
</html>
'''


table = tbFactory.Table()
table.add_can(trash_can=tbFactory.TrashCan(1, 0))


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html_table = tbFactory.htmlTableHeader + table.get_table_block() + tbFactory.htmlTableFooter
        html = cssHeader + htmlHeader + html_table + htmlFooter

        self.wfile.write(html.encode())

    def do_POST(self):

        # Process POST data
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()

        try:

            # Tokenize data
            data = str(body).split(' ')

            # Remove any unneeded characters
            i = 0
            for prop in data:
                prop = prop.replace('\\', '')
                prop = prop.replace('b', '')
                prop = prop.replace('\'', '')
                data[i] = prop
                i = i + 1

            # Update table model with new data

            id = int(data[0]);
            level = int(data[1]);

            table.trash_cans[id].trash_level = level
            table.trash_cans[id].time = datetime.datetime.now()

            if level >= 64:
                table.trash_cans[id].trash_state = "Empty"
            elif level >= 53:
                table.trash_cans[id].trash_state = "Quarter Full"
            elif level >= 42:
                table.trash_cans[id].trash_state = "Half Full"
            elif level >= 31:
                table.trash_cans[id].trash_state = "Three Quarters Full"
            elif level < 31:
                table.trash_cans[id].trash_state = "Full"


        except:
            print("Something went wrong when parsing!")

        response = BytesIO()
        response.write(b'This is a POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('', PORT), Handler)
print('Serving port: ', PORT)
httpd.serve_forever()
