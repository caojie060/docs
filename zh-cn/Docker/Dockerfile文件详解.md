Dockerfile构建映像

可以在docker build命令中使用-f标志指向文件系统中任何位置的Dockerfile。

```bash
docker build -f /path/to/a/Dockerfile
```

## Dockerfile文件说明

**FROM：指定基础镜像，必须为第一个命令**

```dockerfile
格式：
　　FROM <image>
　　FROM <image>:<tag>
　　FROM <image>@<digest>
示例：
　　FROM mysql:5.6
注：
　　# tag或digest是可选的，如果不使用这两个值时，会使用latest版本的基础镜像
```

**MAINTAINER: 维护者信息**

```dockerfile
格式：
    MAINTAINER <name>
示例：
    MAINTAINER Jasper Xu
    MAINTAINER sorex@163.com
    MAINTAINER Jasper Xu <sorex@163.com>
```

**RUN：构建镜像时执行的命令**

```dockerfile
# RUN用于在镜像容器中执行命令，其有以下两种命令执行方式：
shell执行
格式：
    RUN <command>
exec执行
格式：
    RUN ["executable", "param1", "param2"]
示例：
    RUN ["executable", "param1", "param2"]
    RUN apk update
    RUN ["/etc/execfile", "arg1", "arg1"]
注：
　　# RUN指令创建的中间镜像会被缓存，并会在下次构建中使用。如果不想使用这些缓存镜像，可以在构建时指定--no-cache参数，如：docker build --no-cache

```

**ADD：将本地文件添加到容器中，tar类型文件会自动解压(网络压缩资源不会被解压)，可以访问网络资源，类似wget**

```dockerfile
格式：
    ADD <src>... <dest>
    ADD ["<src>",... "<dest>"] 用于支持包含空格的路径
示例：
    ADD hom* /mydir/          # 添加所有以"hom"开头的文件
    ADD hom?.txt /mydir/      # ? 替代一个单字符,例如："home.txt"
    ADD test relativeDir/     # 添加 "test" 到 `WORKDIR`/relativeDir/
    ADD test /absoluteDir/    # 添加 "test" 到 /absoluteDir/
    ADD home* /path/ # 支持通配符 * 添加所有以"home"开头的文件 到/path/ 下
```

**COPY：功能类似ADD，但是是不会自动解压文件，也不能访问网络资源**

语法

```dockerfile
[COPY <src> ... <dest>或 . COPY ["<src>",... "<dest>"]]()

# <src>：要复制的源文件或目录，支持使用通配符

 # <dest>：目标路径，即正在创建的 image的文件系统路径；建议为 <dest>使用绝对路径，<dest>绝对路径为镜像中的路径，而不是宿主机的路径。否则， COPY指定则以 WORKDIR为其起始路径

# 注意：在路径中有空白字符时，通常使用第二种格式 .
```

文件复制准则

```dockerfile
<src>必须是build上下文中的路径，即只能放在workshop这个工作目录下，不能是其父目录中的文件

如果<src>是目录，其内部文件或者子目录会被递归复制，但<src>目录自身不会被复制

如果指定了多个<src>，或在<src>中使用了通配符，则<dest>必须是一个目录，且dest目录必须以/结尾

如果<dest>事先不存在，它将会被自动创建，这包括其父目录路径
```

例子

> 创建一个目录img1，在该目录下新建index.html文件用于镜像制作的素材文件，在img1下新建Dockerfile文件，把index.html拷贝到新镜像里
>
> copy是指在当前的img1工作目录中，准备好要添加到新镜像的文件放到这个img1下面，copy过程实际是基于dockerfile在后台启动一个容器，把工作目录当做卷挂载到后台启动的容器，然后再把这些准备好的文件（img1目录下）拷贝到后台容器，然后基于这个容器制作新镜像，所以，镜像的制作过程是基于指定的镜像来制作

COPY文件

```bash
[root@node1 ~]# mkdir img1/
[root@node1 ~]# cd img1/
[root@node1 img1]# ls
[root@node1 img1]# vim index.html
<h1>zhujingxing </h1>
[root@node1 img1]# vim Dockerfile
# Description: test image
FROM busybox:latest
MAINTAINER "zisefeizhu <zisefeizhu@zhujingxing.com>"
#LABEL maintainer="zisefeizhu <zisefeizhu@zhujingxing.com>"
COPY index.html /data/web/html/

```

**CMD：构建容器后调用，也就是在容器启动时才进行调用。**

```dockerfile
格式：
    CMD ["executable","param1","param2"] (执行可执行文件，优先)
    CMD ["param1","param2"] (设置了ENTRYPOINT，则直接调用ENTRYPOINT添加参数)
    CMD command param1 param2 (执行shell内部命令)
示例：
    CMD echo "This is a test." | wc -
    CMD ["/usr/bin/wc","--help"]
注：
 　　# CMD不同于RUN，CMD用于指定在容器启动时所要执行的命令，而RUN用于指定镜像构建时所要执行的命令。
```

**ENTRYPOINT：配置容器，使其可执行化。配合CMD可省去"application"，只使用参数。**

