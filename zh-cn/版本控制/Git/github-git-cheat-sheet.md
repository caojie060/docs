# github-git-cheat-sheet

 [training.github.com](https://training.github.com/downloads/zh_CN/github-git-cheat-sheet/)

安装
--

### GitHub桌面

[desktop.github.com](https://desktop.github.com/)

### Git全平台版

[git-scm.com](https://git-scm.com/)

配置工具
----

对所有本地仓库的用户信息进行配置

`$ git config --global user.name "[name]"`

对你的提交操作设置关联的用户名

`$ git config --global user.email "[email address]"`

对你的提交操作设置关联的邮箱地址

`$ git config --global color.ui auto`

启用有帮助的彩色控制台输出

分支
--

各个是使用Git工作的一个重要部分。你做的任何提交都会发生在当前“ checked out”到各个分支上。使用`git status`查看那是其中一个分支。

`$ git branch [branch-name]`

创建一个新分支

`$ git checkout [branch-name]`

切换到指定分支并更新工作目录（工作目录）

`$ git merge [branch]`

这通常在拉取请求（PR）中完成，但也是一个重要的Git操作。

`$ git branch -d [branch-name]`

删除指定分支

创建仓库
----

当着手于一个新的仓库时，您只需创建一次。或者在本地创建，然后推到GitHub；或者通过clone一个现有仓库。

`$ git init`

在使用过`git init`命令后，使用以下命令将本地仓库与一个GitHub上的空仓库连接起来：

`$ git remote add origin [url]`

将现有目录转换为一个Git仓库

`$ git clone [url]`

Clone（下载）一个已存在于GitHub上的仓库，包括所有的文件，分支和提交（commits）

.gitignore文件
------------

有时一些文件最好不要用Git跟踪。这通常在某些特殊`.gitignore`文件中完成。你可以在[github.com/github/gitignore](https://github.com/github/gitignore)找到有用的`.gitignore`文件模板。

同步更改
----

将您本地仓库与GitHub.com上的早期仓库同步

`$ git fetch`

下载远端追踪各个的所有历史

`$ git merge`

将远端跟踪合并合并到当前本地分支

`$ git push`

将所有本地分支提交上传到GitHub

`$ git pull`

使用来自GitHub的对应离散分支的所有新提交更新你当前的本地工作分支。`git pull`是`git fetch`和`git merge`的结合

进行更改
----

浏览并检查项目文件的发展

`$ git log`

列出当前分支的版本历史

`$ git log --follow [file]`

列出文件的版本历史，包括重命名

`$ git diff [first-branch]...[second-branch]`

展示两个分支之间的内容差异

`$ git show [commit]`

输出指定commit的元数据和内容变化

`$ git add [file]`

将文件进行快照处理用作版本控制

`$ git commit -m "[descriptive message]"`

将文件快照永久地记录在版本历史中

重做提交
----

清除错误和重建为替换的历史

`$ git reset [commit]`

撤销所有`[commit]`后的的提交，在本地保存更改

`$ git reset --hard [commit]`

放弃所有历史，改回指定提交。

> 小心！更改历史可能带来不良后果。如果您需要更改GitHub（早期）已有的提交，请谨慎操作。如果您需要帮助，可访问[github.community](https://github.community/)或联系支持（支持）。

术语表
---

*   **git**：一个开源的分布式版本控制系统
*   **GitHub**：一个托管和协作管理Git仓库的平台
*   **提交**：一个Git对象，是你整个仓库的快照的哈希值
*   **branch分支**：一个轻型可移动的commit指针
*   **clone**：一个仓库的本地版本，包含所有提交和分支
*   **remote极端**：一个GitHub上的公共仓库，所有小组成员通过它来交换修改
*   **fork**：一个属于另一个用户的GitHub上的仓库的副本
*   **pull request拉取请求**：一处用于比较和讨论分支上约会的差异，并且具有评估，评论，集成测试等功能的地方
*   **HEAD**：代表您当前的工作目录。使用`git checkout`可移动HEAD指针到不同的分支，标记（标签）或提交





 [training.github.com](https://training.github.com/downloads/zh_CN/github-git-cheat-sheet/)

