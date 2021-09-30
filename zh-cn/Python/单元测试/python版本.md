## 查看本机上有哪些可用Python版本

```bash
ls /usr/local/lib/
```
## 安装python3.6

```bash
sudo add-apt-repository ppa:jonathonf/python-3.6   #这个指令是真的方便。记住要按一下Enter键确认。	已经不能用
sudo apt-get update 
sudo apt-get install python3.6
```

或者

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```

若上述运行sudo add-apt-repository ppa:deadsnakes/ppa 出现 “bash: add-apt-repository: command not found” 则先运行：

```bash
sudo apt-get install -y software-properties-common
```

或者

```bash
sudo apt-get install software-properties-common python-software-properties 
#注释：即安装software-properties-common 和 python-software-properties 即可
```



## 查看python版本的优先级

```bash
sudo update-alternatives --config python
```

若没有设置优先级，则会显示如下error：

```bash
update-alternatives: error: no alternatives for python3
```

```bash
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
```

你也可以另外一种方式来设置python的默认版本：

```bash
sudo update-alternatives  --set python /usr/bin/python3.6
```

## 设置python的关联版本

上述方式在终端输入python，会默认使用你设置的版本，但是如果你想在终端输入python时显示2.7的版本，输入python3时才是你想要的版本时，你就需要关联一下版本。
也许你会碰到明明通过apt-get install python3.6 安装了python3版本，但是在终端输入python3时却提示：

```bash
bash: /usr/bin/python3: No such file or directory
```

此时就需要做关联了，做好关联后也相当于设置了默认参数。

```bash
1. 打开.bashrc
 	vim ~/.bashrc
 2. 在.bashrc中添加
 	alias python3=python3.6
 	or
 	alias python3='/usr/bin/python3.6'
 3. 保存并退出文件编辑，使配置生效
 	source ~/.bashrc
```

## 为python安装对应的pip

为python3.6安装对应的pip

```bash
curl https://bootstrap.pypa.io/ez_setup.py -o - | python3.6 && python3.6 -m easy_install pip
or
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" python3 get-pip.py --user
```

## 卸载python

```bash
sudo apt autoremove python3.6
```

