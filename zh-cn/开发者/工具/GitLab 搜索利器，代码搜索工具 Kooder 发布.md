# GitLab 搜索利器，代码搜索工具 Kooder 发布

一个企业里往往有大量的项目，每个项目都包含很多的代码，经过日积月累，不同的开发人员不断地对代码修改完善，代码和代码仓库的数量也随之增长。

由于数量太多，企业中很难有人能掌握所有代码的细节，当想要统一排查代码是否包含某类敏感信息，或检查是否使用了某些不安全的方法时，就需要开发人员各自手工排查自己负责的代码，费时费力。

因此，企业全库的代码搜索就变得非常重要。尤其对于将代码通过 GitLab 部署在本地服务器的企业，由于缺少了云端托管平台自身集成的搜索引擎，想要在本地进行全局的代码搜索就变得异常困难。

为解决该问题，**Gitee 团队在近日开源了代码搜索工具 Kooder，Kooder 的目标是为包括 Gitee/GitLab/Gitea 在内的代码托管系统提供自动的源码、仓库和 Issue 的搜索服务。**

### **Kooder 架构**

Kooder 服务包含两个模块，分别是 `gateway` 和 `indexer`（默认配置下 `indexer` 被集成到 `gateway` 中）。 其中 `gateway` 用来接受来自 `HTTP` 的索引任务， 对任务进行检查后存放到队列中； 同时 `gateway` 还接受搜索的请求，并返回搜索结果给客户端。而 `indexer` 进程负责监控队列中的索引任务， 并将这些要新增、删除和修改索引的任务更新到索引库中。

### **数据流图**

![img](https://pic3.zhimg.com/80/v2-c4e188a84e89d8b48148074022f0fb9a_720w.jpg)



### **搜索界面效果**

![img](https://pic3.zhimg.com/80/v2-2680b76f62b72c8d42e42e1aa686932a_720w.jpg)

![img](https://pic2.zhimg.com/80/v2-868174bbdafa1c4dd25b48d573f24fdd_720w.jpg)

### **进行贡献**

Kooder 遵循 `Apache-2.0` 开源协议，欢迎开发者们踊跃提交 Issue 和 PR。

更多详细信息请前往代码仓库查看：

Gitee（主仓库）：https://gitee.com/koode/kooder

GitHub（镜像仓库）：[https://github.com/oschina/kood](https://github.com/oschina/kooder)

[GitLab 搜索利器，代码搜索工具 Kooder 发布]:https://zhuanlan.zhihu.com/p/355983092

