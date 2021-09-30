## ubuntu安装nodejs直接版

```bash
apt-get update
apt-get upgrade
```

### 16.04版本

```bash
sudo apt-get install nodejs
sudo apt install nodejs-legacy
sudo apt install npm
```

### ubuntu18-20

```bash
sudo apt-get install nodejs
sudo apt install libssl1.0-dev nodejs-dev node-gyp npm
sudo apt install npm
```

### 将`npm`的包更改为淘宝的镜像源

```bash
sudo npm config set registry https://registry.npm.taobao.org 
sudo npm config list
```

### 全局安装n管理器(用于管理nodejs版本)

```bash
sudo npm install n -g
```

### 更新到stable版本

```bash
sudo n stable
sudo node -v
```

### 反手安装一个`git`

```bash
sudo apt-get install git
```



## 曲线救国法

```bash
sudo apt update
```

### 安装 npm

```bash
sudo apt install npm
```

### 安装 n 模块

> 注：n 模块是用来安装各种版本的 node 的一个工具。参数 -g 表示全局安装

```bash
sudo npm install n -g
```

### 安装最新长期支持版 node

```bash
sudo n lts
```

### 检验

```bash
node -v
```

### 各种版本简介

n 模块可以安装各种版本的 node，非常方便。

- latest – 最新版，但不一定稳定
- stable – 最新的稳定版，比 latest 老一点，优点是稳定，但不是长期支持版（api 可能会变动）
- lts – 最新的长期支持版，这是最推荐使用的版本。虽然比 stable 老，但是是长期支持的版本（当然也是稳定版本）。是 long term support 的缩写。

除此之外，可以直接通过版本号，安装制定版本的 node

```bash
sudo n [版本号]
```

### 版本之间的切换

码者目前得知的是：可以通过 n 模块的 use 命令，切换版本：

```bash
sudo n use [版本] # 比如 sudo n use lts
```

但是不知道什么原因，总切换不成功，也没有报错信息。
于是码者通过重新安装，也成功切换了版本，比如切换到 lts 版本就重新安装一下：

```bash
sudo n lts
```

于是就可以使用 lts 版本了。


[在 ubuntu 上安装最新的 node_大概关于-CSDN博客](https://blog.csdn.net/csdn372301467/article/details/85938702)
[Ubuntu安装Nodejs - 轻描丨淡写 - 博客园](https://www.cnblogs.com/xuexianqi/p/13369982.html)