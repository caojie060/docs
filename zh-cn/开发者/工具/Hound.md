# Hound

 **[Gitee 极速下载](https://gitee.com/mirrors) / [hound](https://gitee.com/mirrors/hound)**

[![建置状态](https://travis-ci.org/hound-search/hound.svg?branch=master)](https://travis-ci.org/hound-search/hound) [![.github / workflows / go.yaml](https://github.com/hound-search/hound/workflows/.github/workflows/go.yaml/badge.svg)](https://github.com/hound-search/hound/actions)

> ## ![：警告：](https://gitee.com/assets/emoji/warning-e22260ba8d6c6bc2c0b65eabb98299bf.png) Hound的默认分支名称正在更改！ ![：警告：](https://gitee.com/assets/emoji/warning-e22260ba8d6c6bc2c0b65eabb98299bf.png)
>
> **我们会将默认分支的名称从`master`更改为`main`2021 年 2 月 24 日**。我们将使用[Github 的分支重命名功能](https://github.com/github/renaming/#renaming-existing-branches)，这意味着任何打开的拉取请求都应自动重新定位，并且指向`master`分支上代码的 Web 请求应按预期重定向。这种变化在大多数情况下应该是不可见的，但是您将需要更新任何明确依赖于 Hound`master`分支的存在的代码。

Hound是一个非常快速的源代码搜索引擎。核心基于 Russ Cox 的本文（和代码）： [具有 Trigram Index 的正则表达式匹配](http://swtch.com/~rsc/regexp/regexp4.html)。Hound本身是一个静态的 [React](http://facebook.github.io/react/)前端，它与[Go](http://golang.org/)后端进行通讯。后端为每个存储库保留最新索引，并通过最小的 API 答复搜索。它在起作用：

![Hound屏幕截图](https://gitee.com/mirrors/hound/raw/master/imgs/screen_capture.gif)

## 快速入门指南

### 使用 Go 工具

1. 如果还没有[安装 Go](https://golang.org/doc/install)，请[安装](https://golang.org/doc/install)它。Hound需要 1.4 或更高版本。您可能还想定义一个[`GOPATH`](https://github.com/golang/go/wiki/GOPATH)环境变量）（如果您没有明确设置，则默认为 $ HOME /go）。如果一切都已正确安装，`go version`则应打印出已安装的 go 版本。
2. 使用 Go 工具安装 Hound。二进制文件`houndd`（服务器）和`hound`（cli）将安装在您的GOPATH/bindirectory。您的GOPATH应该在您的 $PATH 中（`echo $PATH`以进行检查）。

```
go get github.com/hound-search/hound/cmds/...
```

1. 创建一个 config.json 文件，并使用它列出您的存储库。查看我们的[example-config.json，](https://gitee.com/mirrors/hound/blob/master/config-example.json) 以了解如何设置各种类型的存储库。例如，我们可以使用在[default-config.json 中](https://gitee.com/mirrors/hound/blob/master/default-config.json)找到的配置将 Hound 配置为搜索自己的源代码：

```
{
  "dbpath" : "db",
  "repos" : {
    "Hound" : { "url" : "https://github.com/etsy/hound.git" }
  }
}
```

可用配置选项的完整列表可以在[此处](https://gitee.com/mirrors/hound/blob/master/docs/config-options.md)找到。
3.`houndd`在与您的目录相同的目录中运行 Hound 服务器`config.json`。您应该看到类似于以下内容的输出：

```
2015/03/13 09:07:42 Searcher started for statsd
2015/03/13 09:07:42 Searcher started for Hound
2015/03/13 09:07:42 All indexes built!
2015/03/13 09:07:42 running server at http://localhost:6080
```

1. 默认情况下，Hound在[http：// localhost：6080](http://localhost:6080/)托管一个 Web ui 。在浏览器中将其打开，然后开始搜索。

### 使用 Docker（1.4+）

1. 如果没有，请[安装 Docker](https://docs.docker.com/get-docker/)。我们至少需要`Docker >= 1.14`。
2. 创建一个 config.json 文件，并使用它列出您的存储库。查看我们的[example-config.json，](https://gitee.com/mirrors/hound/blob/master/config-example.json) 以了解如何设置各种类型的存储库。例如，我们可以将 Hound 配置为使用[default-config.json 中](https://gitee.com/mirrors/hound/blob/master/default-config.json)的配置搜索其自身的源代码。
3. 跑步

```
docker run -d -p 6080:6080 --name hound -v $(pwd):/data etsy/hound
```

您应该能够照常导航到[http：// localhost：6080 /](http://localhost:6080/)。

## 在生产中运行

在生产中没有运行 Hound 的特殊标志。您可以使用该`--addr=:6880`标志来控制服务器绑定到的端口。当前，Hound 不支持 TLS，因为大多数用户只是在 Apache 或 nginx 后面运行 Hound。但是，我们愿意为添加 TLS 支持做出贡献。

## 为什么要使用其他代码搜索工具？

过去，我们使用过许多类似的工具，其中大多数要么太慢，太难配置，要么需要安装太多软件。这带我们去...

## 要求

- 转到 1.13+

是的，就是这样。您可以通过 Apache /nginx/etc 等将请求代理到 Go 服务，但这不是必需的。

## 支持

目前，Hound 仅在 MacOS 和 CentOS 上进行过测试，但是它可以在任何 * nix 系统上运行。不支持 Windows 上的 Hound，但我们听说它可以编译并运行良好（尽管这有助于从 Windows Search Indexer 中排除数据文件夹）。

Hound支持以下版本控制系统：

- Git - 这是默认设置
- Mercurial-`"vcs" : "hg"`在配置中使用
- SVN-`"vcs" : "svn"`在配置中使用
- Bazaar -`"vcs" : "bzr"`在配置中使用

有关如何使用每个 VCS 的示例，请参见[config-example.json](https://gitee.com/mirrors/hound/blob/master/config-example.json)。

## 私人仓库

有两种方法可以使 Hound 索引私有存储库：

- 使用`file://`协议。这使您可以索引存储库的本地克隆。不利的一面是使回购保持最新状态的轮询将无法进行。（这也不适用于非受支持的存储库类型的本地文件夹。）如果使用的是 Docker，则必须将卷挂载到存储库（例如`-v $(pwd)/src:/src`），并在配置中使用存储库的相对路径。
- 在配置中使用 SSH 样式网址：`"url" : "git@github.com:foo/bar.git"`。只要 在运行 Hound 的盒子上设置[SSH 密钥](https://help.github.com/articles/generating-ssh-keys/)，它就可以工作。

## 保持回购更新

默认情况下，Hound每 30 秒轮询一次配置中的 URL，以进行更新。您可以通过`ms-between-poll`在配置中按每个存储库设置密钥来覆盖此值。如果要索引大量存储库，则可能还需要对`max-concurrent-indexers`属性进行调整。您可以在[示例 config 中](https://gitee.com/mirrors/hound/blob/master/config-example.json)查看它们的工作方式。

## 编辑器整合

当前，以下编辑器具有支持 Hound 的插件：

- [Sublime Text](https://github.com/bgreenlee/SublimeHound)
- [Vim](https://github.com/urthbound/hound.vim)
- [Emacs](https://github.com/ryoung786/hound.el)
- [Visual Studio Code](https://github.com/sjzext/vscode-hound)

## 在Hound上乱砍Hacking on Hound

### 编辑与建筑

#### 要求：

- make
- Node.js（[安装说明](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager)）

Hound 包含一个`Makefile`帮助在本地构建的工具，但它取决于将源添加到适当的 Go 工作区中，以便 Go 工具可以相应地工作。有关[设置](https://github.com/golang/go/wiki/SettingGOPATH)Go 工作区的更多详细信息，请参见[设置 GOPATH](https://github.com/golang/go/wiki/SettingGOPATH)。通过`GOPATH`设置，以下命令将在本地构建Hound。

```
git clone https://github.com/hound-search/hound.git ${GOPATH}/src/github.com/hound-search/hound
cd ${GOPATH}/src/github.com/hound-search/hound
make
```

如果这是您唯一的 Go 项目，则可以仅为 Hound 设置 GOPATH：

```
git clone https://github.com/hound-search/hound.git src/github.com/hound-search/hound
GOPATH=$(pwd) make -C src/github.com/hound-search/hound
```

### 测验

Hound 中的每个程序包中的测试数量都在增加。在上传您的拉取请求之前，请确保这些通过。您可以使用以下命令运行测试。要运行整个测试套件，请使用：

```
make test
```

如果您只想运行 JavaScript 测试套件，请使用：

```
npm test
```

任何结尾的 Go 文件`_test.go`都被认为是测试文件。同样，任何结尾的 JavaScript 文件`.test.js`都将由我们的测试运行器 Jest 自动运行。测试应位于其涵盖的文件旁边。 [查看 Jest 的文档](https://jestjs.io/docs/en/getting-started)以获取有关编写 Jest 测试的更多详细信息，并[查看 Go 的测试文档](https://golang.org/pkg/testing/)以获取有关测试 Go 代码的更多详细信息。

您需要安装`Node.js >= 12`并`jest`通过`npm install jest`运行 JS 测试进行安装。

### 在 Web UI 上工作

Hound包括一个由多个文件（html，css，javascript 等）组成的 Web UI。为了确保Hound能够与标准 Go 工具无缝配合，这些资源都捆绑在`houndd`二进制文件中。请注意，对 UI 的更改将导致`ui/bindata.go`文件的本地更改。您必须在 “拉取请求” 中包括这些更改。

捆绑`ui/bindata.go`使用中的 UI 更改：

```
make ui
```

为了简化开发，有一个标志将从文件系统读取文件（允许广受欢迎的编辑 / 刷新周期）。

首先，您应该通过运行以下命令来确保已安装所需的所有依赖项：

```
make dev
```

然后使用 --dev 选项运行Hound服务器：

```
bin / houndd --dev
```

## 保持联系

由[Etsy](https://www.etsy.com/)创建，方法是：

- [凯莉・诺顿（Kelly Norton）](https://github.com/kellegous)
- [乔纳森・克莱因（Jonathan Klein）](https://github.com/jklein)

Hound的维护方法：

- [大卫・肖特](https://github.com/dschott68)
- [雅各布・罗斯](https://github.com/jacobrose)
- [尼克・索耶（Nick Sawyer）](https://github.com/nickmoorman)
- [塞勒姆・希拉尔](https://github.com/salemhilal)

[hound]:https://gitee.com/mirrors/hound

