## pgzero语法

```python
screen.draw.filled_circle((400,y),30,'red')
```

没有常见的 if __name_ == '__main__' 这样的真正执行命令块，那是因为 pgzrun 已经封装了这些操作

没有 for, while 这样的循环，只是定义了如何更新、画图的方法，那同样是因为 pgzrun 在后台会为我们执行这样的循环，不需要显式来写