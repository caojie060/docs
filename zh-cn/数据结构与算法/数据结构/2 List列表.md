# List链表

a=[1,2,3,4,5]

查找a[0]

增加a.append(6)

更新a[0]=9

删除a.pop(0)

a.pop默认删除最后一个值

a.remove

常用函数

len(a)

max(a)

min(a)

a.reverse()倒叙

a.clear()

in某个元素是否存在于元组中

3 in a

slice 切片

a[0:3]从0开始不包括3

a[2:5]

a[-1]

a[2:-1]

a[:]所有元素

a[2:]

迭代,遍历

1.for x in a:

​	print(x)

2.for index in range(len(a)):

​	print(a[index])

高级操作

list comprehersion

[i*i for i in a]

[exprenssion if condition else statment for i in iterable]

[i*i if i<3 else i for i in a]

等价于

for i in a:

​	if i < 3:

​		b[i]=i*i

​	else:

​		b[i]=i