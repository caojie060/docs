# `SQL`大全

## 一、基础

### 1、说明：创建数据库

```sql
CREATE DATABASE database-name
```

### 2、说明：删除数据库

```sql
drop database dbname
```

### 3、说明：备份`sql server`

--- 创建 备份数据的 `device`

```sql
USE master

EXEC sp_addumpdevice 'disk', 'testBack', 'c:\mssql7backup\MyNwind_1.dat'
```

--- 开始 备份

```sql
BACKUP DATABASE pubs TO testBack
```

### 4、说明：创建新表

```sql
create table tabname(col1 type1 [not null] [primary key],col2 type2 [not null],..)
```

#### 根据已有的表创建新表：

A：

```sql
create table tab_new like tab_old (使用旧表创建新表)
```

B：

```sql
create table tab_new as select col1,col2… from tab_old definition only
```

### 5、说明：删除新表

```sql
drop table tabname
```

### 6、说明：增加一个列

```sql
Alter table tabname add column col type
```

注：列增加后将不能删除。`DB2`中列加上后数据类型也不能改变，唯一能改变的是增加`varchar`类型的长度。

### 7、说明：添加主键：

```sql
Alter table tabname add primary key(col)
```

#### 说明：删除主键：

```sql
 Alter table tabname drop primary key(col) 
```

### 8、说明：创建索引：

```sqlite
create [unique] index idxname on tabname(col….)
```

#### 删除索引：

```sql
drop index idxname
```

注：索引是不可更改的，想更改必须删除重新建。

### 9、说明：创建视图：

```sql
create view viewname as select statement
```

#### 删除视图：

```sql
drop view viewname
```

### 10、说明：几个简单的基本的`sql`语句

#### 选择：

```sql
select * from table1 where 范围
```

#### 插入：

```sql
insert into table1(field1,field2) values(value1,value2)
```

#### 删除：

```sql
delete from table1 where 范围
```

#### 更新：

```sql
update table1 set field1=value1 where 范围
```

#### 查找：

```sql
select * from table1 where field1 like ’%value1%’ 
```

---like的语法很精妙，查资料!

#### 排序：

```sql
select * from table1 order by field1,field2 [desc]
```

#### 总数：

```sql
select count as totalcount from table1
```

#### 求和：

```sql
select sum(field1) as sumvalue from table1
```

#### 平均：

```sql
select avg(field1) as avgvalue from table1
```

#### 最大：

```sql
select max(field1) as maxvalue from table1
```

#### 最小：

```sql
select min(field1) as minvalue from table1
```



### 11、说明：几个高级查询运算词

#### A： `UNION` 运算符

`UNION` 运算符通过组合其他两个结果表（例如 `TABLE1` 和 `TABLE2`）并消去表中任何重复行而派生出一个结果表。当 `ALL` 随 `UNION` 一起使用时（即 `UNION ALL`），不消除重复行。两种情况下，派生表的每一行不是来自 `TABLE1` 就是来自 `TABLE2`。

#### B：`EXCEPT` 运算符

`EXCEPT`运算符通过包括所有在 `TABLE1` 中但不在 `TABLE2` 中的行并消除所有重复行而派生出一个结果表。当 `ALL` 随 `EXCEPT` 一起使用时 (`EXCEPT ALL`)，不消除重复行。

#### C：`INTERSECT`运算符

`INTERSECT`运算符通过只包括 `TABLE1` 和 `TABLE2` 中都有的行并消除所有重复行而派生出一个结果表。当 `ALL`随 `INTERSECT` 一起使用时 (`INTERSECT ALL`)，不消除重复行。

注：使用运算词的几个查询结果行必须是一致的。

### 12、说明：使用外连接

#### A、`left （outer） join`：

左外连接（左连接）：

结果集几包括连接表的匹配行，也包括左连接表的所有行。

`SQL`: 

```sql
select a.a, a.b, a.c, b.c, b.d, b.f from a LEFT OUT JOIN b ON a.a = b.c
```

#### B：`right （outer） join`:

右外连接(右连接)：

结果集既包括连接表的匹配连接行，也包括右连接表的所有行。

#### C：`full/cross （outer） join`：

全外连接：

不仅包括符号连接表的匹配行，还包括两个连接表中的所有记录。

### 12、分组:`Group by`:

一张表，一旦分组 完成后，查询后只能得到组相关的信息。

组相关的信息：

（统计信息） `count`,`sum`,`max`,`min`,`avg` 分组的标准)

在`SQLServer`中分组时：

不能以`text`,`ntext`,`image`类型的字段作为分组依据

在`selecte`统计函数中的字段，不能和普通的字段放在一起；

### 13、对数据库进行操作：

#### 分离数据库：

```sql
 sp_detach_db;
```

#### 附加数据库：

```sql
sp_attach_db 后接表名，附加需要完整的路径名
```

### 14.如何修改数据库的名称:

```sql
sp_renamedb 'old_name', 'new_name'
```

## 二、提升

### 1、说明：复制表(只复制结构,源表名：`a` 新表名：`b`) (`Access`可用)

法一：

```sql
select * into b from a where 1<>1（仅用于SQlServer）
```

法二：

```sql
select top 0 * into b from a
```

### 2、说明：拷贝表(拷贝数据,源表名：`a` 目标表名：`b`) (`Access`可用)

```sql
insert into b(a, b, c) select d,e,f from b;
```

