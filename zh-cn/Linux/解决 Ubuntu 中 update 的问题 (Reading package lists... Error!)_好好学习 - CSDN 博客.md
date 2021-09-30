> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/wuyilun2013/article/details/43151191)

问题描述: 像安装一个软件, 发现会弹出下列的问题:

Reading package lists... Error!  
E: Encountered a section with no Package: header  
E: Problem with MergeList /var/lib/apt/lists/cn.archive.ubuntu.com_ubuntu_dists_trusty_main_i18n_Translation-en  
E: The package lists or status file could not be parsed or opened.

如下图所示:

![](https://img-blog.csdn.net/20150126130650859?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3V5aWx1bjIwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

尝试了网上的解决办法, 就是输入下面两条命令：

sudo rm /var/lib/apt/lists/* -vf

sudo apt-get update

然后 update 的时候发现了后面出现很多 W: Failed to fetch 的错误, 如下图所示. 然后在 update, 发现还是不行, 一样的错误.

  

![](https://img-blog.csdn.net/20150126130734991?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3V5aWx1bjIwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

解决方法:

1 在 setting 里面找到 software&updates, 如下图所示. 注意, 把'Download from'那里该一下, 我把原来的 from china 改为下面那个, 你可以自己选择一个合适的.

![](https://img-blog.csdn.net/20150126130845596?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3V5aWx1bjIwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)  

2 重新输入 sudo apt-get update 命令, 没有错误, 如下图所示.  再安装软件, 可以正常安装了, 问题解决!

![](https://img-blog.csdn.net/20150126130740841?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3V5aWx1bjIwMTM=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)