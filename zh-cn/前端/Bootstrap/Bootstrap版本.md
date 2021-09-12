# Bootstrap版本

## bootstrap中v4和v3版本的区别

|       Bootstrap v3       |                   Bootstrap v4                    |
| :----------------------: | :-----------------------------------------------: |
|        Less 编写         |                     Sass 编写                     |
|        4种栅格类         |                     5种栅格类                     |
|       使用px为单位       | 使用rem和em为单位 （除部分margin和padding使用px） |
| 使用push和pull向左右移动 |              偏移列通过offset-类设置              |
|   使用float的布局方式    |             选择弹性盒模型（flexbox）             |

**Bootstrap v4特点**

- 新增网格层适配了移动端；
- 全面引入ES6新特性（重写所有JavaScript插件）；
- css文件减少了至少40%；
- 所有文档都用Markdown编辑器重写；
- Bootstrap4 放弃了对 IE8 以及 iOS 6 的支持，现在仅仅支持 IE9 以上 以及 iOS 7 以上版本的浏览器。如果对于其中需要用到以前的浏览器，那么请使用 Bootstrap3。

**栅格**

> 注：Bootstrap3的4种栅格：

- 特小（col-xs-） 适配手机(<768px)
- 小（col-sm-） 适配平板(≥768px)
- 中（col-md-） 适配电脑(≥992px)
- 大（col-lg-） 适配宽屏电脑(≥1200px)

Bootstrap4的5种栅格：

- 特小（col-）(<576px)
- 小（col-sm-）(≥576px)
- 中（col-md-）(≥768px)
- 大（col-lg-） (≥992px)
- 特大（col-xl-）（≥1200px）

> 以往版本行放置在 .container class 内，在 Bootstrap 4 中行还可以放置在 .container-fluid (全屏宽度) class的容器中；

> Bootstrap 3 和 Bootstrap 4 最大的区别在于 Bootstrap 4 现在使用 flexbox（弹性盒子） 而不是浮动。Flexbox 的一大优势是，没有指定宽度的网格列将自动设置为等宽与等高列 。



[HTML中文网](https://www.html.cn/)

[bootstrap中v4和v3版本的区别是什么？](https://www.html.cn/framework/bootstrap/17824.html)

 [bootstrap版本的使用与变化](https://blog.csdn.net/zhangank/article/details/93981990)