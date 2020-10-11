# pandas入门教程

## 0.加载数据

### read_csv() 来加载 CSV 文件

```python
df = pandas.read_csv('music.csv')
```

其中变量 DF 是 Pandas 的 DataFrame 类型

### read_excel() 读取EXCEL 文件中数据

```python
df = pandas.read_csv('music.xls')
```



## 1.serise

```python
import pandas as pd

a=pd.Series([1,2,3,4,5])

a=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'],dtype=float)
```

numpy

```python
import numpy as np

a=np.arange(5)
b=pd.Series(a)
```

字典

```python
dic = {'name':'lee',
		'sex':'man',
		'age':18
}
a=pd.Series(dic)
a=pd.Series(dic,index=['name','color'])
a=pd.Series(5,[0,1,2])
```



## 2.DataFrame

DataFrame是一个[表格型]的数据结构,

DataFrame由按一定顺序排列的多列数据组成.设计，

初衷是将Series的使用场景从一维拓展到多维。

其实DataFrame就是由多个Series组成的，

因此可以说DataFrame是Series的容器。

### DataFrame由3部分组成

**行索引:index**

**列索引:columns**

**值:values**

长这个样子

![img](https://pic1.zhimg.com/80/v2-926421856fd3d26ec8e98c3cec1b8ef4_720w.jpg)

```python
a=np.random.randint(0,10,(2,3))
pd.DataFrame(a,index=['a','b'],columns=['x','y','z'])

population={
    'beijing':1655,
    'shanghai':1655,
    'guangzhou':11568
}
a=pd.Series(population)
pd.DataFrame(a)

a=pd.DataFrame(a,columns=['population'])

gdp={
    'beijing':243251,
    'shanghai':5251235,
    'guangzhou':2353251
}
pd.DataFrame({'gdp':gdp})

a=pd.DataFrame({'populat:population',gdp':gdp})
```

### DataFrame创建方式

#### 使用ndarry创建

```python
#  DataFrame的参数组成 pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
# index指定行索引，columns指定列索引，若不写，则默认从0开始，size指定行数和列数
df = pd.DataFrame(data=np.random.randint(1,10,size=(2,4)),index=["a","b"],columns=["A","B","C","D"])
```

#### 使用字典创建

```python
dic = {"name":["张三","李四","王五"],"age":[1,2,3]}
# key为列的索引，行索引则默认从0开始
pd.DataFrame(dic)
```

可以看出，以字典形式创建，DataFrame以字典的key作为每一列的列名，以字典的值(一个数组)作为每一列的值，DataFrame会自动加上每一行的索引

## 3.属性

```python
a.values //值
a.index //行
a.columns //列
a.shape //几行几列（行，列）
a.size //大小，行数X列数
a.dtypes
```

## 4.索引，切片

### 索引

#### 隐式索引的操作

```python
df = pd.DataFrame(data=np.random.randint(1,10,size=(3,4)))
```

![img](https://pic3.zhimg.com/80/v2-16f736be9514824004eacbf95e2ddd06_720w.png)

- `df[0][0]` `df[列][行]`，获取隐式索引单个元素
- `df[0:2]` 对行的切片操作，获取的是0和1行，顾头不顾尾
- `df[[0,1]]` 对列的操作，获取第一列和第二列，跟`Series`不同
- `df.iloc[0:2,0:2]` iloc对于隐式索引的操作，获取前两行和前两列组成的区域，逗号前式行，逗号后是列
- `df.iloc[[0,1],[0,1]]` iloc对于隐式索引的操作，获取前两行和前两列组成的区域

```python
a=pd.DataFrame({'population':population,'gdp':gdp})

```

#### 显式索引的操作

```python
df1 = pd.DataFrame(data=np.random.randint(1,10,size=(3,4)),index=["a","b","c"],columns=["A","B","C","D"])
```

![img](https://pic3.zhimg.com/80/v2-02d9c8a0baae3768e08138136c9d7c1a_720w.png)

- `df["A"]` 或 `df.A` 获取单列，类似于字典的操作
- `df['A']['a']`获取单个元素，先列后行 `df[列][行]`
- `df["a":"b"]`获取是a到b行,包含b行
- `df[["A","B"]]`获取A列和B列
- `df.loc["a":"b","A":"B"]` loc对于显式索引的操作，`df[行区域，列区域]`
- `df.loc[["a","b"],["A","B"]]`loc对于显式索引的操作，结果同上

总结

1.DataFrame相对于Series而言，多了对于列的操作，但是是建立在Series基础之上。

2.loc是对于显式索引的相关操作(对于标签的处理)，iloc是针对隐式索引的相关操作(对于整数的处理)。

3.`df[0:2]`切片操作是针对行而言，对于`df["A"]`索引操作是对于列而言；获取单个元素先列后行，`df[列][行]`；loc和iloc操作，逗号前是行区域或行列表，逗号后是列区域或列列表。

### 取列

```python
a['gdp']
a.gdp
```

我们可以使用行标签来获取一列或者多列数据。表格中的下标是数字，比如我们想获取第 1、2 行数据，可以使用 `df[1:3]` 来拿到数据。

Pandas 的利器之一是索引和数据选择器。我们可以随意搭配列标签和行标签来进行切片，从而得到我们所需要的数据

### 取行

```python
a.loc['beijing']
a.loc[['beijing','shanghai']]
a.loc['beijing':'shagnhai']
a.iloc[0]
a.iloc[[0,2]]
```

### 取值

```python
a.loc['beijing','gdp']
a.iloc[0,1]
a.values[0][1] //变成numpy的取值
a.iloc[:2,:]
a.gdp>0
a[a.gdp>0]
a.gdp==243251
a[a.gdp==243251]
```

### 过滤数据

```python
df[df['Genre']=='Jazz']
df[df['Listeners']>1800000]
```



## 5.赋值

```python
a.iloc[0,1]=0
```

### 插入列

```python
s=pd.Series([1,2,3],index=['beijing','shanghai','guangzhou'])
a["E"]=s
```



## 6.数据查看

```python
dates=pd.date_range(start='2020-1-1',periods=6)
df=pd.DataFrame(np.random.randint(0,10,(6,4)),index=dates,columns=['A','B','C','D'])
df.describe() //描述整体结构
df.info()
df.head()
df.head(2)
df.tail()
df.tail(2)
df.T //转置,行名变成列名,列名变成行名
df.sort_index(axis=0,ascending=False) //按行排序,从大到小排列
df.sort_index(axis=1) //按列排序,默认从小到大
df.sort_values('B') //按照B列的值的大小排序
```



```python
#行数、列数
df.shape[0]
df.shape[1]
#前几行，后几行，默认为5
df.head()
df.tail(3)
#数据汇总统计
df.describe()
#数据概况
df.info()
#列名
df.columns
#数据类型
df.dtypes
#各列平均值
df.mean()
```



## 7.计算

```python
a=pd.DataFrame([1,2,3]) //创建三行一列的数据
a-2 //每个元素都减2
b=pd.DataFrame([1,2,3])
a+b //对应元素相加

b=pd.DataFrame(np.random.randint(10,size=(1,3))) //创建一行三列的数据
c=a@b //矩阵乘法

a=pd.DataFrame(np.random.randint(0,20,(2,2))) //创建二行二列的数据
b=pd.DataFrame(np.random.randint(0,20,(3,3))) //创建三行三列的数据
a+b
a.add(b,fill_value=0) //填充值
```



## 8.处理缺失值

```python
a=pd.DataFrame(np.arange(9).reshape((3,3)))
a.iloc[:2,2]=np.nan //设为空
a.dropna() //把有缺失值的行扔掉

a=pd.DataFrame(np.arange(9).reshape((3,3)))
a.iloc[:2,2]=np.nan //设为空
a.dropna(axis=1) //把有缺失值的列扔掉

a.dropna(axis=1,how='any') /any只要有缺失值,这一列都扔掉
a.dropna(axis=1,how='all') /all只有这一列全是缺失值,才扔掉这一列
```

### 改缺失值

```python
# 在np中
None是python自带的,其类型为object,
因此,None不能参与到人任何计算中(NoneType)
np.nan(NaN) 是浮点类型(float),能参与到计算中.但计算的结果总是NaN
# 在pandas中
把None和np.nan都视作np.nan
```

```python
a=pd.DataFrame(np.arange(9).reshape((3,3)))
a.iloc[:2,2]=np.nan //设为空
a.fillna(value=0) //自动把所有缺失值用0填充
```

### 处理空值

查看哪些行或列为存在缺失值

- **isnull() 有缺失值则返回True**
- **notnull() 没有缺失值则返回True**
- **isnull().any(axis=1) axis=1是代表行，0代表列，一行中只要有一个空值则返回True**
- **notnull().all(axis=1) 一行中所有不为空则返回True**

```python
df3.notnull()
```

![img](https://pic2.zhimg.com/80/v2-5f4703df9742ca5e0a2e30ac4e217d29_720w.jpg)

```python
df3.notnull().all(axis=1)
```

![img](https://pic4.zhimg.com/80/v2-30e1c32489b8826f33a3329693ea930f_720w.png)

```python
print(df.isnull())
```

如果我想知道哪列存在空值，可以使用 df.isnull().any()

```python
print(df.isnull().any())
```

### 删除空值的行

删除有缺失值的行或列

**df.dropna() 删除有缺失值的整行或整列**

**f3.dropna的参数：(axis=0, how='any', thresh=None, subset=None, inplace=False)**

- **axis=0** 这里的0代表行，在drop操作中0代表行，1代表列，根据axis的设置决定是对行还是列
- **how='any'** how是删除方式，any只要一行或一列中有一个缺失值就删除，还有一个all代表的意思是，一行或一列中所有的都为缺失值才删除，常用的是any
- **inplace=False** inplace代表操作是否对原数据进行覆盖，False代表不在原数据上修改，而是复制出一份，True代表在原数据上修改。

```python
df3.dropna()
```

![img](https://pic2.zhimg.com/80/v2-2e2fa5c069f1110a839d6e5d0f07c1ad_720w.jpg)

```python
df.dropna()
# 将值填充为 0
pd.fillna(0)
```

填充缺失值

**df.fillna() 对缺失值进行填充**

**df.fillna参数：(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, \**kwargs)**

- **value** 填充的值,也可以是字典
- **axis** 1 代表行，0代表列 ，结合method使用，决定了填充是按照行还是列
- **inplace** inplace代表操作是否对原数据进行覆盖，False代表不在原数据上修改，而是复制出一份，True代表在原数据上修改。
- **method** 分为四种填充方式：'backfill', 'bfill', 'pad', 'ffill' 其中pad / ffill表示用前面行/列的值，填充当前行/列的空值； backfill / bfill表示用后面行/列的值，填充当前行/列的空值。

需求1：把缺失值都填充为6

```python
df3.fillna(6)
```

![img](https://pic2.zhimg.com/80/v2-58e93e48a8daa6d133c49e451e8b4c6d_720w.jpg)

需求2：把缺失值按照列方向,填充为前面的那个值

```python
df3.fillna(axis=0,method="ffill") # 改成pad也可以，axis确定了填充的方向，如果不写，默认是列
```

![img](https://pic1.zhimg.com/80/v2-d6563665d5de2243df2e18c1fb3a14c8_720w.jpg)

需求3：把缺失值按照行方向，填充为后面的那个值

```python
df3.fillna(axis=1,method="bfill")# 改成backfill也可以，axis确定了填充的方向，如果不写，
```

![img](https://pic1.zhimg.com/80/v2-a21cc22d0a5d2242a3b282f9cbdd4a2c_720w.jpg)

**重复值处理**

df.duplicated() 查看重复行

df.duplicated()的参数：**(**subset**=None,** keep**='first')**

- **subset** 指定是哪几列重复，默认是所有的列
- **keep** 有{'first', 'last', False}几种方式, 默认 'first'

1. first 将重复项标记为“`True`”，除了第一次出现
2. last：将重复项标记为``True`，除了最后一次出现
3. False：将所有重复项标记为“True”

直接通过示例就能明白了

创建一个DataFrame

```python
dic = {"A":[1,1,1,5,9],"B":[5,5,6,7,7],"C":[6,6,5,2,8]}
df = pd.DataFrame(dic)
df
```

![img](https://pic1.zhimg.com/80/v2-7feb5e10513a9949c07c7c2a869c94e0_720w.png)

需求1：把所有列重复的的行标注出来

```python
df.duplicated() # keep默认为first，subset默认为所有的列，意思就是所有的列同时重复才显示
```

![img](https://pic2.zhimg.com/80/v2-68462469c4bdbe43ed0deba4bb1569b9_720w.png)

我们发现第一行和第二行所有列一样，根据keep设置的first的原则，第一次出现的不显示为True，其余的显示为True，这里的True代表重复的意思，我们只要把True的删除，就可以保留唯一值了。

需求2：把A和B两列同时重复的行显示，要求最后的那个不标注为True

```python
df.duplicated(subset=["A","B"],keep='last')
```

![img](https://pic1.zhimg.com/80/v2-c29d30a3a1ec608d68be6e4b74e7fdc4_720w.png)

我们发现A和B两列同时重复的还是第一行和第二行，设置keep为last之后，第一行显示为重复行，为True，第二行显示为False。

需求3：把A和B两列重复的行全部显示为True

```python
df.duplicated(subset=["A","B"],keep=False) 
```

![img](https://pic1.zhimg.com/80/v2-0c3040dc09b7a3e828d601dfb1214d58_720w.png)

keep设置为False之后，所有重复的行都会显示为True

删除重复行，保留唯一值

对于重复行的处理，我们一般都是找出重复行，只保留一个，删除其他的，那duplicated通过keep设置来让用户自由选择是保留第一个，还是最后一个，通过显示True来实现该功能

**df.drop_duplicates() 删除重复值**

df**.**drop_duplicates参数：**(**subset**=None,** keep**='first',** inplace**=False)**

前两个就不说了，跟duplicated一样

**inplace=False**不在原值上删除，而是复制出一份进行操作，改成True则直接对df进行删除操作，这个也是pandas谨慎的地方，大部分操作都不是在原值上进行的，如果需要可以通过inplace进行设置

需求：删除所有列同时重复的行，默认保留第一个就行

```python
df.drop_duplicates() # 把返回True给删除，很简便
```

![img](https://pic2.zhimg.com/80/v2-d0c5778d2dc30c8f9dd4fa7acf8705c5_720w.png)

注意：此操作之后，原df并没有发生变化，有两种处理方式，第一种：把删除后的数据赋值给新的变量，第二种：直接修改inplace=True。

**排序**

- **df.sort_index() 按索引排序**
- **df.sort_value() 按值排序**

**常用的是纵向排序，也就是默认的axis=0的相关操作**

**sort_index()参数(**axis**=0,** level**=None,** ascending**=True,** inplace**=False,** kind**='quicksort',** na_position**='last',** sort_remaining**=True,** by**=None)**

- **axis=0 纵向排序（行索引），axis=1 横向排序（列索引）**
- **ascending 排序方式，True为升序，False为降序**
- **kind排序方式，默认是quicksort 快排**

```python
df=df.take(np.random.permutation(5),axis=0)
df
```

![img](https://pic3.zhimg.com/80/v2-7f21ff4d72674c0e7f8da7ac1c230262_720w.png)

```python
df.sort_index()
```

![img](https://pic3.zhimg.com/80/v2-d0c848fed0c26111c95a2878c473301e_720w.png)

**df.sort_values()**

**参数：(**by**,** axis**=0,** ascending**=True,** inplace**=False,** kind**='quicksort',** na_position**='last')**

- **axis=0 纵向排序（index），axis=1 横向排序（columns）**
- **ascending = True 升序，False降序**
- **inplace 是否在原值上直接修改，False是重新复制出一份，原frame不变**
- **kind排序方式** {'quicksort', 'mergesort', 'heapsort'} 默认是quicksort 快排，mergesort归并排序，heapsort 堆排序

对某列进行排序

```python
df.sort_values(by="C")
```

![img](https://pic1.zhimg.com/80/v2-2f8d6741df90c005a1f2c5d9d6d3f5f0_720w.png)

```python
df.sort_values(by=["C","B"],axis=0,ascending=[False,True])
```

![img](https://pic1.zhimg.com/80/v2-314fe4229d875113c4995e9e43c9aca4_720w.png)

对行进行排序

```python
df.sort_values(by=[0,2],ascending=[False,True],axis=1)
```

![img](https://pic3.zhimg.com/80/v2-e50ff6ccf66da469063e8727cddd5076_720w.png)

注：当存在多列或多行排序时，是有优先顺序的，根据列表中的优先顺序，在前面的优先级高，越往后优先级越低。



- **np.random.shuffle(x)** 打乱原数组的顺序，shuffle直接在原数组进行修改
- **np.random.permutation(x) x可以为数组或者一个数，**当为数组时,打乱原数组的顺序，不在原数组上进行，返回新的数组，不改变自身数组；当x为一个数时，则会随机排列np.arange(x)。

```python
arr = np.array([[1,2,3],[4,3,2],[5,3,8]])
np.random.shuffle(arr) # shuffle洗牌
arr
```

![img](https://pic1.zhimg.com/80/v2-6f1222c3d68e4b05ef5302d874c7dd18_720w.png)

```python
arr1 = np.array([[1,2,3],[4,3,2],[5,3,8]])
np.random.permutation(arr1) # permutation 随机排列数组
arr1
```

![img](https://pic3.zhimg.com/80/v2-2725801ee93f4bb976fc00249f7af496_720w.png)

```python
np.random.permutation(10)
```

![img](https://pic2.zhimg.com/80/v2-1463fa399944049057dc4810983b7231_720w.png)

- **df.take()**

df**.**take参数：**(**indices**,** axis**=0,** convert**=None,** is_copy**=True,** ***\***kwargs**)**

**axis=0 纵向排序，axis=1横向排序，默认为0，大部分情况下都是纵向排序**

**与permutation联合使用，可实现随机采样功能**

**示例数据**

```python
df
```

![img](https://pic1.zhimg.com/80/v2-b9fa17d589ad5bf9d04dadf6a3638950_720w.png)

对行进行随机排序，按照行索引

permutation中的x，类似于range(5),只能取到0 1 2 3 4，因此在跟take联合使用时，x的大小要跟df的行数相一致

```python
df.take(np.random.permutation(5),axis=0)
```

![img](https://pic1.zhimg.com/80/v2-673c46af8cfeefb461b5f91474041a5c_720w.png)

```python
df.take(np.random.permutation(3),axis=1)
```

![img](https://pic4.zhimg.com/80/v2-768681bff7a1f17c46c76ee159141c63_720w.png)

**替换**

**df.replace()**

df**.**replace参数：**(**to_replace**=None,** value**=None,** inplace**=False,** limit**=None,** regex**=False,** method**='pad')**

- **to_palce:** 被替换的对象
- **value:**替换成新的值
- **inplace:** True原值上修改，False复制出一份修改
- **method** {'pad', 'ffill', 'bfill', `None`}四种替换方式，默认是“pad”

单值替换

```python
df.replace(1,10,inplace=True)
```

![img](https://pic4.zhimg.com/80/v2-065b4e1337d610f2adbc6f692799aa23_720w.png)

多值替换

```python
1 使用字典
dic={10:"满分",5:"中等"}
df.replace(dic) 
# 或者 使用列表
df.replace([10,5],["满分","中等"])
```

![img](https://pic2.zhimg.com/80/v2-c0ccc8feba3959ed9530ffc29977f915_720w.png)

注：DataFrame中无法使用method和limit参数

**映射与运算**

- **map() 可以实现映射和充当运算工具,map()不是df的函数，而是Series的，因为它只针对某一列进行操作**
- **apply() 只可以作为运算工具**

**map()**

使用map通过字段映射，新增一列

```python
emp_dic = {"姓名":["张三","李四","王五"],"dep_id":[1,2,3]}
emp = pd.DataFrame(emp_dic)
# 映射关系表
dic = {"张三":"Hurry","李四":"Lily","王五":"Tom"}
emp['e_name'] = emp['姓名'].map(dic)
```

![img](https://pic4.zhimg.com/80/v2-1dde0e35383f2999a9ad616ff6db2293_720w.jpg)

使用map作为运算工具

```python
df["up_num"] = df["C"].map(lambda x:x*20)
```

![img](https://pic3.zhimg.com/80/v2-b351337fe67cf058add585ebdc69682a_720w.jpg)

map常跟匿名函数lambda一块使用，当然也可以使用普通函数

```python
def complex(s):
    return s*10
df["up_num1"] = df["C"].map(complex)
```

![img](https://pic2.zhimg.com/80/v2-a163866557b71af8d3e552ef83973961_720w.jpg)

注意：并不是任何形式的函数都可以作为map的参数.只有当一个函数具有一个参数且有返回值,那么该函数才可以作为map的参数

**apply()**

**只能当做运算工具，当运算量很大时，建议使用apply**

```python
df['up_num2'] = df['C'].apply(lambda x:x*5)
```

![img](https://pic3.zhimg.com/80/v2-a3359b2b384040cedec77e9d95168b32_720w.jpg)

## 9.合并对齐

### 级联

根据指定的行或列进行值的拼接，不参与任何计算，只是把多个df变成1个

```python
pd.concat()
参数(objs, axis=0, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=None, copy=True)
```

- `axis=0` 列方向级联拼接，`axis=1`行方向级联拼接，默认为0
- `join`为级联方式，`outer`会将所有的项进行级联（忽略匹配和不匹配），取并集，而`inner`只会将匹配的项级联到一起，不匹配的不级联,取交集。
- `join_axes` `index`对象列表，用于其他n-1轴的特定索引，可以指定根据哪个轴来对齐数据
- `ignore_index` `boolean`，`default False`。如果为`True`，请不要使用并置轴上的索引值。结果轴将被标记为0，...，n-1。如果要连接其中并置轴没有有意义的索引信息的对象，这将非常有用。注意，其他轴上的索引值在连接中不受影响。
- `keys` 序列，默认值无。使用传递的键作为最外层构建层次索引。如果为多索引，应该使用元组。
- `levels` 序列列表，默认值无。用于构建`MultiIndex`的特定级别（唯一值）。否则，它们将从键推断。
- `names：list`，`default`无。结果层次索引中的级别的名称。



```python
a=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'])
b=pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'])
```

### 垂直合并

```python
pd.concat([a,b]) // 列是没有动的
pd.concat([a,b],ignore_index=True) //舍弃原来的行名
```

默认是按照列方向

```python
pd.concat([df1,df2,df3],keys=['x', 'y', 'z']) # ('x', 'y', 'z')元组也可以
```

### 水平合并

行方向进行级联

![img](https://pic2.zhimg.com/80/v2-3e6a84f8c9cd39f59a395325f271df51_720w.jpg)

```python
pd.concat([a,b],axis=1)
```

### join_axes

,可以指定根据哪个轴来对齐数据

```python
#新增df5
dic5={'a':[1,2,3,4],'b':[5,6,7,8]}
df5= pd.DataFrame(dic5,index=[2,3,4,5])
df5
```

df1和df5行方面拼接，只有2和3是一样的

```python
d.concat([df1,df5],axis=1,join_axes=[df1.index])
```

效果类似于按照df1的行索引进行级联，df1的所有行会显示，而df5只能显示匹配上的

### join的用法，取并集或交集

```python
pd.concat([df1,df5],axis=1,join='outer') # 取并集，缺失值显示为NaN
```

![img](https://pic4.zhimg.com/80/v2-f83acdcedeed45cca5fdee7f15389a5b_720w.jpg)

```python
pd.concat([df1,df5],axis=1,join='inner') # 取交集
```

![img](https://pic3.zhimg.com/80/v2-ad936d09153d4ee868ffd3b3c5e44666_720w.jpg)

### df.append()方法，类似于添加的意思

df1**.**append参数：**(**other**,** ignore_index**=False,** verify_integrity**=False,** sort**=None)**

默认是列方向级联，跟concat的默认方式是一样的

```python
df1.append(df2)
```

![img](https://pic2.zhimg.com/80/v2-f51d05df994925ffbbc41b566ed5a909_720w.png)

这种方式操作更简单，后面会经常使用

### 合并

```python
c=pd.Series([1,2,3,4],index=['a','b','c','d'])
a.append(c,ignore_index=True) //填充空值
```

### 对齐合并

```python
a=pd.DataFrame([[2,0],[3,1]],columns=['A','B'])
b=pd.DataFrame([[0,4],[1,5]],columns=['B','C'])
pd.merge(a,b) //以a为基点合并
```

**pd.merge() 跟SQL中的连表查询很像，需要根据合并条件进行两表合并，也就是两个DataFrame需要具有相同的列，然后再进行条件连接合并，而concat单纯根据索引就能进行拼接。**

**参数;**

```python
pd.merge(
    left, right, 
         how='inner', 
         on=None, left_on=None, right_on=None, 
         left_index=False, right_index=False, 
         sort=False,
         suffixes=('_x', '_y'), 
         copy=True, 
         indicator=False, 
         validate=None
        )
```



- `left` 和`right` 定义左表和右表，指定需要连接的两个`DateFrame`
- `how`连接方式 `{'left', 'right', 'outer', 'inner'}`, 默认'`inner`'

1. `inner` 内连接，只连接两个`DataFrame`的交集
2. `left` 左连接，以左表为主，会显示左表全部内容，右表根据左表匹配，未匹配上不显示
3. `right` 右连接，以右表为主
4. `outer` 全外连接，会显示所有内容

- `on` 如果两个`Frame` 指定连接条件的列名一致，可以使用这种方式
- `left_on` 当两个`frame`列名不一致时，根据定义的左表和右表分别定义连接的字段名
- `right_on` 当两个`frame`列名不一致时，根据定义的左表和右表分别定义连接的字段名
- `left_index` 为`True`时，代表以索引作为连接条件
- `right_index` 同上

**示例**

**两个DataFrame列名相同且内容一致，默认自动连接**

```python
dic1 = {"name":["A","B","C","D"],"age":[20,21,22,23]}
dic2 = {"name":["A","C","D","F"],"sex":["M","F","M","M"]}
df1 = pd.DataFrame(dic1)
df2 = pd.DataFrame(dic2)
pd.merge(df1,df2) # name一列相同，自动连接
或者 
pd.merge(df1,df2,on="name") 
```

![img](https://pic3.zhimg.com/80/v2-29d70701e01a8eb791ff0b5155ce454a_720w.png)

**当连接条件列名不一致时，使用lefton 和 right_on**

```python
emp_dic = {"姓名":["张三","李四","王五"],"dep_id":[1,2,3]}
dep_dic = {"id":[1,2],"部门名称":["销售部","运营部"]}
emp = pd.DataFrame(emp_dic)
dep = pd.DataFrame(dep_dic)
pd.merge(emp,dep,left_on="dep_id",right_on="id")

SQL: select * from emp e left join dep d on e.dep_id = d.id
```

![img](https://pic1.zhimg.com/80/v2-627399617b11e06f43b6fab9b34add08_720w.jpg)

**当连接条件为索引时，可以使用left_index 和 righti_ndex**

```python
pd.merge(emp,dep,left_on="dep_id",right_index=True) 
# dep_id 与dep的行索引进行匹配
```

![img](https://pic2.zhimg.com/80/v2-f4683f74f82ce1f0166d35009c555799_720w.jpg)

## 10.分组

**分组聚合基本操作**

1. **split : 先将数据按一个属性分组 (得到 `DataFrameGroupby` / `SeriesGroupby` )**
2. **apply : 对每一组数据进行操作 (取平均 取中值 取方差 或 自定义函数)**
3. **combine: 将操作后的结果结合起来 (得到一个DataFrame 或 Series 或可视化图像)**

**使用groupby进行分组，groups查看分组情况**

df**.**groupby参数：**(**by**=None,** axis**=0,** level**=None,** as_index**=True,** sort**=True,** group_keys**=True,** squeeze**=False,** observed**=False,** ***\***kwargs**)**

实例数据

```python
sale_data = pd.read_excel('./sale_data.xlsx') # 读取Excel文件
```

![img](https://pic3.zhimg.com/80/v2-a0a02d6517c78b34ae6ffe77134ee6b6_720w.jpg)

**需求1：计算各门店的销售数量**

第一步：分组

```python
sale_data.groupby(by="门店编码")
```

![img](https://pic1.zhimg.com/v2-56f76393c9d77d385f96f27ca9c17bc8_r.jpg)

这是一个DataFrameGroupby，主要的功能能是允许你在不额外写循环的情况下, 快速对每一组数据进行操作。

第二步：聚合函数

```python
sale_data.groupby(by="门店编码").sum()
```

如果不指定列，则默认对所有的列都进行聚合计算

![img](https://pic4.zhimg.com/80/v2-34b2c12dfc36673a7eef67519e73db63_720w.jpg)

题目要求对销售数量，因此修改如下：

```python
sale_data.groupby(by="门店编码")["销售数量"]
```

![img](https://pic2.zhimg.com/v2-7b6b270ca7304974010a43461ca6a6f1_r.jpg)

这是一个SeriesGroupBy对象，在不用循环的情况实现聚合计算

```python
sale_data.groupby(by="门店编码")["销售数量"].sum()
```

![img](https://pic4.zhimg.com/80/v2-b5d380059c41f73ace9c25405a3719c7_720w.png)

得到每个门店的销售数量总和是一个Series，聚合函数，还可以使用

**std(标准差)、median(中位数)、min(最大值)、max(最小值)、mean(均值)**

**查看分组情况**

```python
sale_data.groupby(by="门店编码").groups
```

![img](https://pic1.zhimg.com/v2-fea6aaa673a1a33a7edbf0bbbb918e68_r.jpg)

**需求2：计算每个产品的均价，并新增一列到sale_data？**

```python
mean_price = sale_data.groupby(by="产品编码")["单价"].mean()
mean_dic = mean_price.to_dict() # to_dict转换成字典形式
mean_dic
```

![img](https://pic2.zhimg.com/80/v2-89444a6538781f072a4132724b1389cd_720w.png)

```text
sale_data["mean_price"] = sale_data["产品编码"].map(mean_dic)
```

![img](https://pic2.zhimg.com/v2-ebea2f6dd77aae2ce3f252566532b061_r.jpg)



**分组聚合高级操作**

使用groupby分组后,也可以使用transform和apply提供自定义函数实现更多的运算

sale_data.groupby(by="门店编码")["销售数量"].sum()

等价于 sale_data.groupby(by="门店编码")["销售数量"].apply(sum),然后对sum函数进行定义，这里的一些常用聚合函数，是pandas给定义好的，我们根据实际需要可以进行自定义

模拟mean函数实现对于不同产品的平均价格计算

```text
# 定义求平均函数
def my_mean(s): # 使用apply传入的是分组后的，因此是一个Series
    sum_num = 0
    n=0
    for i in s:
        sum_num+=i
        n+=1
    return sum_num/n
# 实现分组聚合计算
sale_data.groupby(by="产品编码")["单价"].apply(my_mean)
```

![img](https://pic2.zhimg.com/80/v2-3de25689937da340e61d76b284777d25_720w.jpg)

```text
# 使用transform返回的是原始数据每一行的值，对原数据结构并没有进行任何修改
sale_data.groupby(by="产品编码")["单价"].transform(my_mean)
```

![img](https://pic1.zhimg.com/80/v2-4b26e31c85d2da8f7cb6dd54f6a74988_720w.png)

**agg聚合操作**

**全称：aggregate**

```text
sale_data.agg({"销售数量":["sum","mean"],"单价":["sum","mean"]}) # aggregate
```

![img](https://pic1.zhimg.com/80/v2-ef52f9be1ed57a57d7d2335a0f0281a4_720w.jpg)

```python
df=pd.DataFrame({
    'key':list('ABCCBA'),
    'data1':range(6),
    'data2':range(20,26)
})
df.groupby('key')
```
Pandas 会将 所选类型的两行数据聚合一组
```python
df.groupby('key').sum() //分组的和
df.groupby('key').mean() //分组的均值
df.groupby('key')['data1'].mean() //先索引,只求某一列的均值
df.groupby('key')[['data1']].mean() //得出Dataframe的均值,得到Dataframe的形式
```

### 自定义的函数

```python
def func(x):
    x['data1'] /= x['data1'].sum()
    return x

df.groupby('key').apply(func) //用函数处理分组后的数据
```



## 11.数据透视表

```python
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head()
titanic.pivot_table('survived',index='sex',columns='class')
```

**DataFrame数据透视**

**这个数据透视表跟Excel中的数据透视功能是一样的，也是分组计算的一种方式，只能这种方式比groupby更加方便快捷，可操作性强，灵活好用。**

**df.pivot_table() 数据透视**

**参数：(**values**=None,** index**=None,** columns**=None,** aggfunc**='mean',** fill_value**=None,** margins**=False,** dropna**=True,** margins_name**='All')**

- **values：** 对哪些列进行聚合计算，可以指定一列或多列
- **index：**根据哪一列进行行方向分组，也就是分组条件，这个是必须要有的，类似groupby中by，或者是Excel数透中的行标签
- **columns:** 根据哪一列进行列方向进行分组，类似于Excel数据透视的列标签
- **aggfunc：**聚合计算方式，也就是对应的聚合函数操作

示例还是上面的销售数据

需求1： 计算每个门店的总销售数量

```text
sale_data.pivot_table(index="门店编码",values="销售数量",aggfunc="sum")
```

![img](https://pic1.zhimg.com/80/v2-2b217949fecf505e47cfad0c8bf54d28_720w.png)

需求2：计算每个门店的每个产品的销售数量

```text
sale_data.pivot_table(index="门店编码",columns="产品编码",values="销售数量",aggfunc="sum")
```

![img](https://pic2.zhimg.com/v2-eeb956e3eca2ec0e74874e08b05c400d_r.jpg)

需求3： 计算2016年每月的每家门店的销售数量和平均单价

```text
sale_data.pivot_table(index=["月份","门店编码"],values=["销售数量","单价"],aggfunc=["sum","mean"])
```

![img](https://pic3.zhimg.com/80/v2-10adbdc2df1e9b05759d3d18adcf91d2_720w.jpg)

**DataFrame交叉表**

**pd.crosstab() 主要用于分类数据计数，类似于列联表**

**参数;(**index**,** columns**,** values**=None,** rownames**=None,** colnames**=None,** aggfunc**=None,** margins**=False,** margins_name**='All',** dropna**=True,** normalize**=False)**

- index 交叉表的行标签
- columns 交叉表的列标签

```text
pd.crosstab(sale_data["门店编码"],sale_data["产品编码"])
```



**总结：**

**1 groupby对原DataFrame进行分组操作，返回DataFrameGroupby或SeriesGroupBy对象，在此基础上可直接进行采用已定义好的聚合函数进行计算。**

**2 使用apply和transform可以实现对于聚合操作的自定义，根据自己独有的规则设计函数，采用apply对已分组后的数据进行计算，返回的是分组后的计算结果。**

**3 apply和transform最大的不同在于，apply返回的分组后的列+分组后的计算结果，他已经改变了原始表的结构，而transfrom返回的是原始分组的列，以及对应的每一行的结果，保留了原始表的所有的。类似于SQL中的聚合函数和开窗函数的区别。**

**4 map是Series的方法，传入的是每个值，而apply既可以用于Series也可以用于DataFrame，并且用于DataFrame时传入的是一个Series，而用于Series时传入的是个值，transform用法与apply一致，只是返回的结果保持跟源数据结构一致。**

**5 aggregate用法比groupby更加简便。**





**pandas是python数据分析三剑客中非常重要 一员，所以写的内容比较细，比较多，希望能够对大家有所帮助。**

## Pandas 可视化





[【数据分析】【pandas】2020自制最全最快入门教程](https://www.bilibili.com/video/BV16E411G7sd)

[国外大神制作的超棒 Pandas 可视化教程](https://zhuanlan.zhihu.com/p/103167104)

 [Python数据分析：Pandas之DataFrame](https://zhuanlan.zhihu.com/p/136211023)

[十分钟想搞定pandas？](https://zhuanlan.zhihu.com/p/56972890)