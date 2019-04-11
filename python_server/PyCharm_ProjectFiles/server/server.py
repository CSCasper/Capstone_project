from http.server import HTTPServer, BaseHTTPRequestHandler
import table.tableFactory as tbFactory
from io import BytesIO
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

# Create trash table configured with three TrashCans
table = tbFactory.Table()
table.add_can(trash_can=tbFactory.TrashCan(1, 0))


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Build html page and send it to the client
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
            trash_id = int(data[0]);
            trash_level = int(data[1]);

            table.trash_cans[trash_id].trash_level = trash_level
            table.trash_cans[trash_id].time = datetime.datetime.now()
            table.trash_cans[trash_id].update_trash_state()

        except:
            print("Something went wrong when parsing!")

        response = BytesIO()
        response.write(b'This is a POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


# Server startup
httpd = HTTPServer(('', PORT), Handler)
print('Serving port: ', PORT)
httpd.serve_forever()