```dockerfile
格式：    ENTRYPOINT ["executable", "param1", "param2"] (可执行文件, 优先)    ENTRYPOINT command param1 param2 (shell内部命令)示例：    FROM ubuntu    ENTRYPOINT ["top", "-b"]    CMD ["-c"]注：　　　# ENTRYPOINT与CMD非常类似，不同的是通过docker run# 执行的命令不会覆盖ENTRYPOINT，而docker run# 命令中指定的任何参数，都会被当做参数再次传递给ENTRYPOINT。Dockerfile中只允许有一个ENTRYPOINT命令，多指定时会覆盖前面的设置，而只执行最后的ENTRYPOINT指令。
```

**LABEL：用于为镜像添加元数据**

```dockerfile
格式：    LABEL <key>=<value> <key>=<value> <key>=<value> ...示例：　　LABEL version="1.0" description="这是一个Web服务器" by="IT笔录"注：　　# 使用LABEL指定元数据时，一条LABEL指定可以指定一或多条元数据，指定多条元数据时不同元数据之间通过空格分隔。推荐将所有的元数据通过一条LABEL指令指定，以免生成过多的中间镜像。
```

指定后可以通过docker inspect查看：

```shell
docker inspect itbilu/test
```

```json
"Labels": {    "version": "1.0",    "description": "这是一个Web服务器",    "by": "IT笔录"},
```

**ENV：设置环境变量**

```dockerfile
格式：    ENV <key> <value>  #<key>之后的所有内容均会被视为其<value>的组成部分，因此，一次只能设置一个变量    ENV <key>=<value> ...  #可以设置多个变量，每个变量为一个"<key>=<value>"的键值对，如果<key>中包含空格，可以使用\来进行转义，也可以通过""来进行标示；另外，反斜线也可以用于续行示例：    ENV myName John Doe    ENV myDog Rex The Dog    ENV myCat=fluffy    ENV version 1.0.0    ENV version=1.0.0    # 可以通过 ${key} 在其它指令中来引用变量，如 ${version} 。我们也可以通过 docker run 中的 -e <ENV> 来动态赋值。
```

**EXPOSE：指定于外界交互的端口**

```dockerfile
格式：    EXPOSE <port> [<port>...]示例：    EXPOSE 80 443    EXPOSE 8080    EXPOSE 11211/tcp 11211/udp注：　　# EXPOSE并不会让容器的端口访问到主机。要使其可访问，需要在docker run# 运行容器时通过-p来发布这些端口，或通过-P# 参数来发布EXPOSE导出的所有端口
```

**VOLUME：用于指定持久化目录**

```dockerfile
格式：    VOLUME ["/path/to/dir"]示例：    VOLUME ["/data"]    VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"注：　　# 一个卷可以存在于一个或多个容器的指定目录，该目录可以绕过联合文件系统，并具有以下功能：1 卷可以容器间共享和重用2 容器并不一定要和其它容器共享卷3 修改卷后会立即生效4 对卷的修改不会对镜像产生影响5 卷会一直存在，直到没有任何容器在使用它
```

**WORKDIR：工作目录，类似于cd命令**

```dockerfile
格式：    WORKDIR /path/to/workdir示例：    WORKDIR /a  (这时工作目录为/a)    WORKDIR b  (这时工作目录为/a/b)    WORKDIR c  (这时工作目录为/a/b/c)注：　　# 通过WORKDIR设置工作目录后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT、ADD、COPY等命令都会在该目录下执行。在使用docker run# 运行容器时，可以通过-w参数覆盖构建时所设置的工作目录。
```

**USER:**指定运行容器时的用户名或 UID，后续的 RUN 也会使用指定用户。使用USER指定用户时，可以使用用户名、UID或GID，或是两者的组合。当服务不需要管理员权限时，可以通过该命令指定运行用户。并且可以在之前创建所需要的用户

```dockerfile
格式:　　USER user　　USER user:group　　USER uid　　USER uid:gid　　USER user:gid　　USER uid:group 示例：　　USER www 注：　　# 使用USER指定用户后，Dockerfile中其后的命令RUN、CMD、ENTRYPOINT都将使用该用户。镜像构建完成后，通过docker run运行容器时，可以通过-u参数来覆盖所指定的用户。
```

ARG：用于指定传递给构建运行时的变量

```dockerfile
格式：    ARG <name>[=<default value>]示例：    ARG site    ARG build_user=www    # 通过 docker run 中的 --build-arg <key>=<value> 来动态赋值，不指定将使用其默认值。
```

**ONBUILD：用于设置镜像触发器**

```dockerfile
格式：　　ONBUILD [INSTRUCTION]示例：　　ONBUILD ADD . /app/src　　ONBUILD RUN /usr/local/bin/python-build --dir /app/src注：　　# 当所构建的镜像被用做其它镜像的基础镜像，该镜像中的触发器将会被钥触发
```



模板

```dockerfile
FROM 基础镜像MAINTAINER 维护者RUN 干什么ADD 放点文件WORKDIR 当前工作目录,cd改名了VOLUME 目录挂载EXPOSE 端口RUN 
```

[Dockerfile文件详解 - 百衲本 - 博客园](https://www.cnblogs.com/panwenbin-logs/p/8007348.html)
[Docker 构建脚本 Dockerfile 指令全解析 - DockOne.io](http://dockone.io/article/9404)