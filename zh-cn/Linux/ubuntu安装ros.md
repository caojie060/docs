

1.设置sources.list

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

2.设置key（公钥已更新）

```bash
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

或

```bash
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key     421C365BD9FF1F717815A3895523BAEEB01FA116
```

3.更新package

```bash
sudo apt-get update
```

或

```bash
sudo apt-get update && sudo apt-get upgrade -y
```

4.安装ros kinetic完整版

```bash
sudo apt-get install ros-kinetic-desktop-full
```

5.初始化rosdep

注意：在使用ROS之前需要初始化rosdep

```bash
sudo rosdep init
rosdep update
```

6.配置ros环境

```bash
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

7.安装依赖项

```bash
sudo apt-get install python-rosinstall python-rosinstall-generator python-wstool build-essential
```

8.测试ros是否安装成功

```bash
roscore
```



如果想安装其他ROS功能包，可以使用apt-cache命令搜索ros-kinetic开头的所有功能包。

```bash
$ apt-cache search ros-kinetic
```


如果想安装个别功能包，请使用如下命令。

```bash
$ sudo apt-get install ros-kinetic-[功能包名称]
```

**安装rosinstall**

这是安装ROS各种功能包的程序。很有用的工具，务必安装。

```bash
sudo apt-get install python-rosinstall
```

**创建并初始化工作目录**

新版本ROS使用名为catkin的工具来构建系统，为了使用它需要创建并初始化catkin工作目录。

```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
```

在所创建的catkin工作目录,使用catkin_make命令来构建。

```bash
$ cd ~/catkin_ws/
$ catkin_make
```

加载与catkin构建系统相关的环境文件。

```bash
$ source ~/catkin_ws/devel/setup.bash
```














[Ubuntu16.04下安装ROS Kinetic（详细图文教程）_野原新之助007-CSDN博客](https://blog.csdn.net/qq_40936141/article/details/86241910)
[Ubuntu16.04安装ROS Kinetic详细过程_^_^妖言惑眾的博客-CSDN博客_ubuntu16.04安装ros](https://blog.csdn.net/weixin_43159148/article/details/83375218)