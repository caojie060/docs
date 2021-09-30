# VS Code 的 REST Client插件

接口测试辅助工具

### 安装方式

在插件市场中搜索 `REST Client` 并安装即可

[REST Client插件](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
REST Client 支持了 [cURL](https://en.wikipedia.org/wiki/CURL) 和 [RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html) 两种标准来调用 REST API
## **RFC 2616**

下面就是一个符合RFC 2616标准的POST请求

```http
POST http://dummy.restapiexample.com/api/v1/create HTTP/1.1
content-type: application/json

{
    "name":"Hendry",
    "salary":"61888",
    "age":"26"
}
```

我们在 VS Code 新建一个以 `.http` 或者 `.rest` 结尾的文件，填入你的 HTTP 请求，点击 `Send Request`，或者右键选择 `Send Request`，或者直接用快捷键 Ctrl+Alt+R ，你的 REST API 就执行了，然后 API Response 就会显示在右边区域。

```http
//正常Get请求
GET https://example.com/comments/1

//Post请求 Json格式提交
POST https://example.com/comments  
User-Agent: rest-client
Accept-Language: en-GB,en-US;q=0.8,en;q=0.6,zh-CN;q=0.4
Content-Type: application/json

{
    "name": "sample",
    "time": "Wed, 21 Oct 2015 18:27:50 GMT"
}

//Post请求表单提交
POST https://api.example.com/login 
Content-Type: application/x-www-form-urlencoded

name=foo
&password=bar

/*特别注意，参数和标头必须有空一行，否则会报错的*/
```

使用方式
在当前文件夹下新建一个 以 .http 或者 以 .rest结尾的文件,并打开该文件输入内容;
按照 HTTP Raw 的格式编写请求内容
在编写请求内容完成后,会在请求方式上方浮现一个 Send Request按钮,点击该按钮即可完成请求的调用
在执行调用后,会在右方弹出一个窗口用以返回调用结果

## **cURL**

下面是一个符合cURL标准的POST请求

```http
curl -X POST "http://dummy.restapiexample.com/api/v1/create" -d "Hello World"
```

同样地，也能通过 REST Client 在 VS Code 里一键运行。
## **HTTP语言**

REST Client 添加了 HTTP 语言的定义，支持把以 . http 或者 . rest 结尾的文件当作 HTTP 语言，提供了语法高亮，代码自动补全，代码注释等功能。
HTTP 文件的最大好处，就是方便分享。
你可以把 HTTP 文件文件放到 GitHub，这样的话，所有开发或者使用项目的人都能复用这个 HTTP 文件了。也极大的方便管理你的所有 REST API。
更方便的是，通过###分隔符，同一个 HTTP 文件里可以涵盖多个 HTTP 请求。不像 Postman，不同的 HTTP 请求需要放在不同的 tab 里。
## **代码生成**

“代码生成”也是 REST Client 里一个很方便的功能，你可以方便地通过 Generate Code Snippet 命令来把 HTTP 请求生成出不同编程语言的代码：JavaScript, Python, C, C#, Java, PHP, Go, Ruby, Swift 等等主流语言。
比如Get 请求，然后 Shift+Ctrl+P 进入 VsCode 的命令行，然后选择 Rest Client: Generate Code Snippet 就会展示一下界面，然后选择你想要转换的语言就可以了
## **高阶功能**

其实REST Client还有很多的功能，有需求的童鞋可以慢慢挖掘，笔者列出了一些比较有用的高阶功能：

-   Authentication：REST Client支持了Basic Auth，SSL Client Certificates，Azure Active Directory等多种验证机制
-   Cookies的支持
-   支持 HTTP 3xx 的重定向
-   变量的支持：环境变量，文件变量，预定义的系统变量等等

下面就是使用文件变量的一个例子，这样在不同的HTTP请求中，变量就能共享了。其中，{{$datetime iso8601}} 是预定义的系统变量

```http
@hostname = api.example.com
@port = 8080
@host = {{hostname}}:{{port}}
@contentType = application/json
@createdAt = {{$datetime iso8601}}

###

@name = hello

GET https://{{host}}/authors/{{name}} HTTP/1.1

###

PATCH https://{{host}}/authors/{{name}} HTTP/1.1
Content-Type: {{contentType}}

{
    "content": "foo bar",
    "created_at": {{createdAt}}
}
```


[[VSCode插件推荐] REST Client: 也许是比Postman更好的选择 - 知乎](https://zhuanlan.zhihu.com/p/54266685)
[使用VsCode的Rest Client进行请求测试 - 国产小品牌 - 博客园](https://www.cnblogs.com/niubi007/p/11422715.html)
[简单实用的 VSCODE 插件 ·Rest Client·_ghimi的博客-CSDN博客](https://blog.csdn.net/weixin_36242811/article/details/108611523)
[VSCode 小鸡汤 第01期 - REST Client 简单好用的接口测试辅助工具 - noark9 - 博客园](https://www.cnblogs.com/noark9/p/10348198.html)