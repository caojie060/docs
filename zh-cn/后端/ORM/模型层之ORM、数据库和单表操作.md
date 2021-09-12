# 模型层之`ORM`、数据库和单表操作

<iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=86 src="//music.163.com/outchain/player?type=2&id=535351562&auto=1&height=66"></iframe>

## `ORM`简介

`ORM`是“对象-关系-映射”的简称，一般指持久化数据和实体对象的映射

### 什么是“持久化”

持久（Persistence），即把数据（如内存中的对象）保存到可永久保存的存储设备中（如磁盘）。

持久化的主要应用是将内存中的数据存储在关系型的数据库中，当然也可以存储在磁盘文件中、XML数据文件中等等。

### `ORM`的作用

在关系型数据库和对象之间作一个映射，

这样，我们在具体的操作数据库的时候，就不需要再去和复杂的`SQL`语句打交道，

只要像平时操作对象一样操作它就可以了 。

它实现了数据模型与数据库的解耦，

即数据模型的设计不需要依赖于特定的数据库，

通过简单的配置就可以轻松更换数据库。



## 连接数据库

`settings.py`文件下的DATABASES处修改配置



```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 连接数据库种类
        'NAME': 'test',  # 连接数据库名
        'HOST':'127.0.0.1',  # IP
        'PORT':3306,  # 端口
        'USER':'root',  # 用户名
        'PASSWORD':'123456'  # 密码
    }
}
# 键必须都是大写
```



告诉`Django`用`pymysql`替换它默认`mysqldb`模块连接数据库

- 方式1:在你的项目文件夹下面的`__init__.py`
- 方式2:也可以在你的应用文件夹下面的`__init__.py`

```python
# 固定写法

import pymysql
pymysql.install_as_MySQLdb()  # 告诉django用pymysql代替mysqldb连接数据库
```


　重新连接其他数据库

　　右键原数据库，remove，连接流程如上介绍。



## 单表操作

### 创建表

####  创建模型

　　应用文件夹下的`models.py`文件中创建模型

```python
from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)  # 设定主键并自增，如果不写，默认将id作为主键
    name = models.CharField(max_length=64)  # max_length参数必须写
    pub_data = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=12)

    def __str__(self):
        return self.name  # 返回一个字符串（这里是名字）区分不同的对象
```

### 更多字段和参数

#### 字段

| 字段                                                         | 类型               | 描述                                                         |
| ------------------------------------------------------------ | ------------------ | ------------------------------------------------------------ |
| `AutoField(Field)`                                           | `int自增列`        | `必须填入参数 primary_key=True`                              |
| `BigAutoField(AutoField)`                                    | `bigint自增列`     | `必须填入参数 primary_key=True`                              |
| `SmallIntegerField(IntegerField)`                            | `小整数`           | `-32768 ～ 32767`                                            |
| `PositiveSmallIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)` | `正小整数`         | `0 ～ 32767`                                                 |
| `IntegerField(Field)`                                        | `整数列(有符号的)` | `-2147483648 ～ 2147483647`                                  |
| `PositiveIntegerField(PositiveIntegerRelDbTypeMixin, IntegerField)` | `正整数`           | `0 ～ 2147483647`                                            |
| `BigIntegerField(IntegerField)`                              | `长整型(有符号的)` | `-9223372036854775808 ～ 9223372036854775807`                |
| `BooleanField(Field)`                                        | `布尔值类型`       |                                                              |
| `NullBooleanField(Field)`                                    | `可以为空的布尔值` |                                                              |
| `CharField(Field)`                                           | `字符类型`         | `必须提供max_length参数， max_length表示字符长度`            |
| `TextField(Field)`                                           | `文本类型`         |                                                              |
| `EmailField(CharField)`                                      | `字符串类型`       | `Django Admin以及ModelForm中提供验证机制`                    |
| `IPAddressField(Field)`                                      | `字符串类型`       | `Django Admin以及ModelForm中提供验证 IPV4 机制`              |
| `GenericIPAddressField(Field)`                               | `字符串类型`       | `Django Admin以及ModelForm中提供验证 Ipv4和Ipv6`             |
| `URLField(CharField)`                                        | `字符串类型`       | `Django Admin以及ModelForm中提供验证 URL`                    |
| `SlugField(CharField)`                                       | `字符串类型`       | `Django Admin以及ModelForm中提供验证支持 字母、数字、下划线、连接符（减号）` |
| `CommaSeparatedIntegerField(CharField)`                      | `字符串类型`       | `格式必须为逗号分割的数字`                                   |
| `UUIDField(Field)`                                           | `字符串类型`       | `Django Admin以及ModelForm中提供对UUID格式的验证`            |
| `FilePathField(Field)`                                       | `字符串`           | `Django Admin以及ModelForm中提供读取文件夹下文件的功能`      |
| `FileField(Field)`                                           | `字符串`           | `路径保存在数据库，文件上传到指定目录`                       |
| `ImageField(FileField)`                                      | `字符串`           | `路径保存在数据库，文件上传到指定目录`                       |
| `DateTimeField(DateField)`                                   | `日期+时间格式`    | `YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]`                         |
| `DateField(DateTimeCheckMixin, Field)`                       | `日期格式`         | `YYYY-MM-DD`                                                 |
| `TimeField(DateTimeCheckMixin, Field)`                       | `时间格式`         | `HH:MM[:ss[.uuuuuu]]`                                        |
| `DurationField(Field)`                                       | `长整数`           | `时间间隔，数据库中按照bigint存储，ORM中获取的值为datetime.timedelta类型` |
| `FloatField(Field)`                                          | `浮点型`           |                                                              |
| `DecimalField(Field)`                                        | `10进制小数`       |                                                              |
| `BinaryField(Field)`                                         | 二进制类型         |                                                              |

