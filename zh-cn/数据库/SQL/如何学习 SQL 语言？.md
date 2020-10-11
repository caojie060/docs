# 如何学习 SQL 语言？

## 数据库基础

| 名称                               | 链接                                                         | 类型     | 说明                                                         |
| ---------------------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| 数据库基础知识复习                 | [数据库基础知识复习](http://blog.csdn.net/yutianzuijin/article/details/12243751) | csdn     | 其实这篇文章讲的就是所有要点，可以有针对性的了解不熟悉的。不太明白的就直接找一本《数据库原理》看看，大概5小时 |
| SQL 语言在数据分析工作中有多重要？ | [SQL 语言在数据分析工作中有多重要？](https://www.zhihu.com/question/362373428/answer/953729276) | 知乎     | 刷题前之前了解下 SQL 是什么                                  |
| 《SQL必知必会》                    |                                                              | 工具书   | 图灵出的,Amazon上最畅销的SQL图书的中文版，写得很明快，概念非常清楚。这本书用来学习关系型数据库也很不错，至少基本概念比大部头的教材说得清楚得多。这本书弊端在于，没办法直接练习，知识点很容易就忘记。我也是看完这本书之后感觉好像是懂了一些，一做题发现还是很多东西都学的半生不熟的状态，需要二次回炉重造。 |
| 《SQL入门经典》                    |                                                              | 工具书   | 都是简单易懂的经典教材，不用担心看不懂                       |
| Head First SQL                     |                                                              | 工具书   | O'Reilly的Head First SQL也很适合初学者，不过中文版《深入浅出SQL》 好像绝版了。 |
| 《SQL解惑(第2版)》                 | [SQL解惑第二版中文版.pdf](http://filemarkets.com/fs/bblu1esc5orp7io2da15/) | 工具书   | 图灵出的                                                     |
| 《SQL沉思录》                      | [51CTO下载-SQL沉思录.pdf](http://filemarkets.com/fs/bbldue7sc0or1pi4o1e7/) | 工具书   | 图灵出的                                                     |
| 《SQL编程风格》                    | [SQL编程风格.pdf](http://filemarkets.com/fs/dblufesc2orpcio15248/) | 工具书   | 图灵出的                                                     |
| 《SQL权威指南》                    | [MySQL开发者SQL权威指南.pdf](http://filemarkets.com/fs/6b8leu9e9sccaodrpio6/)[Transact-SQL权威指南.pdf](http://filemarkets.com/fs/ebl8ue9scbor5pico751/) | 工具书   | 图灵出的                                                     |
| 《Oracle完全学习手册》             |                                                              |          | 要入门Oracle的同学可以看看这本，从安装到操作讲解得非常详细，而且可以从头到尾跟着书本进行操作。如果仅仅想学习SQL语言的话，可以看看第7~10章，知识点覆盖面挺广的。 |
| 《MySQL必知必会》                  |                                                              |          | 没错，经典就是经典，最好的入门书籍，没有之一。十分全面，浅显易懂。最重要的是，整本书薄薄的，妈妈再也不怕孩子看书永远都停在第一页了。几天就能看完，对SQL语言有个大概的理解和印象。记不住也没关系，后面看视频刷题不怕记不住，这个阶段有个初步概念就行。 |
| SQL 教程菜鸟教程                   | [SQL 教程菜鸟教程](https://www.runoob.com/sql/sql-tutorial.html) | 网络教程 |                                                              |
| 关系型数据库基础概念_数据库        | [关系型数据库基础概念_数据库](https://blog.csdn.net/kdb_viewer/article/details/82688147?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task) | csdn     | 关系型数据库+SQL语法                                         |

- ## SQL基本语法

心中熟记SQL魔咒：`select from where group by having order by`

```sql
SELECT  [ALL|DISTINCT]  <列名> as <别称>  [,<表名> as <别称> ]....
FROM <表名> as <别称> [,<表名> as <别称> ]....
where <条件> 
GROUP BY  <列名>
HAVING  <条件>
ORDER BY <列名>  [ASC|DESC]
```

## SQL线上编辑器

| 名称                 | 链接                                                         | 类型       | 说明                                                         |
| -------------------- | ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| Fiddle               | [SQL Fiddle](http://www.sqlfiddle.com/)                      | 在线编辑器 | A tool for easy online testing and sharing of database problems and their solutions. |
| SQL Teaching         | [SQL Teaching](https://www.sqlteaching.com/)                 | 在线编辑器 | 英语教程                                                     |
| Learn SQL Codecademy | [Learn SQLCodecademy](https://www.codecademy.com/zh/learn/learn-sql) | 在线编辑器 | 这个网站提供了一些基本的SQL操作的教学资源和在线环境给初学者练习SQL，虽然是全英文的但是里边的英文并不难理解。每一个教学部分都有文字讲解和操作环节，讲解环节挺详细的，会把语句分解开来讲解 |
| SQL Zoo              | http://sqlzoo.net/wiki/SELECT_basics/zh                      | 在线编辑器 | 在SQL练习平台sqlzoo中将习题做一遍，不仅是检验前面的学习效果，更是通过实践加强熟悉前面的知识。这里不能偷懒，一定要将每一道提做一遍，以后找工作面试都能用得上。如果现在偷懒，后面找不到工作的恶果可是要自己负责的。这个平台致力于边学边练。但是只有SQL查询语言，题目非常简单，适合新手！ |
| 自学SQL网            | [自学SQL网](http://www.xuesql.cn/)                           | 在线编辑器 | 中文学习工具,和作者提供的「电影数据表」打交道。教材会引导你写SQL找出最新上映的N部电影，或者统计某个导演一共拍了多少电影之类的。 |
| datacamp             | [learn.datacamp.com](https://learn.datacamp.com/career-tracks/data-analyst-with-sql-server) |            | 包含了简单的查询语句，以及数据库的知识，知识点非常全面。如果对这个平台不是很熟悉，可以看这个回答：[datacamp好用吗?](https://www.zhihu.com/question/367036627/answer/1220480153)有11堂课，45课时，比阅读任何一本工具书都快，而且是边学边练，加深记忆。 |
| sqlbolt              | https://sqlbolt.com/                                         |            | 自学SQL网的原版练习网站 ,有免费的题解和额外课程              |

## SQL习题

| 名称                                         | 链接                                                         | 类型     | 说明                                                         |
| -------------------------------------------- | ------------------------------------------------------------ | -------- | ------------------------------------------------------------ |
| 经典SQL练习题                                | [经典SQL练习题](http://blog.csdn.net/qaz13177_58_/article/details/5575711/) | csdn     | 大概10小时就可以掌握                                         |
| SQL查询语句练习题27道                        | [SQL查询语句练习题27道](http://blog.csdn.net/friendan/article/details/8072668) | csdn     | 大概10小时就可以掌握                                         |
| 题库 - 力扣 (LeetCode)                       | [题库 - 力扣 (LeetCode)](https://leetcode-cn.com/problemset/database/) |          |                                                              |
| [更新中...]MySQL题目练习及答案（使用SQLyog） | [[更新中...]MySQL题目练习及答案（使用SQLyog）](https://blog.csdn.net/woooooood/article/details/85163780) | CSDN     | _woooooood的博客,sql yog 数据库练习题                        |
| SELECT within SELECT Tutorial/zh             | [SELECT within SELECT Tutorial/zh](https://zh.sqlzoo.net/wiki/SELECT_within_SELECT_Tutorial/zh)[答案](https://www.zhihu.com/question/19552975) | sqlzoo   | 在「国家信息表」中查询人口、gdp之类的信息                    |
| The JOIN operation/zh                        | [The JOIN operation/zh](https://zh.sqlzoo.net/wiki/The_JOIN_operation/zh)[答案](https://www.zhihu.com/question/19552975) | sqlzoo   | 賽事                                                         |
| More JOIN operations/zh                      | [More JOIN operations/zh](https://sqlzoo.net/wiki/More_JOIN_operations/zh)[答案](https://www.zhihu.com/question/19552975) | sqlzoo   | 電影                                                         |
| 自学SQL                                      | [自学SQL](http://xuesql.cn/)                                 | 在线测试 | 包含手册，在线练习，视频，文字课都在里面了                   |
| 数据库SQL实战_牛客网                         | [数据库SQL实战_牛客网](https://www.nowcoder.com/ta/sql)      | 在线测试 | 牛客上一共61题，与面试时的写code形式有点像，有些题比较刁钻，也有几道比较沙雕，总之刷它就对了 |
| 从零学会SQL：入门                            | [从零学会SQL：入门](https://www.zhihu.com/lives/1092472616434180096) | 知乎     | 1）了解数据库的基本概念<br/>2）如何安装数据库？<br/>3）表的创建、删除和更新<br/>4）数据的插入、删除和更新数据 |
| 从零学会SQL：简单查询                        | [从零学会SQL：简单查询](https://www.zhihu.com/lives/1097094125874200576) | 知乎     | 1）基本的查询语句<br/>2） 如何指定查询条件？<br/>3）注释和 SQL 语句注意事项<br/>4）学会运算符指定复杂的查询条件<br/>5）字符串模糊查询 |
| 从零学会SQL：汇总分析                        | [从零学会SQL：汇总分析](https://www.zhihu.com/lives/1097094227900571648) | 知乎     | 1）如何进行汇总分析？<br/>2）如何对数据分组？<br/>3）如何对分组结果指定条件？<br/>4）用 SQL 解决业务问题的套路是什么？<br/>5）如何对查询结果排序？<br/>6）如何看懂 SQL 报错信息？ |
| 从零学会SQL：复杂查询                        | [从零学会SQL：复杂查询](https://www.zhihu.com/lives/1104157397408395264) | 知乎     | 1）视图（什么是视图，如何使用，有什么用，注意事项）<br/>2）子查询、标量子查询、关联子查询<br/>3）各种常用函数 |
| 从零学会SQL：多表查询                        | [从零学会SQL：多表查询](https://www.zhihu.com/lives/1105128761158352896) | 知乎     | 1）表的加法<br/>2）联结，包括交叉联结、内联结、左联结、右联结、全联结<br/>3）一张图记住各种联结<br/>4）联结应用案例<br/>5）case表达式 |
| 猴子：图解SQL面试题：经典50题                | [猴子：图解SQL面试题：经典50题](https://zhuanlan.zhihu.com/p/38354000) | 知乎     | 这里总结了常见的面试题，为以后找工作面试做准备               |
| 《图解SQL面试题》                            | [猴子：免费教程《图解SQL面试题》](https://zhuanlan.zhihu.com/p/152233908) |          | 还有一本免费教程《图解SQL面试题》                            |
| 《SQL基础教程》                              | 日本人MICK所著                                               |          | 也有人推荐《sql必知必会》，但是对于零基础的朋友来说Mick的《sql基础教程》更容易看懂学会，非常适合入门者学习。如果只推荐一本书的话，我只推荐这本。 |
| 《sql进阶教程》                              | 日本人MICK所著                                               |          | 看了几本日本人写的cs类的书，感觉共同点就是，日本人写的cs类的书，不掉书袋，总是尽量把知识写的通俗易懂比如《程序员的数学1》，《网络是如何连接的》。 |
| 《SQL反模式》                                |                                                              |          | 我在sql成长方面最有收获的一本,我看你的答案后下载了此书，确实很不错的书，给我很大启发！ |

## SQL进阶

| 名称                                    | 链接                                                         | 类型   | 说明                                                         |
| --------------------------------------- | ------------------------------------------------------------ | ------ | ------------------------------------------------------------ |
| sql执行顺序 - qanholas                  | [sql执行顺序 - qanholas](http://www.cnblogs.com/qanholas/archive/2010/10/24/1859924.html) | 博客园 | sql执行顺序。当sql逻辑复杂后，sql的执行顺序就会非常重要      |
| SQL ROW_NUMBER() OVER函数的基本用法用法 | [SQL ROW_NUMBER() OVER函数的基本用法用法](http://www.cnblogs.com/gy51Testing/archive/2012/07/26/2609832.html) | 博客园 | SQL ROW_NUMBER() OVER函数。用作分组排序，比如各个省份税收排名前20的企业 |
| SQL中的case when then else end用法      | [SQL中的case when then else end用法](http://lj.soft.blog.163.com/blog/static/7940248120109215191358/) | 博客园 | case when then else end。用作条件判断，比如将10、11、12、13……19、20岁的人群新生成一个字段‘年龄段’取值为10-20岁；聚合函数分别计算，如sum(case when 性别=‘男’ then 收入 end) as 收入_男，sum(case when 性别=‘n女’ then 收入 end) as 收入_女 |
|                                         |                                                              |        | select时加标签。例如select出某一特征user_id时新建一个tag字段作为用户的标签。<br/><br/>select user_id,'白领' as tag |
| Hive差集运算详解                        | [Hive差集运算详解](http://blog.csdn.net/dr_guo/article/details/51182626) | csdn   | 差集运算。例如取A集合中不包含在B集合的用户，做差集。         |

















































[如何学习 SQL 语言？](https://www.zhihu.com/question/19552975)