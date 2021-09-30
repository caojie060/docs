> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/pkueecser/article/details/6089834)

```
1.在终端输入:sudo apt-get remove 要删除的软件包名  
```

例如 sudo apt-get remove eva  
也可以在新立得软件管理包里删除。  选择彻底清除。。

  
或者  
2. 软件中心的系统工具里找到 “Add/Remove Applications” 并安装，  
 然后就可以在菜单 “系统——系统工具” 里打开 “添加 / 删除程序” 了。  
  
linux 和 windows 系统不同，linux 不会产生无用垃圾文件，但是在升级缓存中，linux 不会自动删除这些文件，还是很占硬盘的！  
  
**一、删除缓存**  
  
1，非常有用的清理命令：  
sudo apt-get autoclean                清理旧版本的软件缓存  
sudo apt-get clean                       清理所有软件缓存  
sudo apt-get autoremove             删除系统不再使用的孤立软件  
  
这三个命令主要清理升级缓存以及无用包的。  
  
2，清理 opera firefox 的缓存文件：  
ls ~/.opera/cache4  
ls ~/.mozilla/firefox/*.default/Cache  
  
3，清理 Linux 下孤立的包：  
终端命令下我们可以用：  
sudo apt-get install deborphan -y  
  
4，卸载：tracker  
这个东西一般我只要安装 ubuntu 就会第一删掉 tracker 他不仅会产生大量的 cache 文件而且还会影响开机速度。所以在新得利里面删掉就行。  
  
  
附录：  
包管理的临时文件目录:  
包在  
/var/cache/apt/archives  
  
没有下载完的在  
/var/cache/apt/archives/partial   
  
**二、删除软件**  
  
ubuntu 软件的删除一般用 “ubuntu 软件中心” 或“新立得”就能搞定，但有时用命令似乎更快更好～～  
  
sudo apt-get remove --purge 软件名  
  
sudo apt-get autoremove                                                        删除系统不再使用的孤立软件  
  
sudo apt-get autoclean                                                            清理旧版本的软件缓存  
  
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P              清除残余的配置文件  
  
保证干净。  
  
**三、删除多余内核**  
  
1，首先要使用这个命令查看当前 Ubuntu 系统使用的内核  
  
uname -a  
  
2，再查看所有内核  
  
dpkg --get-selections|grep linux  
  
3，最后小心翼翼地删除吧  
  
sudo apt-get remove linux-image-2.6.32-22-generic  
  
ps：linux-image-xxxxxx-generic    就是要删除的内核版本  
还有  
linux-headers-xxxxxx  
linux-headers-xxxxxx-generic    总之中间有 “xxxxxx” 那段的旧内核都能删，注意一般选内核号较小的删。  
  
  
  
默认情况下 ,gcc 和 g++ 是已经预装好的.  
  
  
  
安装软件  

命令： sudo apt-get install softname1 softname2 softname3……  
卸载软件  
命令：sudo apt-get remove softname1 softname2 softname3……  
卸载并清除配置  
命令： sudo apt-get remove –purge softname1  
更新软件信息数据库  
命令： sudo apt-get update  
进行系统升级  
命令： sudo apt-get upgrade  
搜索软件包  
命令： sudo apt-cache search softname1 softname2 softname3……  
Deb 软件包相关安装与卸载

安装 deb 软件包  
命令： dpkg -i xxx.deb  
删除软件包  
命令：  dpkg -r xxx.deb  
连同配置文件一起删除  
命令： dpkg -r –purge xxx.deb  
查看软件包信息  
命令： dpkg -info xxx.deb  
查看文件拷贝详情  
命令： dpkg -L xxx.deb  
查看系统中已安装软件包信息  
命令： dpkg -l  
重新配置软件包  
命令：  dpkg-reconfigure xxx

```
================================================================================================
```

安

装了 Ubuntu 后，的确感到耳目一新，尝试了许多新鲜有趣的软件，不由得想与大家分享一下其中的快乐。上次说的是抓图工具，因为没有它，我的这个图文系列也无从谈起。这次想给大家介绍增加、刪除软件工具，把它排在第二位来介绍，原因很简单，我们利用和管理任何软件，都离不开这个。闲话少说，就开始看图吧 小图原大，大图点击放大。

最常用和经典的就是系统面板（左上角）“应用程序”下拉菜单中的 “添加 / 刪除...“了，通过它可以下载、安装或卸载大部分常用软件了。其中“教育” 一类软件，是在 windows 操作系统中难觅其踪的。“添加 / 刪除...“的打开位置如下图所示：

![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/.png)

打开的窗口，各项功能标示得十分清楚，第一次用也会明白。

[![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-08.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-08.png)

[![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-09.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-09.png)

“添加 / 刪除...“中有丰富的教育资源，这是 ubuntu 不同于 windows 的一个主要特点。

“添加 / 刪除...“中的资源虽然丰富，但如果你想寻找、安装中文支持资源和第三方资源提供的常用优秀软件，还又另一种更好的方法，那就是利用 Ubuntu Tweak。什么是 ubuntu Tweak 呢？Tweak 在英文中有 “用力拉” 的意思，也是 “妙计” 的含义，ubuntutweak 实际上是一个优秀的系统增强软件，其中就有增加、刪除软件的功能。在哪里下载 ubuntutweak 呢？如果你还不了解而且不会使用“终端”（类以 DOS），最好下载 deb 软件安装包，双击后可自动完成安装。ubuntu tweak0.4.3 deb 包可在以下地址得到：

> [http://ubuntu-tweak.googlecode.com/files/ubuntu-tweak_0.4.3-1%7Eintrepid1_all.deb](http://ubuntu-tweak.googlecode.com/files/ubuntu-tweak_0.4.3-1%7Eintrepid1_all.deb)

ubuntu tweak 安装后可在 “应用程序”－“系统工具 “中找到，打开后的样子如下图所示：

[![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-10.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-10.png)

在 ubuntutweak 窗口 “应用程序”－“添加 / 删除” 中有较丰富的常用软件，特別是有一些中文支持较好的软件，如永中 Office，和上回提到的截图软件 Gscrot 等等。其中的 “源编辑器” 和“第三方源”，可以提供更多及更高版本的软件。什么是 “源”，简单来说，就是软件包的来源之处，下文还会提到。我们看一下 tweak 中的“添加 / 删除” 介面。

[![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-11.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-11.png)

上图中的 Eioffice 就是永中 Office，另外 ibus 是功能极强的输入法支持程序，本文即用 ibus 五笔码出来的。

比上述两种 “添加 / 删除” 程序较为复杂的软件安装工具是“系统”－“系统管理”－“新立得软件包管理器”，本文不想太多介绍，这里只提供两张图供大家参考。

[![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-13.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-13.png)

[![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-12.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-12.png)

说了这么多，其实 ubuntu 系统中安装、刪除软件最常用的方法，还是在终端中执行 sudo apt-get install 和 sudoapt-get remove 命令，虽然目前 ubuntu 的操作越来越直观和容易，在终端中输入和执行命令仍是最快捷的办法。如下图所示：

[  
![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-16.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-16.png)

最后，说一下 “源” 吧，这个其实就是提供代码和软件包下载的服务器地址，你可选择加入源，并对之进行管理。一般可以利用 tweak 中的 “源编辑器” 加入新源，在 “第三方软件源” 查看选择源。另外 “系统”－“系统管理” 中的 “软件源” 来管理和新增源。见如下两图：

[![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-14.png)](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-14.png)

![](http://image-001.yo2cdn.com/wp-content/uploads/292/29200/2008/11/screenshot-15.png)

当然，一旦熟悉了 ubuntu，你就会习惯在终端中加入源并安装软件，编辑、新增源可在终端中输入如下命令用 Gedit 文本编辑器打开源文件：

> sudo gedit /etc/apt/sources.list

如要安装上述 tweak 软件包，可在打开的源文件中加入以下源：

> deb http://ppa.launchpad.net/tualatrix/ubuntu intrepid main  
> deb-src http://ppa.launchpad.net/tualatrix/ubuntu intrepid main

然后在终端中执行如下命令更新源并安装 tweak 即可。

> sudo apt-get update  
> sudo apt-get install ubuntu-tweak

我希望自己和所有的 ubuntu 系统爱好者都能习惯并熟练使用终端，这样会使许多事情事半功倍，包括今天所谈的软件的安装和卸载。比如，你有洁癖，容不得系统中多余无用的软件包，输入一条命令就可以了，即

> sudo apt-get autoremove

就是这么简单、安全和高效。