```python
# 注：当model中如果没有自增列，则自动会创建一个列名为id的列
from django.db import models


class UserInfo(models.Model):
	# 自动创建一个列名为id的且为自增的整数列
	username = models.CharField(max_length=32)

class Group(models.Model):
	# 自定义自增列
	nid = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32)
```

#### 自定义无符号整数字段

```python
class UnsignedIntegerField(models.IntegerField):
	def db_type(self, connection):
		return 'integer UNSIGNED'
```

PS: 返回值为字段在数据库中的属性，`Django`字段默认的值为：

#### Django字段默认的值

| `Django`字段 | 类型 | 描述 |
| --------- | ------- | -------------- |
| `AutoField` | `integer` | `AUTO_INCREMENT` |
| `BigAutoField` | `bigint` | `AUTO_INCREMENT` |
| `BinaryField` | `longblob` | |
| `BooleanField` | `bool` | |
| `CharField` | `varchar(%(max_length)s)` | |
| `CommaSeparatedIntegerField` | `varchar(%(max_length)s)` ||
| `DateField` | `date` | |
| `DateTimeField` | `datetime` ||
| `DecimalField` | `numeric(%(max_digits)s, %(decimal_places)s)` | |
| `DurationField` | `bigint` | |
| `FileField` | `varchar(%(max_length)s)` | |
| `FilePathField` | `varchar(%(max_length)s)` | |
| `FloatField` | `double precision` | |
| `IntegerField` | `integer` | |
| `BigIntegerField` | `bigint` | |
| `IPAddressField` | `char(15)` | |
| `GenericIPAddressField` | `char(39)` | |
| `NullBooleanField` | `bool` | |
| `OneToOneField` | `integer` | |
| `PositiveIntegerField` | `integer` | `UNSIGNED` |
| `PositiveSmallIntegerField` | `smallint` | `UNSIGNED` |
| `SlugField` | `varchar(%(max_length)s)` | |
| `SmallIntegerField` | `smallint` | |
| `TextField` | `longtext` | |
| `TimeField` | `time` | |
| `UUIDField` | `char(32)` | |
#### 参数

| 参数        | 描述                                                         | 注意事项                                                     |
| ----------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| null        | 如果为True，`Django` 将用NULL 来在数据库中存储空值。         | 默认值是 False.                                              |
| blank       | 如果为True，该字段允许不填。默认为False。                    | 要注意，这与 null 不同。null纯粹是数据库范畴的，而 blank 是数据验证范畴的。<br/>如果一个字段的blank=True，表单的验证将允许该字段是空值。如果字段的blank=False，该字段就是必填的。 |
| default     | 字段的默认值。可以是一个值或者可调用对象。                   | 如果可调用 ，每有新对象被创建它都会被调用。                  |
| primary_key | 如果为True，那么这个字段就是模型的主键。                     | 如果你没有指定任何一个字段的primary_key=True，<br/>`Django` 就会自动添加一个`IntegerField`字段做为主键，所以除非你想覆盖默认的主键行为，<br/>否则没必要设置任何一个字段的primary_key=True。 |
| unique      | 如果该值设置为 True, 这个数据字段的值在整张表中必须是唯一的  |                                                              |
| choices     | 由二元组组成的一个可迭代对象（例如，列表或元组），用来给字段提供选择项。 | 如果设置了choices ，默认的表单将是一个选择框而不是标准的文本框，<br/>而且这个选择框的选项就是choices 中的选项。 |

