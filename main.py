import asyncio
import functools
import http.server
import socketserver
import threading
import websockets

from dotenv import dotenv_values
from twitchio.ext import commands
from websockets.server import serve

CONNECTIONS = set()

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


async def ws_handler(websocket):
    CONNECTIONS.add(websocket)
    async for message in websocket:
        await websocket.send(message)


async def ws_start():
    port = 8001
    async with serve(ws_handler, "localhost", port):
        print("WS Server started at localhost:" + str(port))
        await asyncio.Future()


@bot.event
async def event_ready():
    print(f'Bot is online!')


@bot.command(name='test')
async def test(ctx):
    websockets.broadcast(CONNECTIONS, 'Test passed!')
    await ctx.send('test passed!')


def print_hi(name):
    print(f'Hi, {name}')


def run_bot():
    bot.run()


if __name__ == '__main__':
    print_hi('PyCharm')
    threading.Thread(target=start_server).start()
    threading.Thread(target=run_bot).start()
    asyncio.run(ws_start())

