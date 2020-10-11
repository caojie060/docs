#  数据库 GUI 管理工具

1）sqlyog 需要收费，当然有破解版，功能最全，好用
2）navicat 有入门和收费两种，普通使用，入门就足够了。界面小清新。
3）mysql workbench 官方出的GUI，还在不断改进中，基本功能都比较稳定，也是唯一支持多平台的一个GUI

基本上都在用sqlyog，确实好用，还很轻量。
navicat比较好用，就比如导入数据的时候，workbench我导了不下一万次都进不去，而且一堆英文看不懂，navicat.一下子就导入进入了

总结一下：Windows 上优先使用 sqlyog，linux（没有实际生产使用过，仅供参考） 使用 workbench 或 wine sqlyog（未测试），mac 上推荐使用 Sequel Pro。

MySQL Workbench简直反人类

一般都是HeidiSQL,Navicat,SQLyog这几个客户端同时用，各有优缺点吧。
需要同步结构和数据的话，可以使用Navicat；
需要直接复制数据库的话，可以使用SQLyog；
而HeidiSQL的界面相对友好一些，视觉体验好一点。

HeidiSQL 免费功能挺强~

不请自答，我用的是：dbForge Studio FOR MySQL。另外dbForge Studio出了很多其他的工具，例如Code Compare都很好用。

问题收费而且很贵，卖这么贵居然还不支持中文( •̥́ ˍ •̀ू )

dbForge Studio FOR MySQL有免费版本的，Code Compare也有免费版本的。免费版本的都已经很实用了。至于中文版的问题，这个确实没有。

神器

## HeidiSQL

开源免费功能强大的 MySQL（MariaDB）、MSSQL Server、PostgreSQL 数据库 GUI 管理工具

HeidiSQL 是一款数据库管理工具，支持通过多种方式连接管理 MySQL（MariaDB）、MSSQL Server、PostgreSQL 数据库，功能强大，完全免费，推荐大家使用。

可以直接显示数据库中的表以及表中的数据。

可以直接使用 SQL 脚本对数据库进行增、删、改、查。

在进行查询时，HeidiSQL 还贴心的提供了 SQL函数 SQL关键字 等功能，很方便 SQL 脚本的编辑。

支持直接查看数据库及数据表的大小，非常人性化。

[HeidiSQL](https://www.heidisql.com/download.php)[源代码](https://github.com/HeidiSQL/HeidiSQL/releases)

## SQLyog Community

免费的 MySQL GUI 管理工具

SQLyog Community （社区版）是一款免费的 MySQL/MariaDB 管理工具，可以远程管理 MySQL 数据库。

SQLyog Community 可以远程以图形化的方式管理 MySQL/MariaDB 服务。使用它，您可以一目了然的查看数据库中的库和表，点击几下鼠标即可实现对数据库表的设计，或者对数据的变更。也可以直接使用 SQL 语句对数据库进行查询或管理。

因为 SQLyog 有收费版，这款开源版阉割了一些功能，仅支持通过直接连接 MySQL 服务端口的方式连接至 MySQL 服务。其收费版可以支持通过 HTTP/SSH 等通道连接。

不过你可以配合使用本站提供的 **[远程端口映射工具 - 将远程服务器的端口通过SSH通道映射到本地](https://www.appgao.com/Network/remote-port-to-local.html)** ，通过 SSH 通道管理远程的 MySQL 服务。

该免费版本在关闭时也会有广告，提醒您升级到收费版。

 [SQLyog Community](https://github.com/webyog/sqlyog-community)



[大家常用哪个MySQL客户端工具，除了命令行那个mysql之外？](https://www.zhihu.com/question/20423448)

[HeidiSQL - 开源免费功能强大的 MySQL（MariaDB）、MSSQL Server、PostgreSQL 数据库 GUI 管理工具](https://www.appgao.com/Network/heidisql.html)

 [SQLyog Community - 免费的 MySQL GUI 管理工具](https://www.appgao.com/Programming/SQLyog-Community.html)