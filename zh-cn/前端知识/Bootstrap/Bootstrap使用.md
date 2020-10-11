# Bootstrap使!用

##一、什么是bootstrap?

bootstrap框架提供两个最重要的文件：bootstrap.min.css和bootstrap.min.js

在bootstrap4.x版本中，bootstrap.min.js需要依赖两个文件：jquery-3.3.1.slim.min.js和popper.min.js

popper.min.js框架对制作和美化下拉框、文字提示、弹出框等非常有用

## 二、怎么使用bootstrap框架？

使用bootstrap框架有两个方法

### 一是在[官网](https://getbootstrap.com/)下载bootstrap

#### 解压缩后找到bootstrap.min.css和bootstrap.min.js复制粘贴到正在开发的项目下，

*具体放在工程里面的哪一级哪个目录下自己决定，*

#### 然后在需要用到该框架的.html文件里

- 用<link>标签引入bootstrap.min.css，
- 用<script>标签引入bootstrap.min.js。

> 在引入bootstrap.min.js文件之前必须引入jquery-3.3.1.slim.min.js和popper.min.js（这两个文件需要自行去各自官网下载然后复制粘贴到正在开发的项目的任意位置）

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 
    <!-- Bootstrap CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <!--你自己写的样式文件，尽量不要放在bootstrap.min.css之前-->
    <link href="css/your-style.css" rel="stylesheet"> 
 
  </head>
  <body>
    <h1>Hello, world!</h1>
 
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <!--官方建议这三个<script>标签写在body结束标签之前，三个标签顺序不能搞乱-->
    <script src="js/jquery-3.3.1.slim.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>
```

### 二是不需要下载任何文件，使用BootstrapCDN快速地将 Bootstrap 应用到你的项目中

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
 
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
 
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
  </body>
</html>
```

所有文件会通过http请求自动下载并引入到自己的项目中。

## 三、一些重要的设置

### 1. HTML5 doctype

Bootstrap 要求设置 HTML5 doctype，也就是.html文件需要使用HTML5的声明。如果没有这个设置，你会看到一些奇怪的、不完整的样式，但是只要添加了这个设置就不会出现任何错误了。

```html
<!doctype html>
<html lang="en">
  ...
</html>
```

lang属性可以不用添加。

### 2. 响应式meta标签

Bootstrap 本着 移动设备优先 的策略开发的，

按照这一策略，我们优先为移动设备优化代码，

然后根据每个组件的情况并利用 CSS 媒体查询（CSS media queries）技术为组件设置合适的样式。

> 为了确保在所有设备上能够正确渲染并支持触控缩放，务必将设置 viewport 属性的 meta 标签添加到 <head> 中。

```html
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
```

### 3. 盒模型

bootstrap框架内部已经将全局的 box-sizing 值从默认的 content-box 修改为 border-box。

这就确保了 padding 不会影响元素最终的宽度计算，但是这可能会导致第三方组件出现问题，例如 Google 地图和 Google 定制搜索。

所以有的时候需要手动设置回默认值去。怎么设置呢？

```css
.selector-for-some-widget {
  box-sizing: content-box;
}
```

关于box-sizing属性的值，我们可以参考文章：[css的两种盒模型](https://blog.csdn.net/zwkkkk1/article/details/79678177)

### 4. Reboot

为了改善跨浏览器的渲染，我们使用 [Reboot](https://v4.bootcss.com/docs/4.0/content/reboot/) 修正跨浏览器和设备之间的不一致性，同时对常用的 HTML 元素设置统一的效果。

bootstrap4.2.1官方文档：https://getbootstrap.com/docs/4.2/getting-started/introduction/

bootstrap4.x通用的中文文档：https://v4.bootcss.com/docs/4.0/getting-started/introduction/

[bootstrap使用入门（bootstrap4.2.1版本）](https://blog.csdn.net/weixin_41461967/article/details/87095582)