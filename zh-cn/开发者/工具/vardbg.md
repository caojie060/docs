# vardbg

[![在PyPI上可用](https://camo.githubusercontent.com/890ff960558b0c080f0d26b8ae0798e6a4d44865d4440df3933c7f71009ea4fb/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f766172646267)](https://pypi.org/project/vardbg/)

一个简单的 Python 调试器和探查器，可生成程序流的生动可视化图像。它旨在通过使您可视化算法在做什么来帮助学习算法。

由于使用了 f 字符串，因此需要 **Python 3.6** 或更高版本。

该项目是[在](https://codein.withgoogle.com/)2019 年 [Google Code-in 中](https://codein.withgoogle.com/)用于[CCExtractor 开发的](https://ccextractor.org/)过程中创建的。

## 演示版

[![插入排序演示](https://user-images.githubusercontent.com/7930239/73394845-3aa8fb00-4293-11ea-8477-6590cdeab5eb.gif)](https://user-images.githubusercontent.com/7930239/73394845-3aa8fb00-4293-11ea-8477-6590cdeab5eb.gif)

## 特征

- 跟踪每个变量及其内容的历史记录
- 容器内的跟踪元素（列表，集合，字典等）
- 忽略特定变量
- 分析每行的执行
- 总结执行后的所有变量和执行时间
- 将参数传递给调试程序
- 以 JSON 格式导出执行历史记录并进行重放（包括程序输出）
- 创建视频以显示程序流程，执行时间，变量（带有关系）和输出
- 以 MP4，GIF 和 WebP 格式编写视频

## 安装

可以从 PyPI 获得最新的标记版本：

```
点安装vardbg
```

或者，可以克隆此存储库并在安装依赖项后直接运行它：

```
git clone https://github.com/CCExtractor/vardbg
 cd vardbg
python3 -m venv venv
来源venv / bin / activate
点安装诗
诗歌安装。
./debug.py
```

也可以从存储库中安装它：

```
点安装。
```

以上说明假定使用虚拟环境以避免干扰 Python 的系统安装。

## 用法

调试器的所有子命令和选项都记录在使用帮助中，该帮助可在命令行上找到。

例如，此命令将从带有参数`quick_sort`的文件中调试功能，并将会话记录到名为的 JSON 文件中：`sort.py``9 3 5 1``sort1.json`

```
vardbg运行sort.py quick_sort -o qsort.json -a 9 -a 3 -a 5 -a 1
```

然后可以从以上记录中生成视频：

```
vardbg重播qsort.json -v sort_vis.mp4
```

可以在运行调试程序的同时实时生成视频，但是不建议这样做，因为视频创建的开销会极大地延长执行时间，从而破坏分析器结果。但是，如果性能分析对您而言并不重要，那么这是一个有效的用例。

## 配置

视频生成器具有许多选项：分辨率，速度，字体和大小。可以使用[TOML](https://learnxinyminutes.com/docs/toml/)配置文件来修改这些选项。在[默认的配置](https://github.com/CCExtractor/vardbg/blob/master/vardbg/output/video_writer/default_config.toml)文件可用的选项，它可以在最小的覆盖配置进行定制，而不必复制整个配置。然后可以通过`-c`在命令行上传递参数来使用配置。

简单叠加的一个例子是[配置](https://github.com/CCExtractor/vardbg/blob/master/demo_config.toml)用于产生在自述文件中嵌入官方演示视频。这个简单的配置会稍微提高速度（FPS），并在视频开始处添加一个简介屏幕。

## 行为控制

可以在定义变量的代码行中添加特殊注释，以控制 vardbg 如何处理所述变量：

- `# vardbg: ignore` — 不显示此变量或跟踪其值
- `# vardbg: ref lst[i]`— 将变量`i`视为容器中元素的索引 / 键`lst`（仅在视频中显示）

指定变量名称似乎是多余的，但这背后有两个原因：可靠地解析所有定义变量的代码非常困难（循环方法，拆包，直接赋值，`exec`调用，等），并且一行上可以声明多个变量。例如，元组拆包和函数参数是在单个行上添加多个变量的常见情况。因此，必须在引用中指定变量名称，以防止产生歧义。

## 贡献

随时为这个项目做贡献！您可以添加功能，修复错误或进行其他您认为合适的改进。我们只是要求您遵循[代码风格指南](https://github.com/CCExtractor/vardbg/blob/master/CODE_STYLE.md)以保持代码的一致性和连贯性。在使用[pre-commit](https://pre-commit.com/)框架进行推送之前，可以很容易地实施这些准则，该框架可以使用`pre-commit install`命令安装 Git pre-commit 挂钩。

一旦您的捐款符合准则，请[打开拉取请求](https://github.com/CCExtractor/vardbg/compare)以将事情正式化。

[vardbg]:https://github.com/CCExtractor/vardbg#vardbg

