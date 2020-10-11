#SQL查询基础语法

数据库概要



SQL查询最基础语法
目 录

基本的SELECT语句
内置函数和计算
WHERE条件限制——展开
GROUP BY 分组条件——展开
HAVING 过滤分组条件——展开
ORDER BY对结果进行排序————展开
子查询——展开
JOIN多表联合查询——展开
小结：


1 基本的SELECT语句

SELECT 语句的基本格式为：

SELECT 要查询的列名 FROM 表名字 WHERE 限制条件; # 如果要查询表的所有内容，只需要把列名改成星号 *

# 查询‘员工表’所有内容

SELECT * FROM employee;

列名：id、姓名、年龄、薪水、手机、部门
# 查询‘项目表’所有内容

SELECT * FROM project;

列名：项目id，项目名称、开始时间、结束时间、所属部门
# 查询‘部门表’所有内容

SELECT * FROM department;

列名：部门名称，部门人数
#查询姓名和年龄

SELECT name,age FROM employee;



2 内置函数和计算
函数名：COUNT SUM AVG MAX MIN

作用： 计数 和 平均值 最大值 最小值

COUNT 函数可用于任何数据类型(因为它只是计数)，而 SUM 、AVG 函数都只能对数字类数据类型做计算，MAX 和 MIN 可用于数值、字符串或是日期时间数据类型



# 计算出薪水的数量、平均值和最大值。 as 表示 别名

SELECT count(salary) as number, avg(salary), max(salary) as max_salary FROM employee;



3 WHERE条件限制——展开

3.1 WHERE限制条件可以有数学符号 (=,<,>,>=,<=)

# 筛选出年龄大于 25 的结果

SELECT name,age FROM employee WHERE age>25;

# 查找一个名字为 Tom的员工 # 查询字符串（文本）要将内容用’’前后括起来

SELECT name,age,phone FROM employee WHERE name='Mary'; 

3.2 WHERE 后面可以有不止一条限制，而根据条件之间的逻辑关系，可以用 OR(或) 和 AND(且) 连接：

#筛选出 年龄小于 30，或 age 大于 40

SELECT name,age FROM employee WHERE age<30 OR age>40;

3.3 筛选“在”或“不在”某个范围内的结果，用in或not in

# 查询在部门3或部门4的人:

SELECT name,age,phone,in_dpt 
FROM employee 
WHERE in_dpt IN ('dpt3','dpt4');

3.4 关键字 LIKE 在SQL语句中和通配符一起使用，通配符代表未知字符。SQL中的通配符是 _ 和 % 。其中 _ 代表一个未指定字符，% 代表不定个未指定字符。

# 电话号码前四位数为1101，而后两位忘记了，则可以用两个 _ 通配符代替：

SELECT name,age,phone FROM employee WHERE phone LIKE '1101__';



4 GROUP BY 分组条件——展开

先将指定字段有相同内容归为一组，将所有记录分类成各个组，然后针对各组进行下一步操作和计算（如求每组数量count，求每组数值和sum，求每组最大值max等）。

# 求每个部门的人数、部门薪水总和、部门最高薪水

SELECT in_dpt, count(id), sum(salary), max(salary)

FROM employee

GROUP BY in_dpt;




5 HAVING 过滤分组条件——展开

将分组条件分组计算后的各组的值再进行条件筛选

# 求部门人数在三个人及以上的部门，每个部门的人数、部门薪水总和、部门最高薪水

SELECT in_dpt, count(id), sum(salary), max(salary)
FROM employee
GROUP BY in_dpt
HAVING count(id) > 2;

6 ORDER BY对结果进行排序————展开
对结果按某一列来排序，这就要用到 ORDER BY排序关键词。默认情况下，ORDER BY的结果是升序排列，而使用关键词asc和desc可指定升序或降序排序。

# 按薪水降序排列

SELECT * FROM employee ORDER BY salary desc;



7 子查询——展开

当查询条件WHERE的取值范围需要通过其他表获取时

# 想要知道名为 "Tom" 的员工所在部门做了几个工程。员工信息储存在 employee 表中，但工程信息储存在project 表中

SELECT COUNT(proj_name) 
FROM project
WHERE of_dpt in (SELECT in_dpt FROM employee WHERE name='Tom');



8 JOIN多表联合查询——展开

子查询只有在结果来自一个表时才有用。所以需要显示两个表或多个表中的数据时需要多表查询。多表联合的基本思想是把多个表按指定的相同字段连接成一个新的表来操作。

# 查询各员工所在部门的人数

SELECT employee.id, employee.name, department.people_num
FROM employee 
JOIN department ON employee.in_dpt = department.dpt_name
ORDER BY id;



9 小结：

7 	SELECT (查询内容)
1 	FROM <left table> （查询主表）
3 	<join type> JOIN <right table> （关联的表）
2 	ON <join condition> （两表关联条件）
4 	WHERE （过滤查询结果的条件）
5 	GROUP BY （分组条件）
6 	HAVING （过滤分组的条件）
8 	ORDER BY （排序条件）
# 前面的数字为实际程序执行时的顺序，要养成良好的代码格式，该空行空行，该大写大写（数据库操作的词尽量保持大写，库表列内容等尽量保持小写）



如果需要详细语法，请移步网盘下载：

https://pan.baidu.com/s/1Gxu70S-SukaS24WuMOt7nA

编辑于 2018-03-16
赞同 20
添加评论
分享
收藏
喜欢

收起
继续浏览内容

知乎
发现更大的世界
打开

Chrome
继续

张文亮
分布式数据管理系统研发
讲逻辑，多练习，写整齐和规范
发布于 2011-06-02
赞同
添加评论
分享
收藏
喜欢

继续浏览内容

知乎
发现更大的世界
打开

Chrome
继续

不剪发的Tony老师
一个专注于数据库领域的分享者
推荐我自己的一个视频：《SQL 入门教程》。


SQL 入门教程
【课程介绍】
本课程为 SQL 入门教程，基于最新标准 SQL: 2016，全面讲解六种主流数据库的 SQL 语句实现与差异，包括：Oracle、MySQL、SQL Server、PostgreSQL、Db2 以及 SQLite 。

【课程收益】
掌握最新 SQL 标准中的查询语句、条件过滤、分组汇总、排序显示，多表连接查询，子查询，集合运算，常见函数等等；
学会使用数据操作语句（INSERT、UPDATE、DELETE、MERGE）维护表中的数据；
学习视图的操作以及使用数据定义语言（DDL）维护表结构。
以上内容在六种数据库中的实现和差异。