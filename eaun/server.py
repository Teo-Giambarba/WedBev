from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        message = "<html><head><meta charset=\"UTF-8\"></head><body><h1>Olá, Mundo~</h1></body></html>"
        self.wfile.write(message.encode())

if __name__ == "__main__":
    server_address = ('', 8000)
    http = HTTPServer(server_address, MyHandler)
    print('Server rodando em http://localhost:8000')
    http.serve_forever()