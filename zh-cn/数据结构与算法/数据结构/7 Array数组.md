# Array数组

顺序表

线性表

根据线性表的实际存储方式，分为两种实现模型：

- **顺序表**，将元素顺序地存放在一块连续的存储区里，元素间的顺序关系由它们的存储顺序自然表示。
- **链表**，将元素存放在通过链接构造起来的一系列存储块中。

Python中的list和tuple两种类型采用了顺序表的实现技术

tuple是不可变类型，即不变的顺序表，因此不支持改变其内部状态的任何操作，而其他方面，则与list的性质类似

在Python的官方实现中，list就是一种采用分离式技术实现的动态顺序表。

这就是为什么用list.append(x) （或 list.insert(len(list), x)，即尾部插入）比在指定位置插入元素效率高的原因。

index

append

pop(i)

insert(i,item)

del

iteration

contains(in)

get slice[x:y]

del slice

set slice

reverse

concatenate

sort

multiply











 [**顺序表**](https://www.cnblogs.com/Dr-wei/p/11857703.html)