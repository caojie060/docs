# 用docsify写博客

## 为什么要用docsify

无需构建快速生成文档页

网站：https://github.com/docsifyjs/docsify
	文档：https://docsify.js.org/zh-cn

无需构建，写完 markdown 直接发布

支持自定义主题

容易使用并且轻量

**不想因为生成的一堆** `.html` **文件“污染” commit 记录，只需要创建一个** `index.html` **就可以开始写文档而且直接**[部署在 GitHub Pages](https://docsify.js.org/#/zh-cn/deploy)。

2020 最最最简单的是使用 docsify，写完直接 push到GitHub就好了。

大概长这样   [Xiaoyu Pang's blog](https://xiaoyupang.github.io)

![img](https://pic2.zhimg.com/50/v2-a3d02615114100db4acedd84dd07772b_hd.jpg?source=1940ef5c)







## 一 初始化项目

### 1.1 安装Node.js

下载并安装

### 1.2 安装docsify-cli工具

```bash
npm i docsify-cli -g
```

会在这个路径下

 C:\Users\Administrator\AppData\Roaming\npm\node_modules

生成 docsify-cli 文件夹

### 1.3 初始化文档结构

先创建一个本地文件夹docs，然后执行命令

```bash
docsify init ./docs
```

会生成如下目录：

```
 -| docs/
    -| .nojekyll 用于阻止 GitHub Pages 会忽略掉下划线开头的文件
    -| index.html 入口文件
    -| README.md 会做为主页内容渲染
```

直接编辑 `docs/README.md` 就能更新网站内容

**遇到的问题：**

1. 初始化docsify文档不成功

   升级node.js之后就成功了

```bash
npm install -g npm
```

### 1.4 本地实时预览

```bash
docsify serve docs
```

默认访问 [http://localhost:3000](http://localhost:3000/)

- README文件：

```markdown
# Headline
> An awesome project.
```

## 二、定制

### 2.1 定制导航栏

```html
<script>
    window.$docsify = {
      name: 'PassJava-Learning',
      repo: 'https://github.com/Jackson0714/PassJava-Platform',
      loadNavbar: true,
      loadSidebar: true, // 加载自定义侧边栏
      maxLevel: 2, // 默认情况下会抓取文档中所有标题渲染成目录，可配置最大支持渲染的标题层级。
      subMaxLevel: 4, // 生成目录的最大层级
      mergeNavbar: true, // 小屏设备下合并导航栏到侧边栏
      alias: { // 定义路由别名，可以更自由的定义路由规则。 支持正则
        '/.*/_sidebar.md': '/_sidebar.md',//防止意外回退
        '/.*/_navbar.md': '/_navbar.md'
      }
    }
  </script>
```

- 添加_sidebar.md文件来配置侧边栏

```markdown
* 介绍
    * [PassJava 功能介绍](introduction/PassJava_introduction_01.md)
    * [PassJava 必备知识](introduction/PassJava_introduction_02.md)
* PassJava 架构篇

* SpringBoot 学习篇
    * [SpringBoot整合JDBC](springboot-tech/spring-boot-05-data-jdbc.md)
    * [SpringBoot整合Druid](springboot-tech/spring-boot-06-data-druid.md)
    * [SpringBoot整合MyBatis](springboot-tech/spring-boot-07-data-mybatis.md)

* 工具篇
    * [图床神器配置](tools/图床神器配置.md)
    * [使用docsify写开源文档](tools/使用docsify写开源文档.md)
    * [我的常用工具](tools/我的常用工具.md)

* 想法
    * [打造一款刷Java知识的小程序2](idea/打造一款刷Java知识的小程序2.md)
```

- 添加_navbar.md文件来配置顶部导航栏

```markdown
* 演示
  * [后台管理]()
  * [小程序端]()

* 项目地址
  * [后台平台](https://github.com/Jackson0714/PassJava-Platform)
  * [后台管理](https://github.com/Jackson0714/PassJava-Portal)
  * [学习教程](https://github.com/Jackson0714/PassJava-Learning)
```

- 查看导航栏效果

  

  ![img](https://pic1.zhimg.com/v2-9b0a2e2fa2b4ecf45309ef070fd5f8cf_r.jpg)

  

### 2.2 定制封面页

- 在index.html中添加封面页的配置

```markdown
<script>
    window.$docsify = {
      coverpage: true
    }
 </script>
```

- 添加_coverpage.md文件来配置封面页

```markdown
![logo](images/logo.png)

# PassJava-Learning

> PassJava 学习教程，架构、业务、技术要点全方位解析。

PassJava 是一款帮助Java面试的开源系统，
可以用零碎时间利用小程序查看常见面试题，夯实Java基础。
采用流行的技术，如 SpringBoot、MyBatis、Redis、 MySql、
MongoDB、 RabbitMQ、Elasticsearch，采用Docker容器化部署。

[GitHub](https://github.com/jackson0714/PassJava-Learning)
[Get Started](README.md)
```

- 查看封面效果

  

  ![img](https://pic3.zhimg.com/v2-bd70e0149e5e42b4b8e0ca99bca8ccc3_r.jpg)

  

###2.3添加全文搜索

在index.html中添加全文搜索的配置

```html
<script>
    window.$docsify = {
      search: {
        placeholder: '搜索',
        noData: '找不到结果!',
        depth: 3
      },
    }
 </script>
```



![img](https://picb.zhimg.com/v2-e6541ddb6222c3511d3d14923bcc73de_r.jpg)

#### 搜索插件

新增index.html:

```html
<script>
  window.$docsify = {
    search: 'auto',
 
    search : [
      '/',            // => /README.md
      '/guide',       // => /guide.md
      '/get-started', // => /get-started.md
      '/zh-cn/',      // => /zh-cn/README.md
    ],
 
     
    search: {
      maxAge: 86400000,
      paths: [],
      placeholder: 'Type to search',
 
       
      placeholder: {
        '/zh-cn/': '搜索',
        '/': 'Type to search'
      },
 
      noData: 'No Results!',
 
 
      noData: {
        '/zh-cn/': '找不到结果',
        '/': 'No Results'
      },
 
      depth: 2,
 
      hideOtherSidebarContent: false,
 
 
      namespace: 'website-1',
    }
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
```

**那我们来解释一下： 1.指定搜索路径** `search: 'auto',`**表示是否搜索，默认是**`auto` **或：**

```javascript
search : [
      '/',            // => /README.md
      '/guide',       // => /guide.md
      '/get-started', // => /get-started.md
      '/zh-cn/',      // => /zh-cn/README.md
    ],
```

**如：**`/`**就表示**`README.md` `guide`**表示**`/guide.md` **设置后就表示只搜索这几个目录 2.**`maxAge: 86400000,`**到期时间（官方这么说），不用改动 3.**`paths: [],`**可以设置搜索的目录，或设置**`auto`**或**`/`**，貌似和**`search:[]`**一样？ 4.搜索框的提示** `placeholder: 'Type to search',` **或：**

```javascript
placeholder: {
        '/zh-cn/': '搜索',
        '/': 'Type to search'
      },
```

**这样可以设置中英文目录的搜索框的提示** `noData: 'No Results!',`**表示无结果时显示的文字 或：**

```javascript
noData: {
        '/zh-cn/': '找不到结果',
        '/': 'No Results'
      },
```

**分别设置中英文 5.标题深度** `depth: 2,`**（官方这么解释）可以设置为**`1-6` **6.隐藏其他侧边栏内容** `hideOtherSidebarContent: false,`**（官方这么解释）默认为**`false` **7.避免搜索索引冲突** `namespace: 'website-1',`**可以自己设置 同一域下的多个网站之间可以设置名称 避免搜索索引冲突 其实有很多参数都不用设置 比如我的配置是：**

```javascript
search: 'auto',
search: {
maxAge: 86400000,
paths: '/',
placeholder: '搜索...',
noData: '未找到结果，换个搜索词试试？',
namespace: 'XhemjBlog',
    },
```



### 2.4添加代码高亮

在index.html中添加代码高亮的配置

```html
  <script src="//unpkg.com/prismjs/components/prism-bash.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-java.js"></script>
  <script src="//unpkg.com/prismjs/components/prism-sql.js"></script>
```

其他支持高亮语言请参考：https://github.com/PrismJS/prism/tree/gh-pages/components

### 2.5 添加一键拷贝代码

在index.html中添加一键拷贝代码的配置

```html
<script src="//unpkg.com/docsify-copy-code"></script>
```

#### 复制代码插件

```html
<script src="//cdn.jsdelivr.net/npm/docsify-copy-code"></script>
```



### 2.6 主题颜色

```javascript
window.$docsify = {
    themeColor: '#c30aff',
}
```

`#c30aff`就是主题的颜色了

### 2.7 外链打开方式

```javascript
window.$docsify = {
    externalLinkTarget: '_blank',
}
```

`_blank`**表示在新标签页中打开**

### 2.8 表情插件

先在`index.html`中新增:

```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/emoji.min.js"></script>
```

即可输入 ​`:100:` => :100:

### 2.9 Google Analytics

就是谷歌统计 直接新增:

```html
<script>
  window.$docsify = {
    ga: 'UA-XXXXX-Y'
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/ga.min.js"></script>
```

`ga: 'UA-XXXXX-Y'`**就是谷歌统计的编号 或：**

```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js" data-ga="UA-XXXXX-Y"></script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/ga.min.js"></script>
```

```javascript
ga: 'UA-XXXXX-Y'=data-ga="UA-XXXXX-Y"
```

### 2.10 外链脚本插件

如果你需要在.md文件中引用如：

```html
<script src="https://domain.com/xxx.js" ></script>
```

安装：

```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/external-script.min.js"></script>
```

> 照这样看来是可以在.md中写.html的……

### 2.11 图片缩放插件

```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/zoom-image.min.js"></script>
```

**效果就是点击一下图片可以放大 如：** ![logo](https://docsify.js.org/_media/icon.svg) **如果不想缩放可以设置：**

```markdown
![](image.png ":no-zoom")
```

### 2.12 Disqus评论插件

```html
<script>
  window.$docsify = {
    disqus: 'shortname'
  }
</script>
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/disqus.min.js"></script>
```

### 2.13 Gitalk评论插件

```html
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/gitalk/dist/gitalk.css">
 
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/gitalk.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/gitalk/dist/gitalk.min.js"></script>
<script>
  var gitalk = new Gitalk({
    clientID: 'Github Application Client ID',
    clientSecret: 'Github Application Client Secret',
    repo: 'Github repo',
    owner: 'Github repo owner',
    admin: ['Github repo collaborators, only these guys can initialize github issues'],
    // facebook-like distraction free mode
    distractionFreeMode: false
  })
</script>
```

**可以使文章实现评论效果，教程详见：**https://github.com/gitalk/gitalk/

### 2.13 链接下一篇文章插件

**可以再文章底部显示“下一篇”和“上一篇” 效果见**[https://xhemj.gitee.io/books/#/p/how-to-use-Docsify.md](https://xhemj.gitee.io/books/#/p/how-to-use-Docsify)

```html
<script src="//cdn.jsdelivr.net/npm/docsify-pagination/dist/docsify-pagination.min.js"></script>
```

**也可以自定义：**

```javascript
window.$docsify = {
pagination: {
            previousText: '上一篇',
            nextText: '下一篇',
            crossChapter: true,
            crossChapterText: true,
        },
    }
```

**更多插****件可以见**https://docsify.js.org/#/awesome?id=plugins

### 2.14 Social Share分享插件

**经过测试，无法直接在**`index.html`**中嵌入代码 需要先安装上面的外链脚本插件**

```html
<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/external-script.min.js"></script>
```

**后在**`.md`**文件中写下：**

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/social-share.js/1.0.16/css/share.min.css">
<div class="social-share"></div>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/social-share.js/1.0.16/js/social-share.min.js"></script>
```

即可在文件中嵌入分享插件 详细自定义教程可见：https://github.com/overtrue/share.js

### 2.15 嵌入Markdown文件插件

```html
<script src="https://unpkg.com/docsify-remote-markdown/dist/docsify-remote-markdown.min.js">
```

可以自定义：

```javascript
window.$docsify = {
remoteMarkdown: {
    tag: 'md',
        },
    }
```

使用方法：

```markdown
[你设置的tag，如：md](https://domain.com/markdown.md)
```

效果如上方的分享插件就可以直接链接： 而不用写分享代码

```html
<script src="https://unpkg.com/docsify-footer-enh/dist/docsify-footer-enh.min.js"></script>
```

**自定义：**

```javascript
window.$docsify = {
footer: {
            copy: '',
            auth: '',
            pre: '<hr>',
            style:'text-align: center;'
        },
    }
```

**实测**`copy`**和**`auth`**可以随便写 写什么文字代码都可以** `pre`**是正文和Footer的分割线，默认**`<hr>` **效果可以见**[https://xhemj.gitee.io/books/#/p/how-to-use-Docsify.md](https://xhemj.gitee.io/books/#/p/how-to-use-Docsify)

### 2.16 自定义封面背景

目前的背景是随机生成的渐变色，每次刷新都会显示不同的颜色。
docsify封面支持自定义背景色或者背景图，在_coverpage.md文档末尾添加：

```markdown
<!-- 背景图片 -->
![](_media/bg.png)

<!-- 背景色 -->
![color](#2f4253)
```

注意：
1.自定义背景配置一定要在_coverpage.md文档末尾。
2.背景图片和背景色只能有一个生效.
3.背景色一定要是#2f4253这种格式的。

### 2.17 把封面作为首页

配置了封面后，封面和首页是同时出现的，封面在上面，首页在下面。
 通过设置`onlyCover`参数，可以让docsify网站首页只显示封面，
 原来的首页通过`http://localhost:3000/#/README`访问。

在`index.html`文件中的`window.$docsify`添加`onlyCover: true,`选项：

```markdown
<script>
  window.$docsify = {
    coverpage: true,
    onlyCover: true,
  }
</script>
<script src="./docsify.min.js"></script>
```

通过此配置可以把./README.md文件独立出来，当成项目真正的README介绍文件。

### 2.18 侧边栏目录扩展和折叠

首先，确保已启用[loadSidebar](https://docsify.js.org/#/configuration?id=loadsidebar)配置，并且Markdown文件`_sidebar.md`位于根目录中。

然后将脚本插入文档，就像[官方插件](https://docsify.js.org/#/plugins)的用法一样

```html
<script>
  window.$docsify = {
    loadSidebar: true,
    alias: {
      '/.*/_sidebar.md': '/_sidebar.md',
    },
    subMaxLevel: 3,
    ...
  }
</script>
<script src="//unpkg.com/docsify/lib/docsify.min.js"></script>

<!-- plugins -->
<script src="//unpkg.com/docsify-sidebar-collapse/dist/docsify-sidebar-collapse.min.js"></script>
```

```html
<link rel="stylesheet" href="./statics/css/sidebar-folder.css">
```



#### 风格示范

- 箭头样式

  参考：[sidebar.css](https://github.com/iPeng6/docsify-sidebar-collapse/blob/master/src/sidebar.css)

- 资料夹样式

  参考：[sidebar-folder.css](https://github.com/iPeng6/docsify-sidebar-collapse/blob/master/src/sidebar-folder.css)

  [![img](https://github.com/iPeng6/docsify-sidebar-collapse/raw/master/assets/style-folder.jpg)](https://github.com/iPeng6/docsify-sidebar-collapse/blob/master/assets/style-folder.jpg)

## 三、写文章

**只需用Markdown语法写好一个**`.md`的文章放在根目录或子目录后就会自动识别了。

`_sidebar.md`的加载逻辑是从每层目录下获取文件，如果当前目录不存在该文件则回退到上一级目录。 例如当前路径为`/zh-cn/more-pages`则从`/zh-cn/_sidebar.md`获取文件，如果不存在则从`/_sidebar.md`获取。

> 注意，如果是托管在网上，请在文件根目录新增名叫`.nojekyll`的空文件。

为了更好地SEO，您可以在每个文件后面自定义标题：

```markdown
* [Home](/)
* [Guide](guide.md "The greatest guide in the world")
```

默认情况下会自动根据文章标题生成目录，如果不想要，可以再`index.html`中新增：

```html
<script>
  window.$docsify = {
    loadSidebar: true,
    subMaxLevel: 2
  }
</script>
```

`subMaxLevel: 2`表示只显示`h1~h2`的标题，对应`#`和`##`。 如果你想忽略某个标题，则可以在文章中新增`{docsify-ignore}`：

```markdown
# Getting Started
## Header {docsify-ignore}
```

如果想忽略全部的标题，则可以新增`{docsify-ignore-all}`：

```markdown
# Getting Started {docsify-ignore-all}
## Header
```

表示忽略`{docsify-ignore-all}`下的全部标题

!> `{docsify-ignore-all}`和`{docsify-ignore}`在正文中都不会显示

## 四、在Github上部署文档

- 提交代码到github

- Setting中开启github pages

  

  ![img](https://pic2.zhimg.com/v2-67b0f5eac88e31b4bfbb2aa0d5016eb4_r.jpg)

  

- GitHub Pages配置

  

  ![img](https://picb.zhimg.com/v2-cda8a593ebd43ea4e1a6ee43bfc99cdb_r.jpg)

  

- 配置成功

  访问 https://jackson0714.github.io/PassJava-Learning

## 五、部署到云服务器

### 1.添加nginx配置文件

- 执行命令

```bash
sudo vim /etc/nginx/conf.d/pass_java_learning.conf
```

- 更新配置信息

  ```nginx
  server {
    listen       80;
    server_name  tech.jayh.club;
  
    location / {
        root   /home/ubuntu/jay/passjava/passjava-learning/PassJava-Learning/docs;
        index  index.html;
    }
  }
  ```


### 2.域名解析

主机记录：tech

记录类型：A

线路类型：默认

记录值：主机IP地址



![img](https://picb.zhimg.com/v2-11449b1026e001902856a07d4bd71a60_r.jpg)



### 3.访问 tech.jay.club

###4. 遇到的问题

- 404  未找到页面

  可以通过命令查看错误日志

  ```bash
  cat /var/log/nginx/error.log
  ```

  **原因：**docs 路径配置错误，下面三种路径都报404

  ​    /home/jay/passjava/passjava-learning/PassJava-Learning/docs;

  ​    /jay/passjava/passjava-learning/PassJava-Learning/docs;

  ​    ~/jay/passjava/passjava-learning/PassJava-Learning/docs;

  **解决方案：**

  改成 /home/ubuntu/jay/passjava/passjava-learning/PassJava-Learning/docs

- 403 限制访问

  修改nginx.conf文件

  ```bash
  sudo vim nginx.conf
  ```

  `user www-data` 改为 `user root`

  重启 nginx 服务

  ```bash
  sudo service nginx restart
  ```

  

https://www.zhihu.com/question/59088760/answer/1315283862

https://zhuanlan.zhihu.com/p/125711613

https://blog.csdn.net/github_39655029/article/details/105852702

http://www.zyiz.net/tech/detail-123347.html

https://www.imooc.com/article/287154

https://blog.csdn.net/weixin_33874713/article/details/88705987

[关于导航_sidebar，可以设置二级导航收缩功能](https://github.com/docsifyjs/docsify/issues/616)

https://www.jianshu.com/p/bac7e84adf21

 [docsify-edit-on-github](https://github.com/njleonzhang/docsify-edit-on-github)

**[ docsify-sidebar-collapse](https://github.com/iPeng6/docsify-sidebar-collapse)**

[awesome-docsify](https://github.com/docsifyjs/awesome-docsify)

