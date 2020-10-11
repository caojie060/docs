# Flask视图

Flask蓝图,它提供了模块化管理程序路由的功能，使程序结构更加清晰、简单易懂！

## 一、蓝图的定义

定义：在蓝图被注册到应用后，所要执行的操作的集合称为蓝图。

当分配请求时，Flask会把蓝图和视图函数关联起来，并生成两个端点对应的URL。

## 二、应用

新建**app.py、news.py、products.py**三个文件（放在同一目录下）。

app.py文件内容如下：

```python
from flask import Flask
import news
import products

app = Flask(__name__)
@app.route('/')
def index():
    return "你好！"
app.register_blueprint(news.new_list)
app.register_blueprint(products.product_list)

if __name__ == "__main__":
    app.run(debug=True)
```

import news,products用来导入另外两个文件，register_blueprint()可以将导入模块里的蓝图对象注册到app中。

**注意：**import可以将两个.py文件关联起来，导入后就能调用里面的类或方法，如import random，导入的也是.py文件。

news.py文件内容如下：

```python
from flask import Blueprint

new_list = Blueprint('news', __name__)

@new_list.route("/news")
def news():
    return "这是新闻版块！"
```

Blueprint()创建一个Blueprint对象，第一个参数可看作该对象的姓名，@new_list.route(“/news”)表示在‘app’网址基础上给蓝图对象创建新的地址。

products.py文件内容如下：

```python
 from flask import Blueprint

product_list = Blueprint('products', __name__)

@product_list.route("/products")
def products():
    return "这是产品版块！"
```

**运行文件，并在浏览器输入****[http://\**127.0.0.1:5000/news\**](http://127.0.0.1:5000/news)、[http://\**127.0.0.1:5000/products\**](http://127.0.0.1:5000/products)****查看蓝图设置是否生效：**

## **三**

蓝图的目的是实现各个模块的视图函数写在不同的py文件中，在主视图中导入分路由视图的模块，并且注册蓝图对象。

当然，**视图函数的名称不能和蓝图对象的名称一样**。





[Flask干货：Flask视图高级技术（四）](https://zhuanlan.zhihu.com/p/164856344)

