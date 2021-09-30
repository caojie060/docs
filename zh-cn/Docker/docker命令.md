[Docker命令大全 - Arish - 博客园](https://www.cnblogs.com/catxjd/p/9783509.html)
[docker | Docker Documentation](https://docs.docker.com/engine/reference/commandline/docker/)
[docker 命令大全 - sandea - 博客园](https://www.cnblogs.com/sandea/p/11861874.html)


### 容器生命周期管理

- [run](https://www.runoob.com/docker/docker-run-command.html)创建一个新的容器并运行一个命令

语法

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
OPTIONS说明：
-a stdin: 指定标准输入输出内容类型，可选 STDIN/STDOUT/STDERR 三项；
-d: 后台运行容器，并返回容器ID；
-i: 以交互模式运行容器，通常与 -t 同时使用；
-p: 端口映射，格式为：主机(宿主)端口:容器端口 
-t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用；
--name="nginx-lb": 为容器指定一个名称；
--dns 8.8.8.8: 指定容器使用的DNS服务器，默认和宿主一致；
--dns-search example.com: 指定容器DNS搜索域名，默认和宿主一致；
-h "mars": 指定容器的hostname；
-e username="ritchie": 设置环境变量；
--env-file=[]: 从指定文件读入环境变量；
--cpuset="0-2" or --cpuset="0,1,2": 绑定容器到指定CPU运行；
-m :设置容器使用内存最大值；
--net="bridge": 指定容器的网络连接类型，支持 bridge/host/none/container: 四种类型；
--link=[]: 添加链接到另一个容器；
--expose=[]: 开放一个端口或一组端口

```

实例

```bash
使用docker镜像nginx:latest以后台模式启动一个容器,并将容器命名为mynginx。

docker run --name mynginx -d nginx:latest
使用镜像nginx:latest以后台模式启动一个容器,并将容器的80端口映射到主机随机端口。

docker run -P -d nginx:latest
使用镜像 nginx:latest，以后台模式启动一个容器,将容器的 80 端口映射到主机的 80 端口,主机的目录 /data 映射到容器的 /data。

docker run -p 80:80 -v /data:/data -d nginx:latest
绑定容器的 8080 端口，并将其映射到本地主机 127.0.0.1 的 80 端口上。

$ docker run -p 127.0.0.1:80:8080/tcp ubuntu bash
使用镜像nginx:latest以交互模式启动一个容器,在容器内执行/bin/bash命令。

runoob@runoob:~$ docker run -it nginx:latest /bin/bash
root@b8573233d675:/# 
```



- [start/stop/restart](https://www.runoob.com/docker/docker-start-stop-restart-command.html)

```bash
docker start :启动一个或多少已经被停止的容器
docker stop :停止一个运行中的容器
docker restart :重启容器
语法
docker start [OPTIONS] CONTAINER [CONTAINER...]
docker stop [OPTIONS] CONTAINER [CONTAINER...]
docker restart [OPTIONS] CONTAINER [CONTAINER...]
实例
启动已被停止的容器myrunoob
docker start myrunoob
停止运行中的容器myrunoob
docker stop myrunoob
重启容器myrunoob
docker restart myrunoob
```

- [kill](https://www.runoob.com/docker/docker-kill-command.html) 杀掉一个运行中的容器。

```bash
docker kill [OPTIONS] CONTAINER [CONTAINER...]
OPTIONS说明：
-s :向容器发送一个信号
实例
杀掉运行中的容器mynginx
runoob@runoob:~$ docker kill -s KILL mynginx
mynginx
```

- [rm](https://www.runoob.com/docker/docker-rm-command.html) 删除一个或多少容器

```bash
语法
docker rm [OPTIONS] CONTAINER [CONTAINER...]
OPTIONS说明：
-f :通过SIGKILL信号强制删除一个运行中的容器
-l :移除容器间的网络连接，而非容器本身
-v :-v 删除与容器关联的卷
实例
强制删除容器db01、db02
docker rm -f db01 db02
移除容器nginx01对容器db01的连接，连接名db
docker rm -l db 
删除容器nginx01,并删除容器挂载的数据卷
docker rm -v nginx01
```

- [pause/unpause](https://www.runoob.com/docker/docker-pause-unpause-command.html)

```bash
docker pause :暂停容器中所有的进程。
docker unpause :恢复容器中所有的进程。
语法
docker pause [OPTIONS] CONTAINER [CONTAINER...]
docker unpause [OPTIONS] CONTAINER [CONTAINER...]
实例
暂停数据库容器db01提供服务。
docker pause db01
恢复数据库容器db01提供服务。
docker unpause db01
```

- [create](https://www.runoob.com/docker/docker-create-command.html)创建一个新的容器但不启动它

```bash
docker pause :暂停容器中所有的进程。
docker unpause :恢复容器中所有的进程。
语法
docker pause [OPTIONS] CONTAINER [CONTAINER...]
docker unpause [OPTIONS] CONTAINER [CONTAINER...]
实例
暂停数据库容器db01提供服务。
docker pause db01
恢复数据库容器db01提供服务。
docker unpause db01
```

- [exec](https://www.runoob.com/docker/docker-exec-command.html)在运行的容器中执行命令

```bash
语法
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
OPTIONS说明：
-d :分离模式: 在后台运行
-i :即使没有附加也保持STDIN 打开
-t :分配一个伪终端
实例
在容器mynginx中以交互模式执行容器内/root/runoob.sh脚本

runoob@runoob:~$ docker exec -it mynginx /bin/sh /root/runoob.sh
http://www.runoob.com/
在容器mynginx中开启一个交互模式的终端
runoob@runoob:~$ docker exec -i -t  mynginx /bin/bash
root@b1a0703e41e7:/#
```



### 容器操作

- [ps](https://www.runoob.com/docker/docker-ps-command.html)列出容器

```bash
语法
docker ps [OPTIONS]
OPTIONS说明：
-a :显示所有的容器，包括未运行的。
-f :根据条件过滤显示的内容。

--format :指定返回值的模板文件。
-l :显示最近创建的容器。
-n :列出最近创建的n个容器。
--no-trunc :不截断输出。
-q :静默模式，只显示容器编号。
-s :显示总的文件大小。
实例
列出所有在运行的容器信息。
runoob@runoob:~$ docker ps
CONTAINER ID   IMAGE          COMMAND                ...  PORTS                    NAMES
09b93464c2f7   nginx:latest   "nginx -g 'daemon off" ...  80/tcp, 443/tcp          myrunoob
96f7f14e99ab   mysql:5.6      "docker-entrypoint.sh" ...  0.0.0.0:3306->3306/tcp   mymysql
列出最近创建的5个容器信息。
runoob@runoob:~$ docker ps -n 5
CONTAINER ID        IMAGE               COMMAND                   CREATED           
09b93464c2f7        nginx:latest        "nginx -g 'daemon off"    2 days ago   ...     
b8573233d675        nginx:latest        "/bin/bash"               2 days ago   ...     
b1a0703e41e7        nginx:latest        "nginx -g 'daemon off"    2 days ago   ...    
f46fb1dec520        5c6e1090e771        "/bin/sh -c 'set -x \t"   2 days ago   ...   
a63b4a5597de        860c279d2fec        "bash"                    2 days ago   ...
列出所有创建的容器ID。
runoob@runoob:~$ docker ps -a -q
09b93464c2f7
b8573233d675
b1a0703e41e7
f46fb1dec520
a63b4a5597de
6a4aa42e947b
de7bb36e7968
43a432b73776
664a8ab1a585
ba52eb632bbd
...
```

- [inspect](https://www.runoob.com/docker/docker-inspect-command.html) 杀掉一个运行中的容器。

```bash
语法
docker inspect [OPTIONS] NAME|ID [NAME|ID...]
OPTIONS说明：
-f :指定返回值的模板文件。
-s :显示总的文件大小。
--type :为指定类型返回JSON。
实例
获取镜像mysql:5.6的元信息。
runoob@runoob:~$ docker inspect mysql:5.6
[
    {
        "Id": "sha256:2c0964ec182ae9a045f866bbc2553087f6e42bfc16074a74fb820af235f070ec",
        "RepoTags": [
            "mysql:5.6"
        ],
        "RepoDigests": [],
        "Parent": "",
        "Comment": "",
        "Created": "2016-05-24T04:01:41.168371815Z",
        "Container": "e0924bc460ff97787f34610115e9363e6363b30b8efa406e28eb495ab199ca54",
        "ContainerConfig": {
            "Hostname": "b0cf605c7757",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "3306/tcp": {}
            },
...
获取正在运行的容器mymysql的 IP。 
runoob@runoob:~$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mymysql
172.17.0.3
```

- [top](https://www.runoob.com/docker/docker-top-command.html)查看容器中运行的进程信息，支持 ps 命令参数

```bash
语法
docker top [OPTIONS] CONTAINER [ps OPTIONS]
容器运行时不一定有/bin/bash终端来交互执行top命令，而且容器还不一定有top命令，可以使用docker top来实现查看container中正在运行的进程。
实例
查看容器mymysql的进程信息。
runoob@runoob:~/mysql$ docker top mymysql
UID    PID    PPID    C      STIME   TTY  TIME       CMD
999    40347  40331   18     00:58   ?    00:00:02   mysqld
查看所有运行容器的进程信息。
for i in  `docker ps |grep Up|awk '{print $1}'`;do echo \ &&docker top $i; done
```

- [attach](https://www.runoob.com/docker/docker-attach-command.html)连接到正在运行中的容器

```bash
语法
docker attach [OPTIONS] CONTAINER
要attach上去的容器必须正在运行，可以同时连接上同一个container来共享屏幕（与screen命令的attach类似）。
官方文档中说attach后可以通过CTRL-C来detach，但实际上经过我的测试，如果container当前在运行bash，CTRL-C自然是当前行的输入，没有退出；
如果container当前正在前台运行进程，如输出nginx的access.log日志，CTRL-C不仅会导致退出容器，而且还stop了。这不是我们想要的，detach的意思按理应该是脱离容器终端，但容器依然运行。好在attach是可以带上--sig-proxy=false来确保CTRL-D或CTRL-C不会关闭容器。
实例
容器mynginx将访问日志指到标准输出，连接到容器查看访问信息。
runoob@runoob:~$ docker attach --sig-proxy=false mynginx
192.168.239.1 - - [10/Jul/2016:16:54:26 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36" "-"
```

- [events](https://www.runoob.com/docker/docker-events-command.html)从服务器获取实时事件

```bash
语法
docker events [OPTIONS]
OPTIONS说明：
-f ：根据条件过滤事件；
--since ：从指定的时间戳后显示所有事件;
--until ：流水时间显示到指定的时间为止；
实例
显示docker 2016年7月1日后的所有事件。
runoob@runoob:~/mysql$ docker events  --since="1467302400"
2016-07-08T19:44:54.501277677+08:00 network connect 66f958fd13dc4314ad20034e576d5c5eba72e0849dcc38ad9e8436314a4149d4 (container=b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64, name=bridge, type=bridge)
2016-07-08T19:44:54.723876221+08:00 container start b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64 (image=nginx:latest, name=elegant_albattani)
2016-07-08T19:44:54.726110498+08:00 container resize b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64 (height=39, image=nginx:latest, name=elegant_albattani, width=167)
2016-07-08T19:46:22.137250899+08:00 container die b8573233d675705df8c89796a2c2687cd8e36e03646457a15fb51022db440e64 (exitCode=0, image=nginx:latest, name=elegant_albattani)
...
显示docker 镜像为mysql:5.6 2016年7月1日后的相关事件。
```

```bash
runoob@runoob:~/mysql$ docker events -f "image"="mysql:5.6" --since="1467302400" 
2016-07-11T00:38:53.975174837+08:00 container start 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (image=mysql:5.6, name=mymysql)
2016-07-11T00:51:17.022572452+08:00 container kill 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (image=mysql:5.6, name=mymysql, signal=9)
2016-07-11T00:51:17.132532080+08:00 container die 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (exitCode=137, image=mysql:5.6, name=mymysql)
2016-07-11T00:51:17.514661357+08:00 container destroy 96f7f14e99ab9d2f60943a50be23035eda1623782cc5f930411bbea407a2bb10 (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:18.551984549+08:00 container create c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:18.557405864+08:00 container attach c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:18.844134112+08:00 container start c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:57:19.140141428+08:00 container die c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (exitCode=1, image=mysql:5.6, name=mymysql)
2016-07-11T00:58:05.941019136+08:00 container destroy c8f0a32f12f5ec061d286af0b1285601a3e33a90a08ff1706de619ac823c345c (image=mysql:5.6, name=mymysql)
2016-07-11T00:58:07.965128417+08:00 container create a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
2016-07-11T00:58:08.188734598+08:00 container start a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
2016-07-11T00:58:20.010876777+08:00 container top a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
2016-07-11T01:06:01.395365098+08:00 container top a404c6c174a21c52f199cfce476e041074ab020453c7df2a13a7869b48f2f37e (image=mysql:5.6, name=mymysql)
```

- [logs](https://www.runoob.com/docker/docker-logs-command.html)获取容器的日志

```bash
语法
docker logs [OPTIONS] CONTAINER
OPTIONS说明：
-f : 跟踪日志输出
--since :显示某个开始时间的所有日志
-t : 显示时间戳
--tail :仅列出最新N条容器日志
实例
跟踪查看容器mynginx的日志输出。
runoob@runoob:~$ docker logs -f mynginx
192.168.239.1 - - [10/Jul/2016:16:53:33 +0000] "GET / HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36" "-"
2016/07/10 16:53:33 [error] 5#5: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.239.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "192.168.239.130", referrer: "http://192.168.239.130/"
192.168.239.1 - - [10/Jul/2016:16:53:33 +0000] "GET /favicon.ico HTTP/1.1" 404 571 "http://192.168.239.130/" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36" "-"
192.168.239.1 - - [10/Jul/2016:16:53:59 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36" "-"
...

查看容器mynginx从2016年7月1日后的最新10条日志。
docker logs --since="2016-07-01" --tail=10 mynginx
```

- [wait](https://www.runoob.com/docker/docker-wait-command.html)阻塞运行直到容器停止，然后打印出它的退出代码。

```bash
语法
docker wait [OPTIONS] CONTAINER [CONTAINER...]
实例
docker wait CONTAINER
```

- [export](https://www.runoob.com/docker/docker-export-command.html)将文件系统作为一个tar归档文件导出到STDOUT

```bash
语法
docker export [OPTIONS] CONTAINER
OPTIONS说明：
-o :将输入内容写到文件。
实例
将id为a404c6c174a2的容器按日期保存为tar文件。
runoob@runoob:~$ docker export -o mysql-`date +%Y%m%d`.tar a404c6c174a2
runoob@runoob:~$ ls mysql-`date +%Y%m%d`.tar
mysql-20160711.tar
```

- [port](https://www.runoob.com/docker/docker-port-command.html)列出指定的容器的端口映射，或者查找将PRIVATE_PORT NAT到面向公众的端口

```bash
语法
docker port [OPTIONS] CONTAINER [PRIVATE_PORT[/PROTO]]
实例
查看容器mynginx的端口映射情况。
runoob@runoob:~$ docker port mymysql
3306/tcp -> 0.0.0.0:3306
```

### 容器rootfs命令

- [commit](https://www.runoob.com/docker/docker-commit-command.html)从容器创建一个新的镜像

```bash
语法
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
OPTIONS说明：
-a :提交的镜像作者；

-c :使用Dockerfile指令来创建镜像；

-m :提交时的说明文字；

-p :在commit时，将容器暂停。

实例
将容器a404c6c174a2 保存为新的镜像,并添加提交人信息和说明信息。
runoob@runoob:~$ docker commit -a "runoob.com" -m "my apache" a404c6c174a2  mymysql:v1 
sha256:37af1236adef1544e8886be23010b66577647a40bc02c0885a6600b33ee28057
runoob@runoob:~$ docker images mymysql:v1
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mymysql             v1                  37af1236adef        15 seconds ago      329 MB
```

- [cp](https://www.runoob.com/docker/docker-cp-command.html) 用于容器与主机之间的数据拷贝

```bash
语法
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
OPTIONS说明：
-L :保持源目标中的链接
实例
将主机/www/runoob目录拷贝到容器96f7f14e99ab的/www目录下。
docker cp /www/runoob 96f7f14e99ab:/www/
将主机/www/runoob目录拷贝到容器96f7f14e99ab中，目录重命名为www。
docker cp /www/runoob 96f7f14e99ab:/www
将容器96f7f14e99ab的/www目录拷贝到主机的/tmp目录中。
docker cp  96f7f14e99ab:/www /tmp/
```

- [diff](https://www.runoob.com/docker/docker-diff-command.html)检查容器里文件结构的更改

```bash
语法
docker diff [OPTIONS] CONTAINER
实例
查看容器mymysql的文件结构更改。
runoob@runoob:~$ docker diff mymysql
A /logs
A /mysql_data
C /run
C /run/mysqld
A /run/mysqld/mysqld.pid
A /run/mysqld/mysqld.sock
C /tmp
```

### 镜像仓库

- [login](https://www.runoob.com/docker/docker-login-command.html)登陆到一个Docker镜像仓库

```bash
docker login : 登陆到一个Docker镜像仓库，如果未指定镜像仓库地址，默认为官方仓库 Docker Hub
docker logout : 登出一个Docker镜像仓库，如果未指定镜像仓库地址，默认为官方仓库 Docker Hub
语法
docker login [OPTIONS] [SERVER]
docker logout [OPTIONS] [SERVER]
OPTIONS说明：
-u :登陆的用户名
-p :登陆的密码
实例
登陆到Docker Hub
docker login -u 用户名 -p 密码
登出Docker Hub
docker logout
```

- [pull](https://www.runoob.com/docker/docker-pull-command.html)从镜像仓库中拉取或者更新指定镜像

```bash
语法
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
OPTIONS说明：
-a :拉取所有 tagged 镜像

--disable-content-trust :忽略镜像的校验,默认开启

实例
从Docker Hub下载java最新版镜像。
docker pull java
从Docker Hub下载REPOSITORY为java的所有镜像。
docker pull -a java
```

- [push](https://www.runoob.com/docker/docker-push-command.html)将本地的镜像上传到镜像仓库,要先登陆到镜像仓库

```bash
语法
docker push [OPTIONS] NAME[:TAG]
OPTIONS说明：
--disable-content-trust :忽略镜像的校验,默认开启
实例
上传本地镜像myapache:v1到镜像仓库中。
docker push myapache:v1
```

- [search](https://www.runoob.com/docker/docker-search-command.html)从Docker Hub查找镜像

```bash
语法
docker search [OPTIONS] TERM
OPTIONS说明：
--automated :只列出 automated build类型的镜像；
--no-trunc :显示完整的镜像描述；
-s :列出收藏数不小于指定值的镜像。
实例
从Docker Hub查找所有镜像名包含java，并且收藏数大于10的镜像
runoob@runoob:~$ docker search -s 10 java
NAME                  DESCRIPTION                           STARS   OFFICIAL   AUTOMATED
java                  Java is a concurrent, class-based...   1037    [OK]       
anapsix/alpine-java   Oracle Java 8 (and 7) with GLIBC ...   115                [OK]
develar/java                                                 46                 [OK]
isuper/java-oracle    This repository contains all java...   38                 [OK]
lwieske/java-8        Oracle Java 8 Container - Full + ...   27                 [OK]
nimmis/java-centos    This is docker images of CentOS 7...   13                 [OK]
```

### 本地镜像管理

- [images](https://www.runoob.com/docker/docker-images-command.html) 列出本地镜像

```bash
语法
docker images [OPTIONS] [REPOSITORY[:TAG]]
OPTIONS说明：
-a :列出本地所有的镜像（含中间映像层，默认情况下，过滤掉中间映像层）；

--digests :显示镜像的摘要信息；

-f :显示满足条件的镜像；

--format :指定返回值的模板文件；

--no-trunc :显示完整的镜像信息；

-q :只显示镜像ID。

实例
查看本地镜像列表。
runoob@runoob:~$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
mymysql                 v1                  37af1236adef        5 minutes ago       329 MB
runoob/ubuntu           v4                  1c06aa18edee        2 days ago          142.1 MB
<none>                  <none>              5c6e1090e771        2 days ago          165.9 MB
httpd                   latest              ed38aaffef30        11 days ago         195.1 MB
alpine                  latest              4e38e38c8ce0        2 weeks ago         4.799 MB
mongo                   3.2                 282fd552add6        3 weeks ago         336.1 MB
redis                   latest              4465e4bcad80        3 weeks ago         185.7 MB
php                     5.6-fpm             025041cd3aa5        3 weeks ago         456.3 MB
python                  3.5                 045767ddf24a        3 weeks ago         684.1 MB
...
列出本地镜像中REPOSITORY为ubuntu的镜像列表。
root@runoob:~# docker images  ubuntu
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              14.04               90d5884b1ee0        9 weeks ago         188 MB
ubuntu              15.10               4e3b13c8a266        3 months ago        136.3 MB
```

- [rmi](https://www.runoob.com/docker/docker-rmi-command.html) 删除本地一个或多少镜像

```bash
语法
docker rmi [OPTIONS] IMAGE [IMAGE...]
OPTIONS说明：
-f :强制删除；

--no-prune :不移除该镜像的过程镜像，默认移除；

实例
强制删除本地镜像runoob/ubuntu:v4。
root@runoob:~# docker rmi -f runoob/ubuntu:v4
Untagged: runoob/ubuntu:v4
Deleted: sha256:1c06aa18edee44230f93a90a7d88139235de12cd4c089d41eed8419b503072be
Deleted: sha256:85feb446e89a28d58ee7d80ea5ce367eebb7cec70f0ec18aa4faa874cbd97c73
```

- [tag](https://www.runoob.com/docker/docker-tag-command.html)标记本地镜像，将其归入某一仓库

```bash
语法
docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
实例
将镜像ubuntu:15.10标记为 runoob/ubuntu:v3 镜像。
root@runoob:~# docker tag ubuntu:15.10 runoob/ubuntu:v3
root@runoob:~# docker images   runoob/ubuntu:v3
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
runoob/ubuntu       v3                  4e3b13c8a266        3 months ago        136.3 MB

```

- [build](https://www.runoob.com/docker/docker-build-command.html) 命令用于使用 Dockerfile 创建镜像

```bash
语法
docker build [OPTIONS] PATH | URL | -
OPTIONS说明：
--build-arg=[] :设置镜像创建时的变量；
--cpu-shares :设置 cpu 使用权重；
--cpu-period :限制 CPU CFS周期；
--cpu-quota :限制 CPU CFS配额；
--cpuset-cpus :指定使用的CPU id；
--cpuset-mems :指定使用的内存 id；
--disable-content-trust :忽略校验，默认开启；
-f :指定要使用的Dockerfile路径；
--force-rm :设置镜像过程中删除中间容器；
--isolation :使用容器隔离技术；
--label=[] :设置镜像使用的元数据；
-m :设置内存最大值；
--memory-swap :设置Swap的最大值为内存+swap，"-1"表示不限swap；
--no-cache :创建镜像的过程不使用缓存；
--pull :尝试去更新镜像的新版本；
--quiet, -q :安静模式，成功后只输出镜像 ID；
--rm :设置镜像成功后删除中间容器；
--shm-size :设置/dev/shm的大小，默认值是64M；
--ulimit :Ulimit配置。
--tag, -t: 镜像的名字及标签，通常 name:tag 或者 name 格式；可以在一次构建中为一个镜像设置多个标签。
--network: 默认 default。在构建期间设置RUN指令的网络模式
实例
使用当前目录的 Dockerfile 创建镜像，标签为 runoob/ubuntu:v1。
docker build -t runoob/ubuntu:v1 . 
使用URL github.com/creack/docker-firefox 的 Dockerfile 创建镜像。 
docker build github.com/creack/docker-firefox
也可以通过 -f Dockerfile 文件的位置：
$ docker build -f /path/to/a/Dockerfile .
在 Docker 守护进程执行 Dockerfile 中的指令前，首先会对 Dockerfile 进行语法检查，有语法错误时会返回：
$ docker build -t test/myapp .
Sending build context to Docker daemon 2.048 kB
Error response from daemon: Unknown instruction: RUNCMD

```

- [history](https://www.runoob.com/docker/docker-history-command.html)看指定镜像的创建历史

```bash
语法
docker history [OPTIONS] IMAGE
OPTIONS说明：
-H :以可读的格式打印镜像大小和日期，默认为true；

--no-trunc :显示完整的提交记录；

-q :仅列出提交记录ID。


```

实例
查看本地镜像runoob/ubuntu:v3的创建历史。

```bash
root@runoob:~# docker history runoob/ubuntu:v3
IMAGE             CREATED           CREATED BY                                      SIZE      COMMENT
4e3b13c8a266      3 months ago      /bin/sh -c #(nop) CMD ["/bin/bash"]             0 B                 
<missing>         3 months ago      /bin/sh -c sed -i 's/^#\s*\(deb.*universe\)$/   1.863 kB            
<missing>         3 months ago      /bin/sh -c set -xe   && echo '#!/bin/sh' > /u   701 B               
<missing>         3 months ago      /bin/sh -c #(nop) ADD file:43cb048516c6b80f22   136.3 MB
```

- [save](https://www.runoob.com/docker/docker-save-command.html)将指定镜像保存成 tar 归档文件

```bash
语法
docker save [OPTIONS] IMAGE [IMAGE...]
OPTIONS说明：
-o :输出到的文件。

实例
将镜像runoob/ubuntu:v3 生成my_ubuntu_v3.tar文档
runoob@runoob:~$ docker save -o my_ubuntu_v3.tar runoob/ubuntu:v3
runoob@runoob:~$ ll my_ubuntu_v3.tar
-rw------- 1 runoob runoob 142102016 Jul 11 01:37 my_ubuntu_v3.ta

```

- [load](https://www.runoob.com/docker/docker-load-command.html)





- [import](https://www.runoob.com/docker/docker-import-command.html)从归档文件中创建镜像

```bash
语法
docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
OPTIONS说明：
-c :应用docker 指令创建镜像；
-m :提交时的说明文字；

实例
从镜像归档文件my_ubuntu_v3.tar创建镜像，命名为runoob/ubuntu:v4
runoob@runoob:~$ docker import  my_ubuntu_v3.tar runoob/ubuntu:v4  
sha256:63ce4a6d6bc3fabb95dbd6c561404a309b7bdfc4e21c1d59fe9fe4299cbfea39
runoob@runoob:~$ docker images runoob/ubuntu:v4
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
runoob/ubuntu       v4                  63ce4a6d6bc3        20 seconds ago      142.1 MB

```

### info|version

- [info](https://www.runoob.com/docker/docker-info-command.html) 显示 Docker 系统信息，包括镜像和容器数

语法

```bash
docker info [OPTIONS]
```

实例
查看docker系统信息。

```bash
$ docker info
Containers: 12
Images: 41
Storage Driver: aufs
 Root Dir: /var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 66
 Dirperm1 Supported: false
Execution Driver: native-0.2
Logging Driver: json-file
Kernel Version: 3.13.0-32-generic
Operating System: Ubuntu 14.04.1 LTS
CPUs: 1
Total Memory: 1.954 GiB
Name: iZ23mtq8bs1Z
ID: M5N4:K6WN:PUNC:73ZN:AONJ:AUHL:KSYH:2JPI:CH3K:O4MK:6OCX:5OYW
```

- [version](https://www.runoob.com/docker/docker-version-command.html)

语法

```bash
docker version [OPTIONS]
OPTIONS说明：
-f :指定返回值的模板文件。
```

实例
显示 Docker 版本信息。

```bash
$ docker version
Client:
 Version:      1.8.2
 API version:  1.20
 Go version:   go1.4.2
 Git commit:   0a8c2e3
 Built:        Thu Sep 10 19:19:00 UTC 2015
 OS/Arch:      linux/amd64

Server:
 Version:      1.8.2
 API version:  1.20
 Go version:   go1.4.2
 Git commit:   0a8c2e3
 Built:        Thu Sep 10 19:19:00 UTC 2015
 OS/Arch:      linux/amd64
```