### 3、说明：跨数据库之间表的拷贝(具体数据使用绝对路径) (`Access`可用)

```sql
insert into b(a, b, c) select d,e,f from b in ‘具体数据库’ where 条件
```

例子：

```sql
..from b in '"&Server.MapPath(".")&"\data.mdb" &"' where..
```

### 4、说明：子查询(表名1：`a` 表名2：`b`)

```sql
select a,b,c from a where a IN (select d from b ) 
```

或者: 

```sql
select a,b,c from a where a IN (1,2,3)
```

### 5、说明：显示文章、提交人和最后回复时间

```sql
select a.title,a.username,b.adddate from table a,(select max(adddate) adddate from table where table.title=a.title) b
```

### 6、说明：外连接查询(表名1：`a` 表名2：`b`)

```sql
select a.a, a.b, a.c, b.c, b.d, b.f from a LEFT OUT JOIN b ON a.a = b.c
```

### 7、说明：在线视图查询(表名1：`a` )

```sql
select * from (SELECT a,b,c FROM a) T where t.a > 1;
```

### 8、说明：between的用法,between限制查询数据范围时包括了边界值,not between不包括

```sql
select * from table1 where time between time1 and time2

select a,b,c, from table1 where a not between 数值1 and 数值2
```

### 9、说明：in 的使用方法

```sql
select * from table1 where a [not] in (‘值1’,’值2’,’值4’,’值6’)
```

### 10、说明：两张关联表，删除主表中已经在副表中没有的信息

```sql
delete from table1 where not exists ( select * from table2 where table1.field1=table2.field1 )
```

### 11、说明：四表联查问题：

```sql
select * from a left inner join b on a.a=b.b right inner join c on a.a=c.c inner join d on a.a=d.d where .....
```

### 12、说明：日程安排提前五分钟提醒

`SQL`: 

```sql
select * from 日程安排 where datediff('minute',f开始时间,getdate())>5
```

### 13、说明：一条`sql` 语句搞定数据库分页

```sql
select top 10 b.* from (select top 20 主键字段,排序字段 from 表名 order by 排序字段 desc) a,表名 b where b.主键字段 = a.主键字段 order by a.排序字段
```

具体实现：

关于数据库分页：

```sql
 declare @start int,@end int @sql nvarchar(600) set @sql=’select top’+str(@end-@start+1)+’+from T where rid not in(select top’+str(@str-1)+’Rid from T where Rid>-1)’ exec sp_executesql @sql
```

注意：在top后不能直接跟一个变量，所以在实际应用中只有这样的进行特殊的处理。Rid为一个标识列，如果top后还有具体的字段，这样做是非常有好处的。因为这样可以避免 top的字段如果是逻辑索引的，查询的结果后实际表中的不一致（逻辑索引中的数据有可能和数据表中的不一致，而查询时如果处在索引则首先查询索引）

### 14、说明：前10条记录

```sql
select top 10 * form table1 where 范围
```

### 15、说明：选择在每一组b值相同的数据中对应的a最大的记录的所有信息(类似这样的用法可以用于论坛每月排行榜,每月热销产品分析,按科目成绩排名,等等.)

```sql
select a,b,c from tablename ta where a=(select max(a) from tablename tb where tb.b=ta.b)
```

### 16、说明：包括所有在 `TableA`中但不在 `TableB`和`TableC`中的行并消除所有重复行而派生出一个结果表

```sql
(select a from tableA ) except (select a from tableB) except (select a from tableC)
```

### 17、说明：随机取出10条数据

```sql
select top 10 * from tablename order by newid()
```

### 18、说明：随机选择记录

```sql
select newid()
```

### 19、说明：删除重复记录

#### 1),

```sql
delete from tablename where id not in (select max(id) from tablename group by col1,col2,...)
```

#### 2),

```sql
select distinct * into temp from tablename

delete from tablename

insert into tablename select * from temp
```

评价：这种操作牵连大量的数据的移动，这种做法不适合大容量但数据操作

#### 3),例如：

在一个外部表中导入数据，由于某些原因第一次只导入了一部分，但很难判断具体位置，这样只有在下一次全部导入，这样也就产生好多重复的字段，怎样删除重复字段`alter table tablename`

--添加一个自增列

```sql
add column_b int identity(1,1)

delete from tablename where column_b not in(

select max(column_b) from tablename group by column1,column2,...)

alter table tablename drop column column_b
```

### 20、说明：列出数据库里所有的表名

```sql
select name from sysobjects where type='U' // U代表用户
```

### 21、说明：列出表里的所有的列名

```sql
select name from syscolumns where id=object_id('TableName')
```

### 22、说明：列示type、vender、pcs字段，以type字段排列，case可以方便地实现多重选择，类似select 中的case。

```sql
select type,sum(case vender when 'A' then pcs else 0 end),sum(case vender when 'C' then pcs else 0 end),sum(case vender when 'B' then pcs else 0 end) FROM tablename group by type
```

显示结果：

```bash
type vender pcs

电脑 A 1

电脑 A 1

光盘 B 2

光盘 A 2

手机 B 3

手机 C 3
```

### 23、说明：初始化表`table1`

```sql
TRUNCATE TABLE table1
```

### 24、说明：选择从10到15的记录

```sql
select top 5 * from (select top 15 * from table order by id asc) table_别名 order by id desc
```

