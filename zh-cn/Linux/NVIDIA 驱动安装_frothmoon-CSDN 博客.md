> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/frothmoon/article/details/88875020)

需要去[英伟达官网](https://www.nvidia.cn/)下载适合自己电脑的版本（nvidia 网页可以自己测出你的电脑所需要的型号）  
首先`Ctrl + Alt + F1`进入字符界面

删除原有驱动版本
--------

```
sudo apt-get purge nvidia*
sudo apt-get autoremove
sudo ./NIVIDIA-Linux-X86_64-384.59.run --uninstall
```

安装依赖
----

```
sudo apt-get install build-essential gcc-multilib dkms
```

禁用 nouveau 驱动
-------------

编辑 `/etc/modprobe.d/blacklist-nouveau.conf`文件，添加内容：

```
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```

关闭 nouveau：

```
echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
```

重启
--

```
sudo update-initramfs -u
sudo reboot
```

重启后，执行：

```
lsmod | grep nouveau
```

如果没有屏幕输出，说明禁用 nouveau 成功。

获取 kernel source
----------------

```
sudo apt-get install linux-source
sudo apt-get install linux-headers-x.x.x-x-generic
```

其中`x.x.x-x-generic`可以替换为`$(uname -r)`

关掉 x graphic 服务
---------------

```
sudo systemctl stop lightdm(or sudo service lightdm stop)
sudo systemctl stop gdm
sudo systemctl stop kdm
```

登陆 nvidia 官网，可以得到适合自己电脑的驱动，下载下来

安装 NVIDIA 驱动
------------

```
sudo chmod a+x NVIDIA*.run
sudo ./NVIDIA-Linux-x86_64-384.59.run –no-x-check -no-nouveau-check -no-opengl-files
```

`–no-opengl-files`：表示只安装驱动文件，不安装 OpenGL 文件。这个参数不可省略，否则会导致登陆界面死循环，英语一般称为”login loop” 或者”stuck in login”。  
`–no-x-check`：表示安装驱动时不检查 X 服务，非必需。  
`–no-nouveau-check`：表示安装驱动时不检查 nouveau，非必需。  
`-Z, --disable-nouveau`：禁用 nouveau。此参数非必需，因为之前已经手动禁用了 nouveau。  
`-A`：查看更多高级选项。

安装过程中一些选项：  
The distribution-provided pre-install script failed! Are you sure you want to continue?  
选择 yes 继续。  
Would you like to register the kernel module souces with DKMS? This will allow DKMS to automatically build a new module, if you install a different kernel later?  
选择 No 继续。  
问题大概是：Nvidia’s 32-bit compatibility libraries?  
选择 No 继续。  
Would you like to run the nvidia-xconfigutility to automatically update your x configuration so that the NVIDIA x driver will be used when you restart x? Any pre-existing x confile will be backed up.  
选择 Yes 继续

挂载 Nvidia 驱动
------------

```
modprobe nvidia
```

检查驱动是否安装成功
----------

```
nvidia-smi
nvidia-settings #若弹出设置对话框，亦表示驱动安装成功
```

返回图形界面
------

最后退回图形界面：`sudo init 5`or `Ctrl + Alt + F7` or `sudo service lightdm restart`

重启电脑，通过`nvidia-smi`命令查看驱动信息，如果成功显示，那么驱动安装成功

参考
--

https://www.cnblogs.com/pprp/p/9430836.html  
https://blog.csdn.net/stories_untold/article/details/78521925  
https://blog.csdn.net/cosmoshua/article/details/76644029?tdsourcetag=s_pctim_aiomsg