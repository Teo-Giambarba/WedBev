from webserver import MyWebServer
from http.server import SimpleHTTPRequestHandler
import os 

PORT = int(os.getenv("PORT", 3001))

class ManuseioHttpRequest(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content_Type", "text/html, charset=UTF-8")
            self.end_headers()
            self.wfile.write("<p>Olá Mundo</p>".encode())
        else:
            self.send_error(404)

app = MyWebServer(ManuseioHttpRequest)

if __name__ == "__main__":
    app.run(port=PORT)