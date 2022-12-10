import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info(message)
    writer.write(data)

    await writer.drain()

    print('Data received: {!r}'.format(data))

    print("Close the connection")
    writer.close()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 6000)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()
asyncio.run(main())