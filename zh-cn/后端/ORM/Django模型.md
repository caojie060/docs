# Django-模型

## QuerySet方法

|              | QuerySet方法 | SQL   |      |
| ------------ | ------------ | ----- | ---- |
| 条件         | filter()     | where |      |
| 排除         | exclude()    |       |      |
| 所有数据     | all()        |       |      |
|              | get()        |       |      |
|              | first()      |       |      |
|              | last()       |       |      |
| 新增数据     | create()     |       |      |
|              | delete()     |       |      |
| 查询指定数据 | values()     |       |      |
| 去重         | distinct()   |       |      |
|              |              |       |      |
|              |              |       |      |
| 排序         | order_by()   |       |      |
|              | count()      |       |      |

## 条件查询

### 关系查询

|           |                  |      |
| --------- | ---------------- | ---- |
| __gt=     | 大于             |      |
| __gte=    | 大于等于         |      |
| __lt=     | 小于             |      |
| __lte=    | 小于等于         |      |
| =         | 等于             |      |
| __exact=  | 等于             |      |
| __iexact= | 等于(忽略大小写) |      |

### 模糊查询

|               |            |      |
| ------------- | ---------- | ---- |
| __startwith=  | 以...开头  |      |
| __istartwith= | 忽略大小写 |      |
| __endwith=    | 以...结尾  |      |
| __iendwith=   |            |      |
| __contains=   | 包含       |      |
| __icontains=  |            |      |

### 枚举查询

```python
__in=列表或元组
```

### 区间查询

```python
__range=(min,max)
```

### 空值查询

```python
__isnull=True/False
```

### 逻辑查询

```python
from django.db.models import Q
```

#### 逻辑与and

```python
Q()&Q()
```



#### 逻辑或or

```python
Q()|Q()
```

## 和日期相关的查询

|            |                                                  |      |
| ---------- | ------------------------------------------------ | ---- |
| __date     | 查询时间                                         |      |
| __year     | 根据年份查询                                     |      |
| __month    | 根据月份查询                                     |      |
| __day      | 根据 天 查询                                     |      |
| __hour     | 根据 小时查询                                    |      |
| __minute   | 根据 分钟查询                                    |      |
| __second   | 根据 秒查询                                      |      |
| __week     | 根据第几周来查询 (一年 52-53周)                  |      |
| __week_day | 根据星期 来查询数据 (1 代表星期日， 7 代表星期6) |      |

## 聚合查询

```python

```

## 分组查询

```python

```

