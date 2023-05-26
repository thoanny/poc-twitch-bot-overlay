import http.server
import socketserver
import threading
import functools
from dotenv import dotenv_values
from twitchio.ext import commands

config = dotenv_values(".env")

bot = commands.Bot(
    token=config['TMI_TOKEN'],
    client_id=config['CLIENT_ID'],
    nick=config['BOT_NICK'],
    prefix=config['BOT_PREFIX'],
    initial_channels=[config['CHANNEL']]
)


def start_server():
    port = 8000
    handler = http.server.SimpleHTTPRequestHandler
    handler.extensions_map.update({
        ".js": "text/javascript",
    })
    handler = functools.partial(handler, directory='overlay/dist')

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Server started at localhost:" + str(port))
        httpd.serve_forever()


@bot.event
async def event_ready():
    print(f"{config['BOT_NICK']} is online!")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    threading.Thread(target=start_server).start()
    bot.run()