#### 元信息

```python
class UserInfo(models.Model):
	nid = models.AutoField(primary_key=True)
	username = models.CharField(max_length=32)
	class Meta:
		# 数据库中生成的表名称 默认 app名称 + 下划线 + 类名
		db_table = "table_name"

		# 联合索引
		index_together = [
      	("pub_date", "deadline"),
      ]

		# 联合唯一索引
		unique_together = (("driver", "restaurant"),)

		# admin中显示的表名称
		verbose_name

		# verbose_name加s
		verbose_name_plural
```



### 数据库迁移

```python
python manage.py makemigrations  # 将你的数据库变动记录到文件中，并不会帮你创建一张表
python manage.py migrate  # 创建表，将你的数据库变动正在同步到数据库中
```



更改类中字段
　　修改模型层里面的跟表相关的所有的数据，只要你修改了就必须重新执行数据库迁移命令，同时如果你的数据库中有记录，那么需要为原有记录的新增字段添加默认值（default = '默认值'）或者设置可为空（null = TRUE）。





## 新增表记录

### 基于`Queryset`**：**

```python
# 有返回值，并且就是当前被创建的数据对象
models.对应表的类名.objects.create(字段名 = 值，……)
```

 

### **基于对象：**

```python
 # 先实例化产生对象，然后调用save方法保存
object = models.对应表的类名(字段名 = 值，……)

object.save()
```



## 查询表记录

### 查询`API`

| 方法                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| all()               | 查询所有结果                                                 |
| `filter(**kwargs)`  | 它包含了与所给筛选条件相匹配的对象，filter内可以放多个限制条件，多个条件之间是and关系 |
| `get(**kwargs)`     | 返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。 |
| `exclude(**kwargs)` | 它包含了与所给筛选条件不匹配的对象                           |
| order_by(*field)    | 对查询结果排序，默认是以括号里的值升序排列，在值前面加上负号-就是降序排列 |
| reverse()           | 对查询结果反向排序，前面要先有排序才能反向                   |
| count()             | 返回数据库中匹配查询(`QuerySet`) 的对象数量                  |
| first()             | 返回第一条记录                                               |
| last()              | 返回最后一条记录                                             |
| exists()            | 如果`QuerySet`包含数据，就返回True，否则返回False            |
| values(*field)      | 返回一个`ValueQuerySet`——一个特殊的`QuerySet`，运行后得到的并不是一系列model的实例化对象，而是一个可迭代的字典序列 |
| values_list(*field) | 它与values()非常相似，它返回的是一个元组序列（列表套元祖），values返回的是一个字典序列 |
| distinct()          | 从返回结果中剔除重复纪录 去重的对象必须是完全相同的数据才能去重（例如若id不同但其他所有都相同的记录不会被删除，但我们先指定相同的字段，再针对此删除相同的数据） |

### 基于双下划綫查询

| 语法                 | 字段名__查询条件=值      |
| -------------------- | ------------------------ |
| `__gt`=值            | 大于……的                 |
| `__gte`=值           | 大于等于……的             |
| `__lt`=值            | 小于……的                 |
| `__lte`=值           | 小于等于……的             |
| `__in=[值1,值2，……]` | 在列表的值中的           |
| __range=[x,y]        | 在x和y范围内的           |
| `__year`=值          | 年份                     |
| `__contains`=值      | 包含……的（大小写敏感）   |
| `__icontains`=值     | 包含……的（大小写不敏感） |
| `__startswith`=值    | 以……开头的               |
| `__endswith`=值      | 以……开头的               |

## 修改表记录

```python
models.对应表的类名.objects.filter(字段名 = 值[查找条件]).update(字段名=值[更改后的数据])

# 基于对象
object = models.对应表的类名.objects.filter(字段名 = 值[查找条件]).first()

object.字段名 = 值

object.save()
```



## 删除表记录



```python
# 基于Queryset
models.对应表的类名.objects.filter(字段名 = 值[查找条件]).delete()

# 基于对象
object = models.对应表的类名.objects.filter(字段名 = 值[查找条件]).first()

object.delete()
```

在 `Django` 删除对象时，会模仿 `SQL` 约束 ON DELETE CASCADE 的行为，换句话说，删除一个对象时也会删除与它相关联的外键对象。

如果不想级联删除，可以设置为:



```python
publisher = models.ForeignKey(to='Publisher', on_delete=models.SET_NULL, blank=True, null=True)
```





[模型层之ORM、数据库和单表操作](https://www.cnblogs.com/moonzier/p/11221443.html)