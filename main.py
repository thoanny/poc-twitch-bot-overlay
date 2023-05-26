import http.server
import socketserver
import threading
import functools


def start_server():
    port = 8765
    handler = http.server.SimpleHTTPRequestHandler
    handler.extensions_map.update({
        ".js": "text/javascript",
    })
    handler = functools.partial(handler, directory='overlay/dist')

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Server started at localhost:" + str(port))
        httpd.serve_forever()


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    threading.Thread(target=start_server).start()
    print_hi('PyCharm')
