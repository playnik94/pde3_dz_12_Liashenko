import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 6000)
    writer.write(message.encode())
    await writer.drain()
    data = await reader.read(100)

    q1 = int(input('Число 1: '))
    q2 = int(input('Число 2: '))

    e = int(input('Какую операцию вы хотите выполнить? \n 1 Умножение  \n 2 Вычитание \n'))
    if e == 1:
        t = q1 * q2
        y = 'Умножение'
        u = y
    if e == 2:
        t = q1 - q2
        i = 'Вычитание'
        u = i
    print('Результат ', u, ' = ', t, data.decode())
    print('Close the connection')
    writer.close()
asyncio.run(tcp_echo_client(' '))