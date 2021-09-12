# ORM方式操作数据库

```python
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqqlalchemy.ext.declarative import declarative_base

```


​    
```python
# 创建对象的基类:

Base = declarative_base()


class User(Base):
	# 表的名字:
   __tablename__ = 'user'
	# 表的结构:
	id = Column(String(20),primary_key=True)
	name = Column(String(20))
```


```python
engine = create_engine('mysql://root:123456@127.0.0.1/test')
# 创建DBSession类型
DBSession=sessionmaker(bind=engine)
```



```python
# 创建session对象:
session = DBSession()
# 创建新User对象:
new_user = User(id='5', name='Bob')
# 添加到session:
session.add(new_user)
# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()
```



```python
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 打印类型和对象的name属性:
print 'type:', type(user)
print 'name:', user.name
# 关闭Session:
session.close()
```



```
type: <class '__main__.User'>
name: Bob
```

本教程主要参考廖雪峰大神的教程。

windows下要使用sqlalchemy必须安装VCforPython27和MySQL-python-1.2.3.win-amd64-py2.7



 [ORM方式操作数据库](https://blog.csdn.net/elite666/article/details/80573814)