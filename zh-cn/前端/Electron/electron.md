# [Electron调用命令行(cmd)方法总结_王俊的博客-CSDN博客_electron执行cmd命令](https://blog.csdn.net/weixin_42762089/article/details/88711853)

方法一使用 child_process
官方文档：[child_process 子进程 | Node.js API 文档](http://nodejs.cn/api/child_process.html)

参考：[Electron运行后台命令行程序 - 简书](https://www.jianshu.com/p/0f0c88e3aa99)
方法二使用 node-cmd
官方文档：[node-cmd - npm](https://www.npmjs.com/package/node-cmd)

参考：[nodejs 运行CMD命令_llzkkk12的博客-CSDN博客](https://blog.csdn.net/llzkkk12/article/details/78171750)
方法一 (使用 child_process)，可以指定命令行运行的路径，而方法二 (使用 node-cmd) 不能

# [如何从Atom electron应用程序调用Shell脚本或python脚本 - 问答 - Python中文网](https://www.cnpython.com/qa/52567)
它可以直接使用 Node 完成，您可以使用 `child_process` 模块。请注意这是异步的。
我鼓励您也看看[npm](http://npmjs.com/)，有很多模块可以帮助您做您想要的事情，而无需调用 python 脚本。
## [electron-shell-打开浏览器 - ♥之 - 博客园](https://www.cnblogs.com/fwjlucifinil/p/13536319.html#/c/subject/p/13536319.html)

# [Electron+Python界面开发（通过zerorpc） - 知乎](https://zhuanlan.zhihu.com/p/37999476)

[pywebview](https://pywebview.flowrl.com/)

[Python使用pywebview开发桌面应用_Dexter's Laboratory-CSDN博客_pywebview](https://blog.csdn.net/lpwmm/article/details/102998126)

[pywebview3.0初探 - aaronhua - 博客园](https://www.cnblogs.com/aaronhua/p/11358051.html)

[Python使用Eel和HTML开发桌面应用_Dexter's Laboratory-CSDN博客](https://blog.csdn.net/lpwmm/article/details/102965286)

[electron作为python界面开发入门 - DataSense](https://mlln.cn/2018/01/08/electron%E4%BD%9C%E4%B8%BApython%E7%95%8C%E9%9D%A2%E5%BC%80%E5%8F%91%E5%85%A5%E9%97%A8/)

[python-script-manager: 基于electron的桌面应用，方便执行一些python工具脚本](https://gitee.com/maotoumao/python-script-manager)