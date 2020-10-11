# linkedlist链表

```python
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
```

### 节点实现

```Python
class SingleNode(object):
    """单链表的结点"""
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None
```

### 单链表的操作

- is_empty() 链表是否为空
- length() 链表长度
- travel() 遍历整个链表
- add(item) 链表头部添加元素
- append(item) 链表尾部添加元素
- insert(pos, item) 指定位置添加元素
- remove(item) 删除节点
- search(item) 查找节点是否存在

### 单链表的实现

```python
class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print cur.item,
            cur = cur.next
        print ""
        
    
```

**头部添加元素**

[![单链表表头插入元素.png](http://ww1.sinaimg.cn/large/006qX6GLgy1g8xlq8aq48j314i06ydi7.jpg)](http://ww1.sinaimg.cn/large/006qX6GLgy1g8xlq8aq48j314i06ydi7.jpg)

```Python
    def add(self, item):
        """头部添加元素"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        # 将新节点的链接域next指向头节点，即_head指向的位置
        node.next = self._head
        # 将链表的头_head指向新节点
        self._head = node
```

**尾部添加元素**

```Python
    def append(self, item):
        """尾部添加元素"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
```

**指定位置添加元素**

[![单链表指定位置添加元素.png](http://ww1.sinaimg.cn/large/006qX6GLgy1g8xlqgynn4j31bm086jun.jpg)](http://ww1.sinaimg.cn/large/006qX6GLgy1g8xlqgynn4j31bm086jun.jpg)

```Python
    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length()-1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node
```

**删除节点**

[![单链表删除节点.png](http://ww1.sinaimg.cn/large/006qX6GLgy1g8xlqpbhclj319007ywhd.jpg)](http://ww1.sinaimg.cn/large/006qX6GLgy1g8xlqpbhclj319007ywhd.jpg)

```python
    def remove(self,item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
```

**查找节点是否存在**

```python
    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
```

**测试**

```python
if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    print "length:",ll.length()
    ll.travel()
    print ll.search(3)
    print ll.search(5)
    ll.remove(1)
    print "length:",ll.length()
    ll.travel()
```

## Python实现

接下来我们使用Python 3来构建单链表数据结构，首先需要定义一个节点类：

```python
class Node:
    '''单链表的节点'''
    def __init__(self, value):
        self.value = value  # 节点的信息域
        self.next = None    # 节点的指针域

    def __repr__(self):
        return 'Node({!r})'.format(self.value)
```

然后定义单链表类：

```python
class SinglyLinkedList:
    def __init__(self, node=None):
        '''创建一个单链表对象时，如果不传入头节点，则创建空链表'''
        self.__head = node
```

### (1) 判断是否空链表

只需要判断单链表的`__head`属性是否为None即可，如果是None表示没有头节点，则是空链表

```python
def is_empty(self):
    '''判断是否为空链表'''
    return self.__head is None
```

### (2) 求链表的长度

定义一个游标`cur`，用来表示遍历到的当前节点，初始时等于链表的头节点（即`cur = self.__head`）。`count`变量用于统计已遍历了多少个节点，初始时等于0。当`cur`移动到尾节点时，`cur.next == None`，此时再将`cur`往后移动时，需要退出while循环

该方法最后返回`count`即可

```python
def length(self):
    '''求链表的长度'''
    cur = self.__head  # 游标，用来表示当前节点
    count = 0  # 用来统计已遍历的节点数目

    # 1. 如果是空链表，self.__head为None，则cur为None，不会进入循环体，最后返回 count = 0，符合
    # 2. 如果不是空链表，当cur移动到尾节点时，cur.next 是None，循环体中的 cur = cur.next 会让 cur = None，继续往后移动时会退出循环
    while cur is not None:
        count += 1
        cur = cur.next  # 向后移动游标

    return count
```

### (3) 遍历链表

逻辑跟求长度一样，注意，这里使用生成器语法，将每个节点的值产出供客户代码使用

```python
def travel(self):
    '''遍历整个链表'''
    cur =
                                
                            
```

阅读全文

 [Python3数据结构02 - 单向链表](https://madmalls.com/blog/post/singly-linked-list/)