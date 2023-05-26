import http.server
import socketserver
import threading


def start_server():
    port = 8765
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Server started at localhost:" + str(port))
        httpd.serve_forever()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    threading.Thread(target=start_server).start()
    print_hi('PyCharm')
