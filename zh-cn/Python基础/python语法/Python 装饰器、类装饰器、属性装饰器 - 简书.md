> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.jianshu.com](https://www.jianshu.com/p/dd983ecc1104)

今天来介绍一下 python 的装饰器。

1. 首先来介绍一下简单的装饰器，

    def play():

return "i can play"

if __name__ == '__main__':

print(play())

然后我们 command + B 编译一下，或者控制台执行脚本都可以，会打印出我们要的结果

![](http://upload-images.jianshu.io/upload_images/9129553-a4b7eff9da37113a.png)

接下来我们在写一个方法，

def bas(add_func):

def insetFunc():

return add_func() + "basketball"

return insetFunc

![](http://upload-images.jianshu.io/upload_images/9129553-d77da6cdc964b0f2.png)

代码的意思就是，传进来一个方法，然后来执行这个方法的内部方法，然后拼接一个字符串

然后我们在刚才的 play 方法脑袋上加一个 @bas，也就是装饰器的意思

![](http://upload-images.jianshu.io/upload_images/9129553-60f9525cd3bae6fc.png)

这个时候 我们再编译一下，会看见控制台的的打印是这样的

![](http://upload-images.jianshu.io/upload_images/9129553-f0ca479416f50eed.png)

这样一个简单的装饰器就做完了。

2. 类装饰器

class eat(object):

"""docstring for eat"""

def __init__(self, food):

super(eat, self).__init__()

self.food = food

def display(self):

print('my lunch is' + self.food)

, 首先我们写一个类，然后调用这个类的 display 方法，

![](http://upload-images.jianshu.io/upload_images/9129553-d7f529c4fa8d8f45.png)

然后我们可以看到控制台的打印是

![](http://upload-images.jianshu.io/upload_images/9129553-221045be8a597d0d.png)

接下来我们要求，每顿午餐都必须有吃有喝，而我们的 eat 方法只能传入一个参数，怎么办呢，我们可以用一下装饰器。

首先我们新建一个方法

def newEat(newCls):

class newEatCls():

"""docstring for newEatCls"""

def __init__(self, food,water):

# super(newEatCls, self).__init__()

self.new = newCls(food)

self.water = water;

def display(self):

print("my lunch is" + self.new.food + 'and' + self.water)

return newEatCls

![](http://upload-images.jianshu.io/upload_images/9129553-66bb37e853ac21c2.png)

这个方法的意思大概是我们传进来一个类，然后初始化，把这个类里面有的参数，还用原始类去初始化，没有的话赋值给他，然后把这个类重新返回，这样，这个类就被装饰了，然后再对刚才的 eat 的类进行装饰，这样，

![](http://upload-images.jianshu.io/upload_images/9129553-cba1c669ca134d7a.png)

这时候我们看控制台的打印，

![](http://upload-images.jianshu.io/upload_images/9129553-9bb8b63206c510d8.png)

这样我们吃喝就都有了，原来的 display 方法就被装饰了。

3. 属性装饰器

一般有这样的需求，类里面的某个属性，不想让外部来访问，定义成私有变量，因为我们不想别人来改变这个值，只能读，所以，这个时候，我们可以把属性设置为私有的，然后，通过属性装饰器的方式，让外部能够读取到

首先我们这样，定义一个类, 如果我们这样写是会报错的，因为我们声明 persion 类的两个属性都是私有的，外部是访问不了的，

![](http://upload-images.jianshu.io/upload_images/9129553-17d48e16f39fd56f.png) ![](http://upload-images.jianshu.io/upload_images/9129553-541039dbe958aa01.png)

那我们怎样才可以访问到这两个变量呢，通过属性装饰器的方式，

接下来我们在写两个方法，

![](http://upload-images.jianshu.io/upload_images/9129553-66ef652e08cc1531.png)

这样我们的属性装饰器就做完了，@property，来告诉他是一个属性，@name.setter 来装饰他，以给他赋值，这时候运行就不会报错了，可以去到我们的私有属性__name 了，并且给他赋值也是可以的，这样我们的属性装饰器就做完了。