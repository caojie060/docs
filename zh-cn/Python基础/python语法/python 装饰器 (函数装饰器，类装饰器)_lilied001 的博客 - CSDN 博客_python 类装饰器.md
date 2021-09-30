> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/lilied001/article/details/80593475)

只要实现此

obj（func）（）
===========

模式，这个 obj 就叫一个装饰器

------------------------------> 参考 https://cloud.tencent.com/developer/article/1114856  
[https://www.cnblogs.com/lianyingteng/p/7743876.html](https://www.cnblogs.com/lianyingteng/p/7743876.html)

> 函数装饰器

```
例子
---
def decorator(func):
    def inner(*args, **kwargs):
        print('before...........')
        res = func(*args, **kwargs)
        print('after............')
        return res
    return inner

@decorator
def run():
    print('run...............')
    return 0

if __name__ == "__main__":
    run()
    run.__name__
    # 此时decorator叫做装饰器
------------------------------------------
before...........
run...............
after............
inner
```

注意: inner 的返回值要与 func 的一致, 并且 inner 与 func 参数相同

### 为了不改变被装饰函数或类的性质, 添加 functools.wrap 装饰器

```
from functools import wraps

def decorator(func):
    @wraps(func)
    def inner():
        print('before...........')
        res = func()
        print('after............')
        return res
    return inner

@decorator
def run():
    print('run...............')
    return 0

if __name__ == "__main__":
    run()
    print(run.__name__)
------------------------------------------
before...........
run...............
after............
run
```

### 带参数的装饰器 (3 层)

```
from functools import wraps
from datetime import datetime

def start():
    return datetime.now()

def end():
    return datetime.now()


def Filter(start_time, end_time):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            s = start_time()
            res = func(*args,**kwargs)
            e = end_time()
            print("耗时{}".format((e-s).total_seconds()))
            return res
        return inner

    return decorator



@Filter(start, end)
def run():
    for i in range(10000):
        for j in range(100):
            print(j)
    return 0

if __name__ == "__main__":
    run()
```

##### 变种 (截取自 flask @route())

![](https://img-blog.csdn.net/20180616154217937?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xpbGllZDAwMQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

> 类装饰器

```
class decorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('before............')
        res = self.func(*args, **kwargs)
        print('after............')
        return res


@decorator
def run():
    print('run............')

if __name__ == "__main__":
    run()
-----------------------------------
before............
run............
after............
```