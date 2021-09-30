socketio

websocket基于TCP

它通过 HTTP/HTTPS 协议发送一条特殊的请求进行握手后创建了一个 TCP 连接，此后浏览器 / 客户端和服务器之间便可以通过此连接来进行双向实时通信

### 为什么要用websocket

HTTP 协议是无状态、单向通信的，即客户端请求一次，服务器回复一次。如果想让服务器消息及时下发到客户端，需要采用类似于轮询的机制，即客户端定时频繁的向服务器发出请求，这样效率很低，而且 HTTP 数据包头本身的字节量较大，浪费了大量带宽和服务器资源；

为提高效率，出现了 AJAX/Comet 技术，它实现了双向通信且节省了一定带宽，但仍然需要发出请求，本质上仍然是轮询；

新一代 HTML 标准 HTML5 推出了 WebSocket 技术，它使客户端和服务器之间能通过 HTTP 协议建立 TCP 连接，之后便可以随时随地进行双向通信，且交换的数据包头信息量很小；



在支持 WebSocket 的浏览器中，创建 Socket 之后，通过 

onopen

onmessage

onclose

onerror

 四个事件的实现来处理 Socket 的响应



如果游戏需要同时支持手机端、Web 端，那毫无疑问应该使用 WebSocket，现在各个平台都提供了相应的 WebSocket 实现。如果游戏不需要支持 Web 端，且对实时性要求比较高，如多人射击、MMORPG 之类，那么使用 TCP/UDP 结合的原生 Socket 会比较好。



WebSocket 是 HTML5 最新提出的规范，虽然主流浏览器都已经支持，但仍然可能有不兼容的情况，为了兼容所有浏览器，给程序员提供一致的编程体验，SocketIO 将 WebSocket、AJAX 和其它的通信方式全部封装成了统一的通信接口，也就是说，我们在使用 SocketIO 时，不用担心兼容问题，底层会自动选用最佳的通信方式。因此说，WebSocket 是 SocketIO 的一个子集。

## Python websockets 库

Python websockets 是用于在 Python 中构建 WebSocket 服务器和客户端的库，它基于 asyncio 异步 IO 建立，提供基于协程的 API。
请尽量使用 Python≥3.6 以上版本来运行 websockets。
安装 websockets：

```shell
pip3 install websockets
```

主要用到的 API 有：

```python
websockets.connect()
websockets.send()
websockets.recv()
```

### 服务端

`server.py`，用于构建 websocket 服务器，在本地 8765 端口启动，会将接收到的消息加上 `I got your message:` 返回回去。

```python
import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        await websocket.send(message)


asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
```

`client.py` 和指定 url 建立 websocket 连接，并发送消息，然后等待接收消息，并将消息打印出来。

```python
import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        recv_text = await websocket.recv()
        print(recv_text)


asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
```

先执行 server.py，再执行 client.py，client.py 的输出结果如下：

```bash
I got your message: Hello world!
```

###  主动发消息

建立连接之后，客户端可以随时接收服务器发来的消息。服务器可以依据逻辑，给客户端推送指定消息。
服务器和客户端代码会有一点变化，在服务器回完第一条消息之后，开始轮询时间，当秒数达到 0 的时候，会主动给客户端回一条消息。
server.py：

```python
import asyncio
import websockets
import time


async def echo(websocket, path):
    async for message in websocket:
        message = "I got your message: {}".format(message)
        await websocket.send(message)

        while True:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if str(t).endswith("0"):
                await websocket.send(t)
                break


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()
```

client.py：

```python
import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello world!")
        print("< Hello world!")
        while True:
            recv_text = await websocket.recv()
            print("> {}".format(recv_text))


asyncio.get_event_loop().run_until_complete(
    hello('ws://localhost:8765'))
```

先执行 server.py，再执行 client.py，client.py 的输出结果如下：

> ```bash
> < Hello world!
> 
> > I got your message: Hello world!
> > 2020-05-29 15:11:50
> ```
>
> >
> > 最后一条消息则是服务端主动给客户端发送的。









[使用 Python 创建 websocket 服务和客户端请求]:https://blog.csdn.net/weixin_39198406/article/details/106418574

