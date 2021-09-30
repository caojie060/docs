> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.cnblogs.com](https://www.cnblogs.com/tlz888/p/9569234.html)

　　在 ubuntu 下用 apt-get install 安装软件时，发现 package list 中没有所需的软件，

估计可能是 package list 太旧了，于是需要 apt-get update & apt-get upgrade。

但又怕原始的源慢，故修改为阿里云镜像。步骤如下：

### 1、备份原始源的配置文件：

```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bakcup
```

### 2、添加阿里云源到 sources.list 文件：

```
sudo vim /etc/apt/sources.list
```

[![](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

```
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
```

[![](http://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

### 3、update & upgrade

```
sudo apt-get update
sudo apt-get upgrade
```

这里，再说一下 update 和 upgrade 的区别：

**update 命令**，会访问源列表里的每个网址，并读取**软件列表**，然后保存在本地电脑。

**upgrade 命令**，会把本地已安装的软件，与刚下载的软件列表里对应软件进行对比，如果发现已安装的软件版本太低，就会提示你更新。

总而言之，**update 是更新软件列表，upgrade 是更新软件**。