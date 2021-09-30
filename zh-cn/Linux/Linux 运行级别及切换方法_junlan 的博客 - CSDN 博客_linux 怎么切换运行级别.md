> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/qq_21453783/article/details/100251461)

一、init 简介
=========

        Linux 系统操作中不可缺少的程序之一，它是一个由内核启动的用户级进程。内核会在过去曾使用过 init 的几个地方查找它，它的正确位置（对 Linux 系统来说）是 / sbin/init。如果内核找不到 init，它就会试着运行 / bin/sh，如果运行失败，系统的启动也会失败。

二、Linux 系统 7 个运行级别（runlevel）
============================

操作系统当前正在运行的功能级别，从 0-6，具有不同的功能**：**

*   **系统关机模式**（**runlevel** **0**）：系统默认运行级别不能设置为 0，否则无法正常启动系统（一开机就自动关机）。
*   **单用户模式**（**emergency.target**：**runlevel** **1**）：也称为救援模式，root 权限，用于系统维护，禁止远程登陆，类似 Windows 下的安全模式登录。
*   **多用户模式**（**rescue.target**：**runlevel** **2**）：没有 NFS 网络支持。
*   **完整的多用户文本模式**（**multi-user.targe****t**：**runlevel** **3**）：有 NFS，登陆后进入控制台命令行模式。
*   **系统未使用**（**runlevel** **4**）：保留一般不用，在一些特殊情况下可以用它来做一些事情。例如在笔记本电脑的电池用尽时，可以切换到这个模式来做一些设置。
*   **图形化模式**（**graphical.target：runlevel** **5**）：登陆后进入图形 GUI 模式或 GNOME、KDE 图形化界面，如 X Window 系统。
*   **重启模式**（**runlevel** **6**）：默认运行级别不能设为 6，否则无法正常启动系统。

三、启动原理简介
========

1、在目录 / etc/rc.d/init.d 下有许多服务器脚本程序，一般称为服务 (service)：

[root@localhost ~]# **ll  /etc/rc.d/init.d/**

![](https://img-blog.csdnimg.cn/20200423162455585.png)

2、在 / etc/rc.d 下有 7 个名为 rcN.d 的目录，对应系统的 7 个运行级别即 rc0.d-rc6.d：

![](https://img-blog.csdnimg.cn/20200423162524439.png)

注意：

最小化安装的操作系统默认没有图形化软件，安装图形化软件方法如下：

[root@localhost ~]# **yum install -y xorg* gnome* glx***

四、更改系统默认的启动级别
=============

1、查看默认启动的运行模式：

[root@localhost ~]# **systemctl get-default**

![](https://img-blog.csdnimg.cn/2020042316255788.png)

2、设置默认启动为多用户字符界面：

[root@localhost ~]# **systemctl set-default multi-user.target**

![](https://img-blog.csdnimg.cn/20200423162614807.png)

五、从字符界面切换到图形界面的方法：
==================

1、此方法切换至图形化不需要重新输用户名和密码登录：

[root@localhost ~]# **startx**         

2、此方法切换需重新输用户名和密码登录，可以通过 **systemctl isolate multi-user.target** 再切换回命令行模式： 

[root@localhost ~]# **systemctl  isolate graphical.target**      

3、此方法切换需重新输用户名和密码登录，可以通过 **init3** 再切换回命令行模式：

[root@localhost ~]# ** init** **5** 

4、通过快捷键方式切换：

  可使用 Ctrl+Alt+F1~6 进行切换，Ctrl+Alt+1 为图形界面。