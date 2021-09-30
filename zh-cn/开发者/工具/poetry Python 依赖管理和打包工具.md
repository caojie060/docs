# poetry Python 依赖管理和打包工具

### 软件简介

poetry 是一个包管理和打包的工具。

在 Python 中，对于初学者来说，打包系统和依赖管理是非常复杂和难懂的。即使对于经验丰富的开发者，一个项目总是要同时创建多个文件： `setup.py` ,`requirements.txt`,`setup.cfg` , `MANIFEST.in` ，还有最新的 `Pipfile`。

基于此， poetry 将所有的配置都放置在一个 toml 文件中，这些配置包括：依赖管理、构建、打包、发布。

poetry 的灵感来自于其他语言的一些工具： composer (PHP) 和 cargo (Rust) 。

![poetry](https://static.oschina.net/uploads/img/201809/18140749_I7Es.gif)

# 配置

poetry 的项目配置文件是 pyproject.toml ，一个简单的示例文件如下：

```
[tool.poetry]
name = "poetry"
version = "0.11.5"
description = "Python dependency management and packaging made easy."
authors = [
    "Sébastien Eustace <sebastien@eustace.io>"
]
license = "MIT"

readme = "README.md"

homepage = "https://poetry.eustace.io/"
repository = "https://github.com/sdispater/poet"
documentation = "https://poetry.eustace.io/docs"

keywords = ["packaging", "dependency", "poetry"]

classifiers = [
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Libraries :: Python Modules"
]

# Requirements
[tool.poetry.dependencies]
python = "~2.7 || ^3.4"
cleo = "^0.6.7"
requests = "^2.18"
cachy = "^0.2"
requests-toolbelt = "^0.8.0"
jsonschema = "^2.6"
pyrsistent = "^0.14.2"
pyparsing = "^2.2"
cachecontrol = { version = "^0.12.4", extras = ["filecache"] }
pkginfo = "^1.4"
html5lib = "^1.0"
shellingham = "^1.1"
tomlkit = "^0.4.4"

# The typing module is not in the stdlib in Python 2.7 and 3.4
typing = { version = "^3.6", python = "~2.7 || ~3.4" }

# Use pathlib2 for Python 2.7 and 3.4
pathlib2 = { version = "^2.3", python = "~2.7 || ~3.4" }
# Use virtualenv for Python 2.7 since venv does not exist
virtualenv = { version = "^16.0", python = "~2.7" }

[tool.poetry.dev-dependencies]
pytest = "^3.4"
pytest-cov = "^2.5"
mkdocs = "^1.0"
pymdown-extensions = "^4.9"
pygments = "^2.2"
pytest-mock = "^1.9"
pygments-github-lexers = "^0.0.5"
black = { version = "^18.3-alpha.0", python = "^3.6" }
pre-commit = "^1.10"
tox = "^3.0"


[tool.poetry.scripts]
poetry = "poetry.console:main"
```

# 命令

poetry 提供了一系列覆盖整个开发流程的命令，这些命令使用简单：

| 名称    | 功能                                                       |
| ------- | ---------------------------------------------------------- |
| new     | 创建一个项目脚手架，包含基本结构、pyproject.toml 文件      |
| init    | 基于已有的项目代码创建 pyproject.toml 文件，支持交互式填写 |
| install | 安装依赖库                                                 |
| update  | 更新依赖库                                                 |
| add     | 添加依赖库                                                 |
| remove  | 移除依赖库                                                 |
| show    | 查看具体依赖库信息，支持显示树形依赖链                     |
| build   | 构建 tar.gz 或 wheel 包                                    |
| publish | 发布到 PyPI                                                |
| run     | 运行脚本和代码                                             |

[poetry Python 依赖管理和打包工具]:https://www.oschina.net/p/poetry?hmsr=aladdin1e1

