# sourcetrail

#### 软件简介



Sourcetrail 是一款非常不错的开发软件，它为您提供很多代码的变成工作，详细的源代码讲解为您的开发提供了便利的条件！Sourcetrail
的功能强大，设计简单，让您的程序语言变的更加专业，开放的源代码程序为您开发写代码提供了很多有用的思路哦！

Sourcetrail 是一个商业软件，但是现在非商业用途可免费使用。

![img](https://codingdict.com/static/assets/osapp/images/86ce6d1d5c0af34fe4b1d3c86c2fc122.png)

![img](https://codingdict.com/static/assets/osapp/images/42de5364ee0625706e836b4f8eb0076f.png)

主要功能：

### 索引您的源代码

Sourcetrail 的深入静态分析发现源文件中的所有定义和引用。您可以从几种方法中选择项目设置。

### 找到任何符号

使用 Sourcetrail 的搜索字段快速找到整个代码库中的任何符号。模糊的关键字匹配可让您获得最佳匹配，只需几次按键即可。

### 视觉浏览

图形可视化提供了任何类，方法，字段等及其所有关系的快速概述。图形完全互动。使用它通过关注其他节点和边缘来移动代码库。

### 探索你的代码

最后，代码视图将所有元素的实现细节保存在精心安排的代码片段列表中。进一步检查范围和局部变量，或专注于任何其他遇到的参考或元素。

### 连接源代码编辑器

通过 Sourcetrail 和您最喜欢的源代码编辑器之间的插件进行沟通。这样可以方便地在写作和探索之间切换。看看我们的支持编辑列表。

## 如何使用

Edit Project
Files & Directories to Index
应该只填写源代码的路径

Excluded Files & Directories
排除文件，具体看小问号

Source File Extensions
源文件扩展名，需要添加 .h

这将会使用 mingw 的头文件，而不是 msvc (默认)

Include Paths
项目依赖的库的头文件搜索路径，需要正确填写

Global Include Paths
全局的项目依赖的库的头文件搜索路径，只需设置一次

Compiler Flags
编译器标志，（好像只是用来定义宏的

#### 问题

有的文件不会被解析，很无语，是 #include 的问题。
排查中发现的，通过一行一行注释掉 #include 找到罪魁祸首。但无法理解为何会造成这样。就是它 #include <tinyxml.h>，库中有它，项目中也有它，使用库中的就无法解析，使用项目中的就可以。

通过 Include Paths 控制，似乎会优先使用该路径组。

SourceTrail 是一款开源、免费的交互式源代码浏览器，它能够通过索引你的文件以及收集项目的结构数据来简化你在现存代码中查看。目前支持的语言种类：C、C++、Java、Python，并且可以自定义语言类型。

源代码浏览器的作用比较大，从一定程度上能够简化你对一个项目源代码的了解过程，源代码浏览器一般情况下都能够针对某个变量或者方法等进行全项目的查找索引等，比较有名的是 SI 但是收费，而且功能很丰富学习难度大。

创建 SourceTrail 项目


启动 SourceTrail 出现的是开始页面，从开始页面可以进行项目的创建或者打开项目。此处以一个 DirectX 11 的项目为例！

1、点击 New Project 按钮，创建一个新项目；



2、弹出项目创建向导，根据项目的不同该向导的创建步骤也不同，填写项目名称及项目创建目录，并点击 Add Source Group 添加文件到项目中；





3、选择项目语言类型以及以何种方式导入项目；

如果使用 Cmake、Make、QtCreator 作为编译环境，可以导出一个 clang JSON 编译数据库并命名为 compile_commands.json，一个编译数据库包含对编一个项目所有的必要信息，包含源文件、包含路径和编译标志。通过使用编译数据库可以轻松创建 SourceTrail 项目，坐着推荐使用该方法。

导出编译数据库：

对于 CMake 通过定义 CMAKE_EXPORT_COMPILE_COMMANDS 标志位实现；
对于 Make 工程使用 Bear，该工具在一个构建进程中生成一个 compile_commands.json；
对于 Qt Creator 通过选择”Build” 菜单中的”Generate Compilation Database” 选项；
如果使用 Visual Studio 导出一个编译数据库需要使用对应的 Visual Studio 插件，可以通过选择 C++、C、Java、Custom 进行查看创建工程的方法。



4、点击 Next 按钮，并填写 Compilation_Database.json 文件、头文件路径、排除的文件路径等；



5、点击 Next 按钮，填写预编译的头文件路径和标志；



6、点击 Next 后便回到创建项目页，并且在一个项目中可以创建多个 SourceGroup；



7、点击 Create 按钮创建项目，点击弹出窗口中的 Start 进行索引文件；



在这个过程中往往会出现错误，大部分是不能正确识别文件中的内容抛出的异常。

[Sourcetrail - 源代码分析查看工具]:https://codingdict.com/os/software/70655
[Sourcetrail 使用注意]:https://blog.csdn.net/u011091701/article/details/105208145/
[使用 SourceTrail 代替 SourceInsight]:https://blog.csdn.net/BurneAris/article/details/103898910





