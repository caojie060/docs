# 分享一个代码搜索工具：krugle

最近做要做一个 e-learning 系统。于是就想找个现成的开源项目。找了半天，发现了一个代码搜索工具：krugle，感觉非常强大，不仅速度快，而且代码量也多，并且可以查看项目结构，集成 sourceforge,apache,mozilla 等开源项目。并且有 eclipse 对应的插件，可以直接在 eclipse 中搜索代码，然后就发扬拿来主义了.

www.krugle.org

以下是找到的一些描述：Krugle 提供了很多常用的编程语言，有 C、C++、C#、Javascript、Java、Emacs Lisp、Objective C、Python、Perl、PHP、Ruby、Scheme、SQL、TCL、XML 甚至 Unix Shell 都有，可是却没有 ASP、ASP.net 和 VB，这让我很奇怪。在搜索的时候 Krugle 又分为三大类搜索，一个是 Code，一个是 Teach Pages，还有一个就是 Projects。其中 Code 就是搜索源代码了，这其中又分搜索关键字是在 Any area（部分区域）、Comments（注释）、Source Code（源代码）、Function Definition（函数定义）、Function Call（函数调用）和 Class Definition（类定义）中，根据选择的不同搜索出不同的代码链接。Teach Pages 就会返回相关技术的网页链接，而 Projects 就会返回你所选择搜索的相关项目工程的主页。在这三中模式下都是相铺相乘的，无论你是使用哪个模式搜索过结果，当你转到另一个模式下的时候它会自动的将相应的搜索结果返回给你，非常的智能化。

Teach Pages 和 Projects 没什么好说的，就说说 Code 模式吧。我尝试着搜索了几个关键字，如 WordPress、XML、Blog 之类的，发现搜索的结果很多，可以说还是比较全的（Blog 我是搜索全部语言种类的，连由 JSP 编写的都搜索出来了让我吃惊不小，要知道基本上没人会用 JSP 做 Blog 的）。返回的结果显示也比较满意，首先返回的是代码文件名、工程项目主页地址、语言，然后下面就是相关一部分代码预览。在右边你还会发现一些相关的结果如一些赞助的在线书籍和 Teach Pages 的结果，你可以看我这里的截图。

选中一个代码文件名就可以进入查看这个文件的所有代码了，值得称赞的是 Krugle 为每一种的语言文件都采用了语法高亮的显示，让我们能够看得很舒服。再右边原本的相关结果将会变为此代码文件的项目工程树形结构图，你可以方便的查看这个项目工程中其它的代码文件来更细致的了解此文件在其中的作用。你可以在看看我这里的截图。另外 Krugle 还提供了选择代码片断的再搜索功能（个人觉得比较贴近用户，省事了不少）为我们提供了保存文件的功能，不过只能保存正在查看的单一文件，不能将整个项目工程一起保存，并且 Demo 中添加 Note 的功能并没有完善，这有难免有点遗憾，希望再以后能够更加的完善。

[分享一个代码搜索工具：krugle]:https://www.douban.com/group/topic/5667527/

