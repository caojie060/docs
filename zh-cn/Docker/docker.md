docker指令参数

设置ubuntu用户名密码

安装python 和 安装python包

用vscode编辑

加载卷,持久化存储

同时开两个端口-p可多次使用

用命令在外部访问
[If you run SSHD in your Docker containers, you're doing it wrong!](https://jpetazzo.github.io/2014/06/23/docker-ssh-considered-evil/)
你还需要添加一个进程管理器；例如[Monit](http://mmonit.com/monit/) 或[Supervisor](http://supervisord.org/)。这是因为 Docker 将监视一个进程。如果需要多个进程，则需要在顶层添加一个来处理其他进程。换句话说，您正在将一个精益简单的容器变成更复杂的东西。如果您的应用程序停止（如果它干净地退出或崩溃），则不是通过 Docker 获取该信息，而是必须从您的进程管理器获取它。