[dockerfile详解_紫色飞猪-CSDN博客_dockerfile](https://blog.csdn.net/zisefeizhu/article/details/83472190)

Dockerfile制作完成后，用命令build制作基于dockerfile的新镜像

```dockerfile
[root@node1 img1]# docker build  -t tinyhttpd:v0.1-1 ./
Sending build context to Docker daemon  3.072kB
Step 1/3 : FROM busybox:latest                                       //FROM
 ---> 59788edf1f3e
Step 2/3 : MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"      //MAINTAINER
 ---> Using cache
 ---> e0a3a7c1de10
Step 3/3 : COPY index.html /data/web/html/                           //COPY
 ---> 35c00f8b6408 
Successfully built 35c00f8b6408
Successfully tagged tinyhttpd:v0.1-1
[root@node1 img1]# docker image ls            //查看新生成的镜像
REPOSITORY                                          TAG                 IMAGE ID            CREATED             SIZE
tinyhttpd                                           v0.1-1              35c00f8b6408        9 seconds ago       1.15MB
//启动新生成的镜像，在容器内部有目录/data/web/html/，并且有文件index.html
[root@node1 ~]# docker run --name tinyweb1 --rm tinyhttpd:v0.1-1 cat /data/web/html/index.html
<h1>zhujingxing </h1>
```

COPY目录

```dockerfile
[root@node1 img1]# cp -r /etc/yum.repos.d/ ./
[root@node1 img1]# ls 
Dockerfile  index.html  yum.repos.d
[root@node1 img1]# ls yum.repos.d/
CentOS-Base.repo  CentOS-Debuginfo.repo  CentOS-Media.repo    CentOS-Vault.repo  docker-ce.repo.cp
CentOS-CR.repo    CentOS-fasttrack.repo  CentOS-Sources.repo  docker-ce.repo     epel.repo
[root@node1 img1]# vim Dockerfile 
# Description: test image
FROM busybox:latest
MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"
#LABEL maintainer="zisefeizhu <zisefeizhu@zhujingxing.com>"
COPY index.html /data/web/html/
COPY yum.repos.d /etc/yum.repos.d/
[root@node1 img1]# docker build  -t tinyhttpd:v0.1-2 ./
Sending build context to Docker daemon  28.67kB
Step 1/4 : FROM busybox:latest
 ---> 59788edf1f3e
Step 2/4 : MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"
 ---> Using cache
 ---> e0a3a7c1de10
Step 3/4 : COPY index.html /data/web/html/
 ---> Using cache
 ---> 35c00f8b6408
Step 4/4 : COPY yum.repos.d /etc/yum.repos.d/
 ---> 6250436df8e7
Successfully built 6250436df8e7
Successfully tagged tinyhttpd:v0.1-2

[root@node1 ~]# docker run --name tinyweb1 --rm tinyhttpd:v0.1-2 ls /etc/yum.repos.d/
CentOS-Base.repo
CentOS-CR.repo
CentOS-Debuginfo.repo
CentOS-Media.repo
CentOS-Sources.repo
CentOS-Vault.repo
CentOS-fasttrack.repo
docker-ce.repo
docker-ce.repo.cp
epel.repo
```

ADD 

ADD指令类似于 COPY指令， ADD支持使用 TAR文件和 URL路径

语法

```dockerfile
. ADD <src> ... <dest>或

. ADD ["<src>",... "<dest>"]
```

.操作准则 .

同COPY指令的4点准则

 如果<src>为URL且<dest>不以/结尾，则<src>指定的文件将被下载并直接被创建为<dest>；如果<dest>以/结尾，则文件名URL指定的文件将被直接下载，并保存为<dest>/<filename>，注意，URL不能是ftp格式的url

如果<src>是一个本地系统上的压缩格式的tar文件，它将被展开为一个目录，其行为类似于“tar -x”命令，然后，通过URL获取到的tar文件将不会自动展开

如果<src>有多个，或其间接或直接使用了通配符，则<dest>必须是一个以/结尾的目录路径；如果<dest>不以/结尾，则其被视作一个普通文件，<src>的内容将被直接写入到<dest>；

***例子\***

```dockerfile
[root@node1 img1]# vim Dockerfile 
ADD http://nginx.org/download/nginx-1.15.5.tar.gz /usr/local/src/

[root@node1 img1]# docker build  -t tinyhttpd:v0.1-3 ./
Step 5/5 : ADD http://nginx.org/download/nginx-1.15.5.tar.gz /usr/local/src/
Downloading  1.025MB/1.025MB
 ---> 77406c81872f
Successfully built 77406c81872f
Successfully tagged tinyhttpd:v0.1-3

[root@node1 ~]# docker run --name tinyweb1 --rm tinyhttpd:v0.1-3 ls /usr/local/src
nginx-1.15.5.tar.gz

[root@node1 img1]# wget http://nginx.org/download/nginx-1.15.5.tar.gz

[root@node1 img1]# vim Dockerfile 
ADD nginx-1.15.5.tar.gz /usr/local/src/
[root@node1 img1]# docker build  -t tinyhttpd:v0.1-4 ./
Step 5/5 : ADD nginx-1.15.5.tar.gz /usr/local/src/
 ---> ff39a60ceccb
Successfully built ff39a60ceccb
Successfully tagged tinyhttpd:v0.1-4
[root@node1 ~]# docker run --name tinyweb1 --rm tinyhttpd:v0.1-4 ls /usr/local/src
nginx-1.15.5
```

**WORKDIR**

workdir为工作目录，指当前容器环境的工作目录，用于为 Dockerfile中所有的 RUN、CMD、ENTRYPOINT、COPY和 ADD指定设定工作目录

语法

```dockerfile
WORKDIR  <dirpath>

在Dockerfile文件中， WORKDIR指令可出现多次，其路径也可以为相对路径，不过，其是相对此前一个 WORKDIR指令指定的路径

另外， WORKDIR也可调用由 ENV指定定义的变量 .例如

WORKDIR /var/log

WORKDIR  $STATEPATH
```

例子

指定workdir为/usr/local，相当于是容器启动后，会把工作目录切换到/usr/local这个workdir路径下，而不是默认的根目录，如下例子，则相对路径 ./src/ 的绝对路径为容器的/usr/local/src，制作镜像时，把nginx包拷贝到/usr/local/src，把tomcat包解压到/usr/local/src下面

```dockerfile
[root@node1 img1]# vim Dockerfile

FROM busybox:1.27.2

MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"

WORKDIR "/usr/local"

ADD http://nginx.org/download/nginx-1.14.0.tar.gz  ./src/

ADD apache-tomcat-8.0.47.tar.gz ./
```

启动容器并检查

```dockerfile
[root@node1 img1]# docker run -it --rm --name testworkdir testworkdir:v1

/usr/local # ls

apache-tomcat-8.0.47  src

/usr/local # ls src

nginx-1.14.0.tar.gz

/usr/local #

容器启动后，工作路径直接切换为/usr/local
```

VOLUME

定义卷，只能是docker管理的卷，VOLUME为容器上的目录，用于在 image中创建一个挂载点目录，以挂载 Docker host上的卷或其它容器上的卷

语法

```dockerfile
. VOLUME <mountpoint>或

. VOLUME ["<mountpoint>"]
```

如果挂载点目录路径下此前在文件存在， docker run命令会在卷挂载完成后将此前的所有文件复制到新挂载的卷中

例子

```dockerfile
[root@node1 ~]# vim img1/Dockerfile 
#ADD http://nginx.org/download/nginx-1.15.5.tar.gz /usr/local/src/
WORKDIR /usr/locl/
ADD nginx-1.15.5.tar.gz ./src
VOLUME /data/mysql/

[root@node1 img1]# docker build  -t tinyhttpd:v0.1-5 ./
Step 5/7 : WORKDIR /usr/locl/
 ---> Running in 08a4d481c0f9
Removing intermediate container 08a4d481c0f9
 ---> b9246b4e4f2b
Step 6/7 : ADD nginx-1.15.5.tar.gz ./src
 ---> b5e78864d438
Step 7/7 : VOLUME /data/mysql/
 ---> Running in afbc37ddff3e
Removing intermediate container afbc37ddff3e
 ---> e6cbde99a92d
```

查看法一：

```bash
[root@node1 ~]# docker run --name tinyweb1 --rm tinyhttpd:v0.1-5 mount 

/dev/sda3 on /data/mysql type xfs (rw,seclabel,relatime,attr2,inode64,noquota)
```

查看法二：

```bash
[root@node1 ~]# docker run --name tinyweb1 --rm tinyhttpd:v0.1-5 sleep 60

[root@node1 img1]# docker inspect tinyweb1

"Mounts": [
            {
                "Destination": "/data/mysql",
            }
        ],
```

EXPOSE

暴露指定端口，用于为容器打开指定要监听的端口以实现与外部通信

语法

```dockerfile
EXPOSE <port>[/<protocol>] [<port>[/<protocol>] ...] l

其中<protocol>用于指定传输层协议，可为 tcp或udp二者之一，默认为 TCP协议

EXPOSE指令可一次指定多个端口，但是不能指定暴露为宿主机的指定端口，因为指定的宿主机端口可能已经被占用，因此这里使用随机端口，例如

. EXPOSE 11211/udp 11211/tcp
```

***例子：\***

```dockerfile
[root@node1 img1]# vim Dockerfile 
EXPOSE 80/tcp
[root@node1 ~]# docker run --name tinyweb1 --rm tinyhttpd:v0.1-6 /bin/httpd -f -h /data/web/html

[root@node1 ~]# docker inspect tinyweb1                                                                                                                                         "IPAddress": "172.17.0.2",  

[root@node1 ~]# curl 172.17.0.2
<h1>zhujingxing </h1>
[root@node1 ~]# docker port tinyweb1   //没有端口信息   即没有正真暴露出来

启动并暴露端口，注意，启动容器要跟大写P选项-P来暴露

[root@node1 ~]# docker run --name tinyweb1 --rm -P  tinyhttpd:v0.1-6 /bin/httpd -f -h /data/web/html

[root@node1 ~]# curl 172.17.0.2
<h1>zhujingxing </h1>
[root@node1 ~]# docker port tinyweb1
80/tcp -> 0.0.0.0:32768
```

ENV

ENV用于为镜像定义所需的环境变量，并可被 Dockerfile文件中位于其后的其它指令（如 ENV、ADD、COPY等）所调用 ，即先定义后调用

调用格式为 $variable_name或${variable_name}

语法

```dockerfile
ENV <key> <value>或 . ENV <key>=<value> ... .

第一种格式中， <key>之后的所有内容均会被视作其 <value>的组成部分，因此一次只能设置一个变量

第二种格式，可用一次设置多个变量，每个变量为一个“<key>=<value>”的键值对，如果<value>包含空格，可以以反斜线（\）进行转义，也可通过对<value>加引号进行标识；另外反斜线也可以用于续行；

.定义多个变量时，建议使用第二种方式，以便在同一层中完成所有功能
```

***例子***

```dockerfile
[root@node1 img1]# cat Dockerfile 

#ENV  DOC_ROOt=/data/web/html/    单个文件 
ENV  DOC_ROOt=/data/web/html/ \     多个文件
     WEB_SERVER_PACKAGE="nginx-1.15.5"

COPY index.html ${DOC_ROOT:-/data/web/html/}
COPY yum.repos.d /etc/yum.repos.d/
#ADD http://nginx.org/download/nginx-1.15.5.tar.gz /usr/local/src/
WORKDIR /usr/locl/
ADD ${WEB_SERVER_PACKAGE}.tar.gz ./src/
```

创建镜像

```dockerfile

[root@node1 img1]# docker build  -t tinyhttpd:v0.1-7 ./
Sending build context to Docker daemon  1.054MB
Step 1/9 : FROM busybox:latest
 ---> 59788edf1f3e
Step 2/9 : MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"
 ---> Using cache
 ---> e0a3a7c1de10
Step 3/9 : ENV  DOC_ROOt=/data/web/html/      WEB_SERVER_PACKAGE="nginx-1.15.5"
 ---> Using cache
 ---> 61cc545b9111
Step 4/9 : COPY index.html ${DOC_ROOT:-/data/web/html/}
 ---> Using cache
 ---> a962e0fa3d54
Step 5/9 : COPY yum.repos.d /etc/yum.repos.d/
 ---> Using cache
 ---> c6e3e674f856
Step 6/9 : WORKDIR /usr/locl/
 ---> Using cache
 ---> b2574695b705
Step 7/9 : ADD ${WEB_SERVER_PACKAGE}.tar.gz ./src/
 ---> Using cache
 ---> fbf4219523dc
Step 8/9 : VOLUME /data/mysql/
 ---> Using cache
 ---> cbe2f8c57722
Step 9/9 : EXPOSE 80/tcp
 ---> Using cache
 ---> 3edf30b6f3d3
Successfully built 3edf30b6f3d3
Successfully tagged tinyhttpd:v0.1-7
```

运行容器验证

```dockerfile
[root@node1 ~]# docker run -it --name tinyweb1 --rm -P  tinyhttpd:v0.1-7
/usr/locl # ls 
src
/usr/locl # cd src/
/usr/locl/src # ls
nginx-1.15.5
/usr/locl/src # exit
[root@node1 ~]# docker run --name tinyweb1 --rm -P  tinyhttpd:v0.1-7 ls /data/web/html
index.html
有些变量在运行为容器时依然有用，因此需要把那些变量在运行为容器时重新定义为一个新的值，如果变量很多，可以放到一个文件中进行定义，使用参数 --env-list(docker run --help )实现，通过文件来加载环境变量

[root@node1 ~]# docker run --name tinyweb1 --rm -P  tinyhttpd:v0.1-7 printenv
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=39efa2eeac77
DOC_ROOt=/data/web/html/
WEB_SERVER_PACKAGE=nginx-1.15.5
HOME=/root


[root@node1 ~]# docker run --name tinyweb1 --rm -P -e WEB_SERVER_PACKAGE="nginx-1.15-6" tinyhttpd:v0.1-7 printenv
WEB_SERVER_PACKAGE=nginx-1.15-6
DOC_ROOt=/data/web/html/
HOME=/root
[root@node1 ~]# docker run --name tinyweb1 --rm -P -e WEB_SERVER_PACKAGE="nginx-1.15-6" tinyhttpd:v0.1-7 printenv && ls /usr/local/src
WEB_SERVER_PACKAGE=nginx-1.15-6
DOC_ROOt=/data/web/html/
HOME=/root

```

RUN

RUN用于指定 docker build过程中运行的程序，其可以是任何命令，但是这里有个限定，一般为基础镜像可以运行的命令，如基础镜像为centos，安装软件命令为yum而不是ubuntu里的apt-get命令

RUN和CMD都可以改变容器运行的命令程序，但是运行的时间节点有区别，RUN表示在docker build运行的命令，而CMD是将镜像启动为容器运行的命令。因为一个容器正常只用来运行一个程序，因此CMD一般只有一条命令，如果CMD配置多个，则只有最后一条命令生效。而RUN可以有多个。

语法

```dockerfile
RUN <command>或 . RUN ["<executable>", "<param1>", "<param2>"]
```

第一种格式中，<command>通常是一个shell命令，且以“/bin/sh -c”作为父进程来运行它，这意味着此进程在容器中的PID不为1，不能接收Unix信号，因此，当使用 docker stop <container>命令停止容器时，此进程接收不到SIGTERM信号；

第二种语法格式中的参数是一个JSON格式的数组，其中<executable>为要运行的命令，后面的<paramN>为传递给命令的选项或参数；然而，此种格式指定的命令不会以“/bin/sh -c”来发起，表示这种命令在容器中直接运行，不会作为shell的子进程，因此常见的shell操作如变量替换以及通配符（？，*等）替换将不会进行，不过，如果要运行的没能力依赖此shell特性的话，可以将其替换为类似下面的格式

注意:json数组中使用双引号

```dockerfile
RUN ["/bin/bash","-C","<executable>","<paraml>"]
```

例子

把下载的nginx打包文件，用RUN命令来展开

编辑dockerfile

```dockerfile
[root@node1 img1]# vim Dockerfile 

# Description: test image

FROM busybox:latest
MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"
#LABEL maintainer="zisefeizhu <zisefeizhu@zhujingxing.com>"
ENV  DOC_ROOt=/data/web/html/ \
     WEB_SERVER_PACKAGE="nginx-1.15.5.tar.gz"

COPY index.html ${DOC_ROOT:-/data/web/html/}
COPY yum.repos.d /etc/yum.repos.d/
ADD http://nginx.org/download/${WEB_SERVER_PACKAGE} /usr/local/src/
WORKDIR /usr/local/
#ADD ${WEB_SERVER_PACKAGE}.tar.gz ./src/
VOLUME /data/mysql/
EXPOSE 80/tcp
RUN cd /usr/local/src && \
    tar xf ${WEB_SERVER_PACKAGE}
```

创建镜像

```dockerfile
[root@node1 img1]# docker build  -t tinyhttpd:v0.1-9 ./
```

运行容器并验证

```dockerfile
[root@node1 ~]# docker run --name tinyweb1 --rm -P -e WEB_SERVER_PACKAGE="nginx-1.15-6" -it tinyhttpd:v0.1-9 ls /usr/local/src 
nginx-1.15.5         nginx-1.15.5.tar.gz
```

如果RUN的命令很多，就用&&符号连接多个命令，少构建镜像层，提高容器的效率

例子如下

基础镜像为centos,RUN多个命令

由于安装是到互联网上的仓库进行安装，所以，建议把centos的yum源配置为本地，即创建镜像时，把yum的配置有本地仓库源配置在CentOS-Base.repo文件放在imp1下面，配置文件配置ADD拷贝一份到新建镜像的/etc/yum.repos.d目录下，因为经常默认会优先加载CentOS-Base.repo下的包，但是不建议使用这个方法，除非本地仓库有足够的包解决依赖关系，否则建议仅使用默认的即可

编辑dockerfile

```dockerfile
[root@node1 img1]# vim Dockerfile

FROM centos:7.3.1611

MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"

ENV nginx_ver=1.14.0

ENV nginx_url=http://nginx.org/download/nginx-${nginx_ver}.tar.gz

WORKDIR "/usr/local/src"

ADD CentOS-Base.repo  /etc/yum.repos.d/

ADD ${nginx_url} /usr/local/src/

RUN tar xf nginx-${nginx_ver}.tar.gz && \
    yum -y install gcc pcre-devel openssl-devel make &&  \

    cd nginx-${nginx_ver} && \

    ./configure && make && make install
```



创建镜像

```dockerfile
[root@node1 img1]# docker build -t nginx:v1 ./
```

运行容器，启动nginx进程

```dockerfile
[root@node1 img1]# docker run -it --rm --name nginxv1 nginx:v1

[root@ccedfdf5e63f src]# /usr/local/nginx/sbin/nginx
```

此时，nginx进程运行于后台，不建议这么做，因为容器的进程要运行于前台模式，否则容器会终止，nginx运行于前台，需要在nginx的配置文件nginx.conf里添加配置项

```dockerfile
vi /usr/local/nginx/conf/nginx.conf

daemon off；
```

这样使得nginx运行于前台

再次运行nginx，则运行于前台

或者通过-g选项，在运行nginx的全局配置模式之后再运行某些参数，注意off后面的冒号

```dockerfile
[root@ccedfdf5e63f local]# /usr/local/nginx/sbin/nginx -g "daemon off;"
```

CMD 

类似于 RUN指令， CMD指令也可用于运行任何命令或应用程序，不过，二者的运行时间点不同 . RUN指令运行于映像文件构建过程中，而 CMD指令运行于基于 Dockerfile构建出的新映像文件启动一个容器时 . CMD指令的首要目的在于为启动的容器指定默认要运行的程序，且其运行结束后，容器也将终止；不过， CMD指定的命令其可以被 docker run的命令行选项所覆盖 .在Dockerfile中可以存在多个 CMD指令，但仅最后一个会生效

语法

```dockerfile
CMD <command>或

CMD ["<executable>","<param1>","<param2>"]或

CMD["<param1>","<param2>"]
```

.前两种语法格式的意义同 RUN

.第三种则用于为 ENTRYPOINT指令提供默认参数

例子

一：

```dockerfile
[root@node1 img1]# mkdir ~/img2
[root@node1 ~]# cd img2
[root@node1 img2]# vim Dockerfile
FROM busybox
LABEL maintainer="zhujingxing <zisefeizhu@zhujingxing.com>" app="httpd"
ENV WEB_DOC_ROOT="/data/web/html/"
RUN mkdir -p  $WEB_DOC_ROOT && \
    echo '<h1> zhujingxing</h1>' > ${WEB_DOC_ROOT}/index.html
CMD /bin/httpd -f -h ${WEB_DOC_ROOT}
[root@node1 img2]# docker build  -t tinyhttpd:v0.2-1 ./
[root@node1 img2]# docker image inspect tinyhttpd:v0.2-1
      "Cmd": [
            "/bin/sh",
            "-c",
            "/bin/httpd -f -h ${WEB_DOC_ROOT}"
        ],
[root@node1 ~]# docker run --name tinyweb2 -it --rm -P tinyhttpd:v0.2-1    //卡到这里不动了

root@node1 ~]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
ea15f4a3623d        tinyhttpd:v0.2-1    "/bin/sh -c '/bin/ht…"   26 seconds ago      Up 25 seconds                           tinyweb2
[root@node1 ~]# docker exec -it tinyweb2 /bin/sh     //exec 还可以登进去
/ # ps 
PID   USER     TIME  COMMAND
    1 root      0:00 /bin/httpd -f -h /data/web/html/
    6 root      0:00 /bin/sh
   11 root      0:00 ps
/ # printenv
WEB_DOC_ROOT=/data/web/html/
HOSTNAME=ea15f4a3623d
SHLVL=1
HOME=/root
TERM=xterm
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PWD=/
/ # exit
```


二:

```dockerfile
[root@node1 img2]# vim Dockerfile 
FROM busybox
LABEL maintainer="zhujingxing <zisefeizhu@zhujingxing.com>" app="httpd"
ENV WEB_DOC_ROOT="/data/web/html/"
RUN mkdir -p  $WEB_DOC_ROOT && \
    echo '<h1> zhujingxing</h1>' > ${WEB_DOC_ROOT}/index.html
#CMD /bin/httpd -f -h ${WEB_DOC_ROOT}
CMD [ "/bin/httpd","-f","-h ${WEB_DOC_ROOT}"]      //改成json数组格式 

[root@node1 img2]# docker build  -t tinyhttpd:v0.2-2 ./

[root@node1 img2]# docker image inspect tinyhttpd:v0.2-2

"Cmd": [
                "/bin/httpd",
                "-f",
                "-h ${WEB_DOC_ROOT}"
            ],
[root@node1 ~]# docker run --name tinyweb2 -it --rm -P tinyhttpd:v0.2-2   //报错  json默认不会启动shell进程
httpd: can't change directory to ' ${WEB_DOC_ROOT}': No such file or directory
```

三

```dockerfile
[root@node1 img2]#vim Dockerfile 
FROM busybox
LABEL maintainer="zhujingxing <zisefeizhu@zhujingxing.com>" app="httpd"
ENV WEB_DOC_ROOT="/data/web/html/"
RUN mkdir -p  $WEB_DOC_ROOT && \
    echo '<h1> zhujingxing</h1>' > ${WEB_DOC_ROOT}/index.html
#CMD /bin/httpd -f -h ${WEB_DOC_ROOT}
#CMD [ "/bin/httpd","-f","-h ${WEB_DOC_ROOT}"]
CMD [ "/bin/sh","-c","/bin/httpd","-f","-h ${WEB_DOC_ROOT}"]

[root@node1 img2]# docker build  -t tinyhttpd:v0.2-3 ./

[root@node1 ~]# docker run --name tinyweb2 -it  -P tinyhttpd:v0.2-3  //没报错但直接退出终端
[root@node1 ~]# docker ps -a
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS                         PORTS               NAMES
bda42611547e        tinyhttpd:v0.2-3          "/bin/sh -c /bin/htt…"   2 seconds ago       Exited (0) 1 second ago                            tinyweb2

[root@node1 ~]# docker logs tinyweb2   //没输出，说明没有结果，可能是找不到路径
```

四

```dockerfile
[root@node1 img2]# vim Dockerfile 
FROM busybox
LABEL maintainer="zhujingxing <zisefeizhu@zhujingxing.com>" app="httpd"
ENV WEB_DOC_ROOT="/data/web/html/"
RUN mkdir -p  $WEB_DOC_ROOT && \
    echo '<h1> zhujingxing</h1>' > ${WEB_DOC_ROOT}/index.html
#CMD /bin/httpd -f -h ${WEB_DOC_ROOT}
#CMD [ "/bin/httpd","-f","-h ${WEB_DOC_ROOT}"]
#CMD [ "/bin/sh","-c","/bin/httpd","-f","-h ${WEB_DOC_ROOT}"]
CMD [ "/bin/sh","-c","/bin/httpd","-f","-h /data/web/html"]
[root@node1 img2]# docker build  -t tinyhttpd:v0.2-4 ./

[root@node1 ~]# docker rm tinyweb2
tinyweb2 
[root@node1 ~]# docker run --name tinyweb2 -it --rm -P tinyhttpd:v0.2-4    //这应该是没问题的，可能是id号导致的
```

五

编译安装nginx,并将镜像的默认命令修改为nginx启动于前台，暴露80口

编辑dockerfile

```dockerfile
vim Dockerfile

FROM centos:7.3.1611

MAINTAINER "sunny <sunny@ghbsunny.cn>"

ENV nginx_ver=1.14.0

ENV nginx_url=http://nginx.org/download/nginx-${nginx_ver}.tar.gz

WORKDIR "/usr/local/src"

EXPOSE 80/tcp

ADD ${nginx_url} /usr/local/src/RUN tar xf nginx-${nginx_ver}.tar.gz && yum -y install gcc pcre-devel openssl-devel make \

&& cd nginx-${nginx_ver} && ./configure && make && make install

CMD ["/usr/local/nginx/sbin/nginx","-g","daemon off;"]
```

制作镜像

```dockerfile
[root@node1 img2]# docker build -t nginx:v3 ./
```

启动容器并测试

```dockerfile
[root@node1 img2]# docker run -it --rm --name nginxv3 nginx:v3
```

测试，容器的ip 为 172.17.0.2，得到nginx的测试页

```dockerfile
[root@node1 yum.repos.d]# curl 172.17.0.2
```

查看容器80口被暴露为哪个口

```dockerfile
[root@node1 yum.repos.d]# docker port nginxv3

80/tcp -> 0.0.0.0:32772

[root@node1 yum.repos.d]# curl 10.0.0.210:32772
```

注意，CMD在dockerfile里写的命令，如果启动容器的命令行里执行命令，则会把dockerfile里的命令覆盖掉，如下，容器启动后，执行/bin/bash，而不是启动nginx于前台

```dockerfile
[root@node1 img2]# docker run -it --rm -P --name nginxv3 nginx:v3 /bin/bash

[root@5f2f4b930df3 src]# ss -ntlp
```

如果dockerfile指定的CMD不允许覆盖，则使用ENTRYPOINT

ENTRYPOINT

类似 CMD指令的功能，用于为容器指定默认运行程序，从而使得容器像是一个单独的可执行程序

与CMD不同的是，由 ENTRYPOINT启动的程序不会被 docker run命令行指定的参数所覆盖，而且，这些命令行参数会被当作参数传递给 ENTRYPOINT指定指定的程序 .不过， docker run命令的 --entrypoint选项的参数可覆盖ENTRYPOINT指令指定的程序

语法

```dockerfile
ENTRYPOINT <command>

ENTRYPOINT ["<excutable>","<param1>","<param2>"]
```

docker run 命令传入的命令参数会覆盖CMD指令的内容并且附加到ENTRYPOINT命令最后做为其参数使用 . Dockerfile文件中也可以存在多个 ENTRYPOINT指令，但仅有最后一个会生效

例子

```dockerfile
[root@node1 img3]# vim Dockerfile 

FROM nginx:1.14-alpine
LABEL maintainer="zhujingxing  <zisefeizhu@zhujingxing>"
ENV NGX_DOC_ROOT='/data/web/html/'
ADD index.html ${NGX_DOC_ROOT}
ADD entrypoint.sh /bin/
CMD ["/usr/sbin/nginx","-g","daemon off;"]     //注：双引号
ENTRYPOINT ["/bin/entrypoint.sh"]

[root@node1 img3]# vim entrypoint.sh 

#!/bin/sh
cat > /etc/nginx/conf.d/www.conf <<EOF
server {
        server_name $HOSTNAME;
        listen ${IP:-0.0.0.0}:${PORT:-80};
        root ${NGX_DOC_ROOT:-/usr/share/nginx/html};
}
EOF
exec "$@"

[root@node1 img3]# docker build -t myweb:v0.3-6 ./

[root@node1 img3]# docker run --name myweb1 --rm -P -e "PORT=8080" myweb:v0.3-6

[root@node1 ~]# docker exec -it myweb1 /bin/sh
/ # netstat -lnt
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      
/ # ps
PID   USER     TIME   COMMAND
    1 root       0:00 nginx: master process /usr/sbin/nginx -g daemon off;
    8 nginx      0:00 nginx: worker process
    9 root       0:00 /bin/sh
   15 root       0:00 ps
/ # wget -O - -q adf1e144ec50

<h1>zhujingxing</h1>

/ # exit
```

HEALTHCHECK:docker容器运行健康检查

语法形式:

```dockerfile
HEALTHCHECK [OPTIONS] CMD command (通过在容器中运行一个命令执行健康检查)
HEALTHCHECK NONE (禁用从基本镜像继承的任何健康检查)
```

通过HEALTHCHECK，我们可以知道如何测试一个容器查检一个它是否在工作，比如检测一个web 服务是否陷入死循环，不能处理新的连接、即使服务器进程仍在运行

当一个窗口指定了健康检查时、除了正常状态之外、还会有一个健康状态作为初始、如果检查通过、则会变成健康状态、如果经过了一定次数的连续故障、则会变成非健康状态

在CMD之前可以出现的选项如下:

```dockerfile
--interval=DURATION (default: 30s)
--timeout=DURATION (default: 30s)
--start-period=DURATION (default: 0s)
--retries=N (default: 3)
```

注：

启动周期为需要时间启动的容器提供初始化时间。 在此期间的探测失败不会计入最大重试次数。 但是，如果在启动期间运行状况检查成功，则认为容器已启动，并且所有连续的故障都将计入最大重试次数
单次运行检查花费时间超过timeout指定时间、判定失败
每个Dockerfile中只能存在一个HEALTHCHECK指令，如果有多个则最后一个起作用

HEALTHCHECK CMD后面的命令既可以是一个shell命令、也可以是一个exec 的数组

命令的退出状态显示出容器的健康状态、如下：

```dockerfile
0: success - the container is healthy and ready for use

1: unhealthy - the container is not working correctly

2: reserved(保留的) - do not use this exit code 
```

实例:每隔五分钟检查一次网络服务器是否能够在三秒钟内为该网站的主页面提供服务

```dockerfile
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1
```

为方便故障探测调试、检测命令通过stdout或者stderr输出的文本都会被缓存在健康状态中(缓存大小为4096字节)、并可以通过docker inspect查询

当容器的运行状况发生变化时，新的状态会生成一个health_status事件

成功的例子：

```dockerfile
[root@node1 img3]# cat Dockerfile 
FROM nginx:1.14-alpine
LABEL maintainer="zhujingxing  <zisefeizhu@zhujingxing>"
ENV NGX_DOC_ROOT='/data/web/html/'
ADD index.html ${NGX_DOC_ROOT}
ADD entrypoint.sh /bin/
EXPOSE 80/TCP
HEALTHCHECK --start-period=3s CMD wget -O - -q http://${IP:-0.0.0.0}:${PORT:80}/
CMD ["/usr/sbin/nginx","-g","daemon off;"]
ENTRYPOINT ["/bin/entrypoint.sh"]
[root@node1 img3]# docker build -t myweb:v0.3-7 ./
[root@node1 img3]# docker run --name myweb1 --rm -P -e "PORT=8080" myweb:v0.3-7 

[root@node1 ~]# docker exec -it myweb1 /bin/sh

/ # netstat -tnl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      
/ # wget -O

[root@node1 img3]# docker run --name myweb1 --rm -P -e "PORT=8080" myweb:v0.3-7 
127.0.0.1 - - [28/Oct/2018:13:15:35 +0000] "GET / HTTP/1.1" 200 612 "-" "Wget" "-"
127.0.0.1 - - [28/Oct/2018:13:15:43 +0000] "GET / HTTP/1.1" 200 612 "-" "Wget" "-"
```

失败的例子

```dockerfile
[root@node1 img3]# vim Dockerfile 

FROM nginx:1.14-alpine
LABEL maintainer="zhujingxing  <zisefeizhu@zhujingxing>"
ENV NGX_DOC_ROOT='/data/web/html/'
ADD index.html ${NGX_DOC_ROOT}
ADD entrypoint.sh /bin/
EXPOSE 80/TCP
HEALTHCHECK --start-period=3s CMD wget -O - -q http://${IP:-0.0.0.0}:10080/
CMD ["/usr/sbin/nginx","-g","daemon off;"]
ENTRYPOINT ["/bin/entrypoint.sh"]
[root@node1 img3]# docker build -t myweb:v0.3-8 ./

[root@node1 img3]# docker run --name myweb1 --rm -P -e "PORT=8080" myweb:v0.3-8 //三个周期默认1.5分钟后报错
[root@node1 ~]# docker exec -it myweb1 /bin/sh
/ # netstat -tnl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       
tcp        0      0 0.0.0.0:8080            0.0.0.0:*               LISTEN      
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN     
```

ARG

ARG用于指定传递给构建运行时的变量：

```dockerfile
ARG <name>[=<default value>]
```

如，通过ARG指定两个变量：

```dockerfile
ARG site
ARG build_user=IT笔录
```

以上我们指定了 site 和 build_user 两个变量，其中 build_user 指定了默认值。在使用 docker build 构建镜像时，可以通过 --build-arg <varname>=<value> 参数来指定或重设置这些变量的值。

```dockerfile
docker build --build-arg site=itiblu.com -t itbilu/test .
```

这样我们构建了 itbilu/test 镜像，其中site会被设置为 itbilu.com，由于没有指定 build_user，其值将是默认值 IT 笔录。

STOPSIGNAL

STOPSIGNAL用于设置停止容器所要发送的系统调用信号：

STOPSIGNAL signal
所使用的信号必须是内核系统调用表中的合法的值，如：SIGKILL。

SHELL

SHELL用于设置执行命令（shell式）所使用的的默认 shell 类型：

```dockerfile
SHELL ["executable", "parameters"]
```

SHELL在Windows环境下比较有用，Windows 下通常会有 cmd 和 powershell 两种 shell，可能还会有 sh。这时就可以通过 SHELL 来指定所使用的 shell 类型：

```dockerfile
FROM microsoft/windowsservercore

# Executed as cmd /S /C echo default

RUN echo default

# Executed as cmd /S /C powershell -command Write-Host default

RUN powershell -command Write-Host default

# Executed as powershell -command Write-Host hello

SHELL ["powershell", "-command"]
RUN Write-Host hello

# Executed as cmd /S /C echo hello

SHELL ["cmd", "/S"", "/C"]
RUN echo hello
```

USER

USER用于指定运行 image时的或运行 Dockerfile中任何 RUN、CMD或 ENTRYPOINT指令指定的程序时的用户名或 UID ，即改变容器中运行程序的身份

.默认情况下， container的运行身份为 root用户

语法

```dockerfile
USER  <UID>|<UserName>
```

需要注意的是， <UID>可以为任意数字，但实践中其必须为 /etc/passwd中某用户的有效 UID，否则， docker run命令将运行失败

使用USER指定用户时，可以使用用户名、UID 或 GID，或是两者的组合。以下都是合法的指定试：

```dockerfile
USER user
USER user:group
USER uid
USER uid:gid
USER user:gid
USER uid:group
```

使用USER指定用户后，Dockerfile 中其后的命令 RUN、CMD、ENTRYPOINT 都将使用该用户。镜像构建完成后，通过 docker run 运行容器时，可以通过 -u 参数来覆盖所指定的用户

ONBUILD

ONBUILD 用于在 Dockerfile中定义一个触发器 . 用来指定运行docker指令

Dockerfile用于 build映像文件，此映像文件亦可作为 base image被另一个 Dockerfile用作 FROM指令的参数，并以之构建新的映像文件

.在后面的这个 Dockerfile中的 FROM指令在 build过程中被执行时，将会 “触发 ”创建其 base image的Dockerfile文件中的 ONBUILD指令定义的触发器

语法

```dockerfile
ONBUILD <INSTRUCTION>
```

尽管任何指令都可注册成为触发器指令，但是ONBUILD不能自我嵌套，且不会触发FROM和MAINTAINER指令

使用包含ONBUILD指令的Dockerfile构建的镜像应该使用特殊的标签，例如 ruby:2.0-onbuild

在ONBUILD指令中使用ADD或COPY指令应该格外小心，因为新构建过程的上下文在缺少指定的源文件时会失败

ONBUILD 在构建镜像时不会运行，是别人基于这个镜像作为基础镜像构建时，才会运行

如下例子

增加一个ONBUILD命令，执行RUN

```dockerfile
FROM centos:7.3.1611

MAINTAINER "sunny <sunny@ghbsunny.cn>"

ENV nginx_ver=1.14.0

ENV nginx_url=http://nginx.org/download/nginx-${nginx_ver}.tar.gz

WORKDIR "/usr/local/src"

EXPOSE 80/tcp

ADD ${nginx_url} /usr/local/src/

RUN tar xf nginx-${nginx_ver}.tar.gz && yum -y install gcc pcre-devel openssl-devel make \

&& cd nginx-${nginx_ver} && ./configure && make && make install

CMD ["/usr/local/nginx/sbin/nginx","-g","daemon off;"]

ONBUILD RUN echo -e "\nSunny do an onbuild~\n" >> /etc/issue
```

构建镜像

```dockerfile
[root@node1 img4]# docker build -t nginx:v6 ./
```

基于nginx:v6启动容器,此时/etc/issue还没写入echo要插入的信息

```dockerfile
[root@node1 img4]# docker run -it --rm -P --name nginxv3 nginx:v6 /bin/bash

[root@16e90f7a6460 src]# cat /etc/issue

\S

Kernel \r on an \m

[root@16e90f7a6460 src]#
```

然后基于这个nginx:v6镜像，再次制作一个新镜像，编辑一个新的Dockerfile

```dockerfile
[root@node1r ~]# mkdir nginxv7

[root@node1 ~]# cd nginxv7/

[root@node1 nginxv7]# vim Dockerfile

FROM nginx:v6

MAINTAINER "sunny <sunny@ghbsunny.cn>"

CMD "/bin/bash"
```

构建镜像，注意，会提示执行一个build trigger,如下Executing 1 build trigger

```dockerfile
[root@node1 nginxv7]# docker build -t nginx:v7 ./

Sending build context to Docker daemon  2.048kB

Step 1/3 : FROM nginx:v6

# Executing 1 build trigger

 ---> Running in 6bb18c52af99

Removing intermediate container 6bb18c52af99
```

 基于新镜像nginx:v7启动新容器nginxv7

```dockerfile
[root@node1 nginxv7]# docker run -it --rm --name nginxv7 nginx:v7

[root@becc66948713 src]# cat /etc/issue

\S

Kernel \r on an \m

Sunny do an onbuild~

[root@becc66948713 src]#
```

此时，在旧的镜像中的dockerfile里的ONBUILD已经触发，把信息写入到/etc/issue里

一个例子

```dockerfile
FROM debian:stretch-slim

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added

RUN groupadd -r mysql && useradd -r -g mysql mysql

RUN apt-get update && apt-get install -y --no-install-recommends gnupg dirmngr && rm -rf /var/lib/apt/lists/*

# add gosu for easy step-down from root

ENV GOSU_VERSION 1.7
RUN set -x \
	&& apt-get update && apt-get install -y --no-install-recommends ca-certificates wget && rm -rf /var/lib/apt/lists/* \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& gpgconf --kill all \
	&& rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true \
	&& apt-get purge -y --auto-remove ca-certificates wget

RUN mkdir /docker-entrypoint-initdb.d

RUN apt-get update && apt-get install -y --no-install-recommends \

# for MYSQL_RANDOM_ROOT_PASSWORD

​	pwgen \

# for mysql_ssl_rsa_setup

​	openssl \

# FATAL ERROR: please install the following Perl modules before executing /usr/local/mysql/scripts/mysql_install_db:

# File::Basename

# File::Copy

# Sys::Hostname

# Data::Dumper

​	perl \
&& rm -rf /var/lib/apt/lists/*

RUN set -ex; \

# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported

key='A4A9406876FCBD3C456770C88C718D3B5072E1F5'; \
export GNUPGHOME="$(mktemp -d)"; \
gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
gpg --batch --export "$key" > /etc/apt/trusted.gpg.d/mysql.gpg; \
gpgconf --kill all; \
rm -rf "$GNUPGHOME"; \
apt-key list > /dev/null

ENV MYSQL_MAJOR 5.7
ENV MYSQL_VERSION 5.7.24-1debian9

RUN echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list

# the "/var/lib/mysql" stuff here is because the mysql-server postinst doesn't have an explicit way to disable the mysql_install_db codepath besides having a database already "configured" (ie, stuff in /var/lib/mysql/mysql)

# also, we set debconf keys to make APT a little quieter

RUN { \
		echo mysql-community-server mysql-community-server/data-dir select ''; \
		echo mysql-community-server mysql-community-server/root-pass password ''; \
		echo mysql-community-server mysql-community-server/re-root-pass password ''; \
		echo mysql-community-server mysql-community-server/remove-test-db select false; \
	} | debconf-set-selections \
	&& apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}" && rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \
	&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \

# ensure that /var/run/mysqld (used for socket and lock files) is writable regardless of the UID our mysqld instance ends up having at runtime

&& chmod 777 /var/run/mysqld \

# comment out a few problematic configuration values

&& find /etc/mysql/ -name '*.cnf' -print0 \
	| xargs -0 grep -lZE '^(bind-address|log)' \
	| xargs -rt -0 sed -Ei 's/^(bind-address|log)/#&/' \

# don't reverse lookup hostnames, they are usually another container

&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' > /etc/mysql/conf.d/docker.cnf

VOLUME /var/lib/mysql

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 3306 33060
CMD ["mysqld"]
```

Dockerfile 使用经验
Dockerfile 示例

构建Nginx运行环境

```dockerfile
# 指定基础镜像

FROM sameersbn/ubuntu:14.04.20161014

# 维护者信息

MAINTAINER sameer@damagehead.com

# 设置环境

ENV RTMP_VERSION=1.1.10 \
    NPS_VERSION=1.11.33.4 \
    LIBAV_VERSION=11.8 \
    NGINX_VERSION=1.10.1 \
    NGINX_USER=www-data \
    NGINX_SITECONF_DIR=/etc/nginx/sites-enabled \
    NGINX_LOG_DIR=/var/log/nginx \
    NGINX_TEMP_DIR=/var/lib/nginx \
    NGINX_SETUP_DIR=/var/cache/nginx

# 设置构建时变量，镜像建立完成后就失效

ARG BUILD_LIBAV=false
ARG WITH_DEBUG=false
ARG WITH_PAGESPEED=true
ARG WITH_RTMP=true

# 复制本地文件到容器目录中

COPY setup/ ${NGINX_SETUP_DIR}/
RUN bash ${NGINX_SETUP_DIR}/install.sh

# 复制本地配置文件到容器目录中

COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /sbin/entrypoint.sh

# 运行指令

RUN chmod 755 /sbin/entrypoint.sh

# 允许指定的端口

EXPOSE 80/tcp 443/tcp 1935/tcp

# 指定网站目录挂载点

VOLUME ["${NGINX_SITECONF_DIR}"]

ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["/usr/sbin/nginx"]
```

构建tomcat 环境

Dockerfile文件

```dockerfile
# 指定基于的基础镜像

FROM ubuntu:13.10  

# 维护者信息

MAINTAINER zhangjiayang "zhangjiayang@sczq.com.cn"  

# 镜像的指令操作

# 获取APT更新的资源列表

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe"> /etc/apt/sources.list

# 更新软件

RUN apt-get update  

# Install curl  

RUN apt-get -y install curl  

# Install JDK 7  

RUN cd /tmp &&  curl -L 'http://download.oracle.com/otn-pub/java/jdk/7u65-b17/jdk-7u65-linux-x64.tar.gz' -H 'Cookie: oraclelicense=accept-securebackup-cookie; gpw_e24=Dockerfile' | tar -xz  
RUN mkdir -p /usr/lib/jvm  
RUN mv /tmp/jdk1.7.0_65/ /usr/lib/jvm/java-7-oracle/  

# Set Oracle JDK 7 as default Java  

RUN update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-7-oracle/bin/java 300     
RUN update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-7-oracle/bin/javac 300     

# 设置系统环境

ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/  

# Install tomcat7  

RUN cd /tmp && curl -L 'http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.8/bin/apache-tomcat-7.0.8.tar.gz' | tar -xz  
RUN mv /tmp/apache-tomcat-7.0.8/ /opt/tomcat7/  

ENV CATALINA_HOME /opt/tomcat7  
ENV PATH $PATH:$CATALINA_HOME/bin  

# 复件tomcat7.sh到容器中的目录 

ADD tomcat7.sh /etc/init.d/tomcat7  
RUN chmod 755 /etc/init.d/tomcat7  

# Expose ports.  指定暴露的端口

EXPOSE 8080  

# Define default command.  

ENTRYPOINT service tomcat7 start && tail -f /opt/tomcat7/logs/catalina.out
tomcat7.sh命令文件

export JAVA_HOME=/usr/lib/jvm/java-7-oracle/  
export TOMCAT_HOME=/opt/tomcat7  

case $1 in  
start)  
  sh $TOMCAT_HOME/bin/startup.sh  
;;  
stop)  
  sh $TOMCAT_HOME/bin/shutdown.sh  
;;  
restart)  
  sh $TOMCAT_HOME/bin/shutdown.sh  
  sh $TOMCAT_HOME/bin/startup.sh  
;;  
esac  
exit 0
```

原则与建议

容器轻量化。从镜像中产生的容器应该尽量轻量化，能在足够短的时间内停止、销毁、重新生成并替换原来的容器。
使用 .gitignore。在大部分情况下，Dockerfile 会和构建所需的文件放在同一个目录中，为了提高构建的性能，应该使用 .gitignore 来过滤掉不需要的文件和目录。
为了减少镜像的大小，减少依赖，仅安装需要的软件包。
一个容器只做一件事。解耦复杂的应用，分成多个容器，而不是所有东西都放在一个容器内运行。如一个 Python Web 应用，可能需要 Server、DB、Cache、MQ、Log 等几个容器。一个更加极端的说法：One process per container。
减少镜像的图层。不要多个 Label、ENV 等标签。
对续行的参数按照字母表排序，特别是使用apt-get install -y安装包的时候。
使用构建缓存。如果不想使用缓存，可以在构建的时候使用参数--no-cache=true来强制重新生成中间镜像。
一张形象图
