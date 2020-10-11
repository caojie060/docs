# Heap堆(大堆,小堆)

大堆pop返回最大值

小堆pop返回最小值

Java:PriorityQueue

Python:heapq

```python
from heapq import heapify,heappush,heappop
```

默认是小堆

heapify()

heappush()

heappop()

n largest()

n smallest()

a=[1,2,3]

heapify(a)小堆

小堆头一定是最小值,其他不一定

heappush(a,4)向小堆a中添加4

heappop(a)弹出最小值,同时剩余值得最小值变成头

nlargest(2,a)找前两个最大值

nsmallest(2,a)

ლ(′◉❥◉｀ლ)python默认是没有大堆的

建立大堆的方法

1,2,3

a=[-1,-2,-3]

heapify(a)

[-3,-2,-1]

heappush(a,-1*4)

[-4,-3,-2,-1]

heappop(a)

-4

-1*heappop(a)

4