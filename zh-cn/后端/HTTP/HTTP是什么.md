# HTTP是什么

## [HTTP 简介](https://www.twle.cn/l/yufei/http/http-basic-index.html)

本节介绍了 HTTP 协议

HTTP 是一个基于 TCP/IP 通信协议来传递数据 ( HTML 文件, 图片文件, 查询结果等 )

### HTTP 工作原理

HTTP 协议工作于客户端-服务端架构为上。浏览器作为 HTTP 客户端通过 URL 向 HTTP 服务端即 WEB 服务器发送所有请求

**HTTP 默认端口号为** `80` **，但是你也可以改为** `8080` **或者其他端口**

### HTTP 三点注意事项

1. HTTP 是无连接

   无连接的含义是限制每次连接只处理一个请求

   服务器处理完客户的请求，并收到客户的应答后，即断开连接

   采用这种方式可以节省传输时间

2. HTTP 是媒体独立的

   这意味着，只要客户端和服务器知道如何处理的数据内容，任何类型的数据都可以通过 HTTP 发送

   客户端以及服务器指定使用适合的 [MIME-type 内容类型](https://www.twle.cn/l/yufei/http/http-basic-content-type.html)

3. HTTP 是无状态

   HTTP 协议是无状态协议

   无状态是指协议对于事务处理没有记忆能力

   缺少状态意味着如果后续处理需要前面的信息，则它必须重传，这样可能导致每次连接传送的数据量增大

   另一方面，在服务器不需要先前信息时它的应答就较快

以下图表展示了 HTTP 协议通信流程

![cgiarch](https://www.twle.cn/static/i/http_flow.png)

### HTTP 范例

我们接下来要讲解的内容都会用到下面这个范例

我们使用 `CURL` 发送模拟 `GET` 请求服务器上的 `static/media/hello.txt` 文件

#### shell 命令

```bash
curl -v  https://www.twle.cn/static/media/hello.txt
```

> 关于如何使用 CURL ,你可以查看我们的 [Linux CURL 教程](https://www.twle.cn/l/yufei/shell/shell-curl-index.html)

#### 客户端请求信息：

```http
GET /static/media/hello.txt HTTP/1.1
Host: www.twle.cn
User-Agent: curl/7.54.0
Accept: */*
```

#### 服务端响应:

```http
HTTP/1.1 200 OK
Server: Tengine
Date: Sun, 03 Sep 2017 01:08:42 GMT
Content-Type: text/plain
Content-Length: 38
Last-Modified: Sun, 03 Sep 2017 01:08:21 GMT
Connection: keep-alive
ETag: "59ab5605-26"
Strict-Transport-Security: max-age=31536000;includeSubdomains;preload
X-Frame-Options: DENY
Accept-Ranges: bytes
```

#### 输出结果：

```http
你好，世界
你好，简单编程
```



## [HTTP 消息结构](https://www.twle.cn/l/yufei/http/http-basic-messages.html)

本节介绍了 HTTP 消息结构

### HTTP 请求过程

一个HTTP `代理(userAgent)` 是一个应用程序（Web浏览器或其他任何客户端），通过连接到服务器达到向服务器发送一个或多个 HTTP 的请求的目的

一个 HTTP `服务器(SERVER)` 同样也是一个应用程序（通常是一个 Web 服务，如Apache Web 服务器或IIS服务器或 NGINX 等），通过接收客户端的请求并向客户端发送HTTP响应数据

HTTP 使用统一资源标识符（Uniform Resource Identifiers, URI）来传输数据和建立连接

一旦建立连接后，数据消息就通过类似 Internet 邮件所使用的格式 [RFC5322]和多用途Internet邮件扩展（MIME）[RFC2045]来传送

### 客户端请求消息

客户端发送一个HTTP请求到服务器的请求消息包括以下格式：请求行（request line）、请求头部（header）、空行和请求数据四个部分组成

- - 请求行（request line）

    请求行是请求消息里的第一行数据

```http
GET /static/media/hello.txt HTTP/1.1
```

- - 请求头部（header）

    请求头部为第二行到第一个空行之前所有的内容

```http
Host: www.twle.cn
User-Agent: curl/7.54.0
Accept: */*
```

- - 空行

    空行就是两个 `CRLF`

- - 请求数据

    请求数据就是空行之后的所有数据

> 除了 POST 方法和 PUT 方法，其他所有的方法都没有请求数据

### HTTP 响应结构

HTTP 响应也由四个部分组成，分别是：状态行、消息报头、空行和响应正文

- - 状态行

    服务器响应的第一行就是状态行

```http
HTTP/1.1 200 OK
```

- - 消息报头

    从第二行开始到第一个 CRLF CRLF 之前的内容为报头

```http
Server: Tengine
Date: Sun, 03 Sep 2017 01:08:42 GMT
Content-Type: text/plain
Content-Length: 38
Last-Modified: Sun, 03 Sep 2017 01:08:21 GMT
Connection: keep-alive
ETag: "59ab5605-26"
Strict-Transport-Security: max-age=31536000;includeSubdomains;preload
X-Frame-Options: DENY
Accept-Ranges: bytes
```

> CRLF 是回车换行的意思，CRLF CRLF 就是两个回车换行符

- - 空行

    空行就是 `CRLF CRLF` 也就是两个回车换行符 一个回车换行符提供换行，第二个回车换行符则提供了一个空行

- - 响应正文

    空行之后的所有内容都是响应正文

```http
你好，世界
你好，简单编程
```



[HTTP 方法](https://www.twle.cn/l/yufei/http/http-basic-methods.html)

本节介绍了 HTTP 的方法，包括 GET, POST, HEAD 等

[HTTP 头信息](https://www.twle.cn/l/yufei/http/http-basic-header-fields.html)

本节介绍了 HTTP 的头信息

[HTTP 状态码](https://www.twle.cn/l/yufei/http/http-basic-status-codes.html)

本节列出了所有 HTTP 的状态码





 [HTTP 基础教程](https://www.twle.cn/l/yufei/http/http-basic-index.html)