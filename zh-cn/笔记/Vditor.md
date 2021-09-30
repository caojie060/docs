#  Vditor 一款浏览器端的 Markdown 编辑器，支持所见即所得（富文本）、即时渲染（类似 Typora）和分屏预览模式

![Vditor](https://b3log.org/images/brand/vditor-128.png)
易于使用的 Markdown 编辑器，为适配不同的应用场景而生

[![img](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](https://link.ld246.com/forward?goto=https%3A%2F%2Fopensource.org%2Flicenses%2FMIT) [![npm bundle size](https://img.shields.io/bundlephobia/minzip/vditor?style=flat-square&color=blueviolet)](https://link.ld246.com/forward?goto=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvditor) [![img](https://img.shields.io/david/Vanessa219/vditor.svg?style=flat-square&color=ff96b4)](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor)
[![img](https://img.shields.io/npm/v/vditor.svg?style=flat-square)](https://link.ld246.com/forward?goto=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvditor) [![img](https://img.shields.io/npm/dt/vditor.svg?style=flat-square&color=97ca00)](https://link.ld246.com/forward?goto=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fvditor)
[![img](https://data.jsdelivr.com/v1/package/npm/vditor/badge)](https://link.ld246.com/forward?goto=https%3A%2F%2Fwww.jsdelivr.com%2Fpackage%2Fnpm%2Fvditor) [![img](https://hits.b3log.org/Vanessa219/vditor.svg)](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2F88250%2Fhits)

[![img](https://img.shields.io/github/watchers/Vanessa219/vditor.svg?label=Watchers&style=social)](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fwatchers) [![img](https://img.shields.io/github/stars/Vanessa219/vditor.svg?label=Stars&style=social)](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fstargazers) [![img](https://img.shields.io/github/forks/Vanessa219/vditor.svg?label=Forks&style=social)](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fnetwork%2Fmembers) [![img](https://img.shields.io/github/followers/vanessa219.svg?label=Followers&style=social)](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2Fvanessa219)

[English](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fblob%2Fmaster%2FREADME_en_US.md) | [Demo](https://link.ld246.com/forward?goto=https%3A%2F%2Fb3log.org%2Fvditor%2Fdemo%2Findex.html)

## 💡 简介

[Vditor](https://link.ld246.com/forward?goto=https%3A%2F%2Fb3log.org%2Fvditor) 是一款浏览器端的 Markdown 编辑器，支持所见即所得、即时渲染（类似 Typora）和分屏预览模式。它使用 TypeScript 实现，支持原生 JavaScript、Vue、React、Angular，提供[桌面版](https://link.ld246.com/forward?goto=https%3A%2F%2Fb3log.org%2Fsiyuan)。

欢迎到 [Vditor 官方讨论区](https://ld246.com/tag/vditor)了解更多。同时也欢迎关注 B3log 开源社区微信公众号 `B3log开源`：

![b3logos.jpg](https://b3logfile.com/file/2020/08/b3logos-032af045.jpg?imageView2/2/interlace/1/format/webp)



## 🗺️ 背景

随着 Markdown 排版方式的普及，越来越多的应用开始集成 Markdown 编辑器。目前主流可集成的 Markdown 编辑器现状如下：

- 有的仅支持分屏预览，即编辑区和预览区分离
- 有的同时支持所见即所得和分屏预览，但所见即所得模式下不能完整支持 Markdown 语法排版
- 几乎没有类似 Typora 的即时渲染

而这三点恰好对应了三种应用场景：

- 分屏预览：适配传统的 Markdown 使用场景，适合大屏下编辑排版
- 所见即所得：对不熟悉 Markdown 的用户友好，熟悉 Markdown 的用户也可以无缝使用
- 即时渲染：理论上这是最为优雅的 Markdown 编辑方式，让熟悉 Markdown 的用户能够更专注于内容创作

所以，一个能够**适配应用场景**的 Markdown 编辑器至关重要，它需要考虑到：

- 传统 Markdown 用户的使用场景，提供分屏预览
- 富文本编辑用户的使用场景，提供所见即所得
- 高阶 Markdown 用户的使用场景，提供即时渲染

Vditor 在这些方面做了努力，希望能为现代化的通用 Markdown 编辑领域做出一些贡献。

## ✨ 特性

- 支持三种编辑模式：所见即所得（wysiwyg）、即时渲染（ir）、分屏预览（sv）
- 支持大纲、数学公式、脑图、图表、流程图、甘特图、时序图、五线谱、[多媒体](https://ld246.com/article/1589813914768)、语音阅读、标题锚点、代码高亮及复制、graphviz 渲染、[plantuml](https://link.ld246.com/forward?goto=https%3A%2F%2Fplantuml.com)UML 图
- 内置安全过滤、导出、图片懒加载、任务列表、多平台预览、多主题切换、复制到微信公众号 / 知乎功能
- 实现 CommonMark 和 GFM 规范，可对 Markdown 进行格式化和语法树查看，并支持 [10+ 项](https://ld246.com/article/1549638745630#options-preview-markdown)配置
- 工具栏包含 36+ 项操作，除支持扩展外还可对每一项中的[快捷键](https://ld246.com/article/1582778815353)、提示、提示位置、图标、点击事件、类名、子工具栏进行自定义
- 表情 /at/ 话题等自动补全扩展
- 可使用拖拽、剪切板粘贴上传，显示实时上传进度，支持 CORS 跨域上传
- 实时保存内容，防止意外丢失
- 录音支持，用户可直接发布语音
- 粘贴 HTML 自动转换为 Markdown，如粘贴中包含外链图片可通过指定接口上传到服务器
- 支持主窗口大小拖拽、字符计数
- 多主题支持，内置黑白绿三套主题
- 多语言支持，内置中、英、韩文本地化
- 支持主流浏览器，对移动端友好

![editor.png](https://b3logfile.com/file/2020/07/editor-b304aa97.png?imageView2/2/interlace/1/format/webp)

![preview.png](https://b3logfile.com/file/2020/05/preview-80846f66.png?imageView2/2/interlace/1/format/webp)

## 🔮 编辑模式

### 所见即所得（WYSIWYG）

*所见即所得*模式对不熟悉 Markdown 的用户较为友好，熟悉 Markdown 的话也可以无缝使用。

![vditor-wysiwyg](https://b3logfile.com/file/2020/07/wysiwyg-4f216b9b.gif)

### 即时渲染（IR）

*即时渲染*模式对熟悉 Typora 的用户应该不会感到陌生，理论上这是最优雅的 Markdown 编辑方式。

![vditor-ir](https://b3logfile.com/file/2020/07/ir-67cd956c.gif)

### 分屏预览（SV）

传统的*分屏预览*模式适合大屏下的 Markdown 编辑。

![vditor-sv](https://b3logfile.com/file/2020/07/sv-595dcb28.gif)

## 🍱 语法支持

- 所有 CommonMark 语法：分隔线、ATX 标题、Setext 标题、缩进代码块、围栏代码块、HTML 块、链接引用定义、段落、块引用、列表、反斜杠转义、HTML 实体、行级代码、强调、加粗、链接、图片、行级 HTML、硬换行、软换行和纯文本。
- 所有 GFM 语法：表格、任务列表项、删除线、自动链接、XSS 过滤
- 常用 Markdown 扩展语法：脚注、ToC、自定义标题 ID
-  图表语法   
  - 流程图、时序图、甘特图，通过 Mermaid 支持
  -  Graphviz
  -  折线图、饼图、脑图等，通过 ECharts 支持
- 五线谱：通过 abc.js 支持
- 数学公式：数学公式块、行级数学公式，通过 MathJax 和 KaTeX 支持
-  YAML Front Matter
-  中文语境优化   
  - 中西文之间插入空格
  - 术语拼写修正
  - 中文后跟英文逗号句号等标点替换为中文对应标点

以上大部分特性可以通过开关配置是否启用，开发者可根据自己的应用场景选择搭配。

## 🗃 案例

- [Sym](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2F88250%2Fsymphony) 一款用 Java 实现的现代化社区（论坛 / BBS / 社交网络 / 博客）平台 
- [Solo](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2F88250%2Fsolo) & [Pipe](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2F88250%2Fpipe) B3log 分布式社区的博客端节点，欢迎加入下一代社区网络
- [思源笔记](https://link.ld246.com/forward?goto=https%3A%2F%2Fb3log.org%2Fsiyuan) 一款 Markdown 块级引用和双向链接的网状笔记应用 
- [Arya](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2Fnicejade%2Fmarkdown-online-editor) 基于 Vue、Vditor，所构建的在线 Markdown 编辑器
- [更多案例](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fnetwork%2Fdependents%3Fpackage_id%3DUGFja2FnZS0zMTY2Mzg4MzE%3D)

## 🛠️ 使用文档

### CommonJS

- 安装依赖 

```bash
npm install vditor --save
```

- 在代码中引入并初始化对象，可参考 [index.js](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fblob%2Fmaster%2Fdemo%2Findex.js)

```ts
import Vditor from 'vditor'
import "~vditor/src/assets/scss/index"

const vditor = new Vditor(id, {options...})
```

### HTML script

- 在 HTML 中插入 CSS 和 JavaScript，可参考 [demo](https://link.ld246.com/forward?goto=https%3A%2F%2Fb3log.org%2Fvditor%2Fdemo%2Findex.html)

```html
<!-- ⚠️生产环境请指定版本号，如 https://cdn.jsdelivr.net/npm/vditor@x.x.x/dist... -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/vditor/dist/index.css" />
<script src="https://cdn.jsdelivr.net/npm/vditor/dist/index.min.js"></script>
```

### 示例代码

- [官方示例](https://link.ld246.com/forward?goto=https%3A%2F%2Fb3log.org%2Fvditor%2Fdemo%2Findex.html) / [示例源码](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fb3log-index%2Ftree%2Fmaster%2Fsrc%2Fvditor)
- [CommonJS Editor](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fblob%2Fmaster%2Fdemo%2Findex.js)
- [CommonJS Render](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fblob%2Fmaster%2Fdemo%2Frender.js)

### 主题

#### 编辑器主题

编辑器所展现的外观。内置 classic，dark 2 套主题。

- 编辑器初始化时可通过 `options.theme` 设置内置主题
- 初始化完成后可通过 `setTheme` 更新编辑器主题
- 可通过修改 [index.scss](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fblob%2Fmaster%2Fsrc%2Fassets%2Fscss%2Findex.scss) 中的变量对主题颜色进行定制
- 可参考现有结构和类名在原有基础上进行修改

#### 内容主题

Markdown 输出的 HTML 所展现的外观。内置 light，dark，wechat 3 套主题。支持内容主题扩展接口。

- 需在显示元素上添加 `class="vditor-reset"`
- 编辑器初始化时可通过 `options.preview.theme` 设置内置或自己开发的主题列表
- 内容渲染初始化时可通过 `IPreviewOptions.theme` 设置内置或自己开发的主题
- 初始化完成后可通过 `setTheme` 或 `setContentTheme` 更新内容主题

#### 代码主题

代码块所展现的外观。内置 github 等 36 套主题。

- 编辑器初始化时可通过 `options.preview.hljs` 对代码块样式、行号、是否启用进行设置
- 内容渲染初始化时可通过 `IPreviewOptions.hljs` 对代码块样式、行号、是否启用进行设置
- 初始化完成后可通过 `setTheme` 或 `setCodeTheme` 更新代码主题

### API

#### id

可填入元素 `id` 或元素自身 `HTMLElement`

⚠️：当填入元素自身的 `HTMLElement` 时需设置 `options.cache.id` 或将 `options.cache.enable` 设置为 `false`

#### options

#### 

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>undoDelay</td><td>历史记录间隔</td><td>-</td></tr><tr><td>after</td><td>编辑器异步渲染完成后的回调方法</td><td>-</td></tr><tr><td>height</td><td>编辑器总高度</td><td>'auto'</td></tr><tr><td>minHeight</td><td>编辑区域最小高度</td><td>-</td></tr><tr><td>width</td><td>编辑器总宽度，支持 %</td><td>'auto'</td></tr><tr><td>placeholder</td><td>输入区域为空时的提示</td><td>''</td></tr><tr><td>lang</td><td>多语言：en_US, ja_JP, ko_KR, zh_CN</td><td>'zh_CN'</td></tr><tr><td>input(value: string)</td><td>输入后触发</td><td>-</td></tr><tr><td>focus(value: string)</td><td>聚焦后触发</td><td>-</td></tr><tr><td>blur(value: string)</td><td>失焦后触发</td><td>-</td></tr><tr><td>esc(value: string)</td><td><kbd>esc</kbd> 按下后触发</td><td>-</td></tr><tr><td>ctrlEnter(value: string)</td><td><kbd>⌘/ctrl+enter</kbd> 按下后触发</td><td>-</td></tr><tr><td>select(value: string)</td><td>编辑器中选中文字后触发</td><td>-</td></tr><tr><td>tab</td><td><kbd>tab</kbd> 键操作字符串，支持 <code>\t</code> 及任意字符串</td><td>-</td></tr><tr><td>typewriterMode</td><td>是否启用打字机模式</td><td>false</td></tr><tr><td>cdn</td><td>配置自建 CDN 地址</td><td><code>https://cdn.jsdelivr.net/npm/vditor@${VDITOR_VERSION}</code></td></tr><tr><td>mode</td><td>可选模式：sv, ir, wysiwyg</td><td>'ir'</td></tr><tr><td>debugger</td><td>是否显示日志</td><td>false</td></tr><tr><td>value</td><td>编辑器初始化值</td><td>''</td></tr><tr><td>theme</td><td>主题：classic, dark</td><td>'classic'</td></tr><tr><td>icon</td><td>图标风格：ant, material</td><td>'ant'</td></tr></tbody></table>

#### options.toolbar

*   工具栏，可使用 name 进行简写： `toolbar: ['emoji', 'br', 'bold', '|', 'line']` 。默认值参见 [src/ts/util/Options.ts](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fblob%2Fmaster%2Fsrc%2Fts%2Futil%2FOptions.ts)
*   name 可枚举为： `emoji` , `headings` , `bold` , `italic` , `strike` , `|` , `line` , `quote` , `list` , `ordered-list` , `check` ,`outdent` ,`indent` , `code` , `inline-code` , `insert-after` , `insert-before` ,`undo` , `redo` , `upload` , `link` , `table` , `record` , `edit-mode` , `both` , `preview` , `fullscreen` , `outline` , `code-theme` , `content-theme` , `export`, `devtools` , `info` , `help` , `br`
*   当 `name` 不在枚举中时，可以添加自定义按钮，格式如下：

```
new Vditor('vditor', {
  toolbar: [
    {
      hotkey: '⇧⌘S',
      name: 'sponsor',
      tipPosition: 's',
      tip: '成为赞助者',
      className: 'right',
      icon: '<svg t="1589994565028" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2808" width="32" height="32"><path d="M506.6 423.6m-29.8 0a29.8 29.8 0 1 0 59.6 0 29.8 29.8 0 1 0-59.6 0Z" fill="#0F0F0F" p-id="2809"></path><path d="M717.8 114.5c-83.5 0-158.4 65.4-211.2 122-52.7-56.6-127.7-122-211.2-122-159.5 0-273.9 129.3-273.9 288.9C21.5 562.9 429.3 913 506.6 913s485.1-350.1 485.1-509.7c0.1-159.5-114.4-288.8-273.9-288.8z" fill="#FAFCFB" p-id="2810"></path><path d="M506.6 926c-22 0-61-20.1-116-59.6-51.5-37-109.9-86.4-164.6-139-65.4-63-217.5-220.6-217.5-324 0-81.4 28.6-157.1 80.6-213.1 53.2-57.2 126.4-88.8 206.3-88.8 40 0 81.8 14.1 124.2 41.9 28.1 18.4 56.6 42.8 86.9 74.2 30.3-31.5 58.9-55.8 86.9-74.2 42.5-27.8 84.3-41.9 124.2-41.9 79.9 0 153.2 31.5 206.3 88.8 52 56 80.6 131.7 80.6 213.1 0 103.4-152.1 261-217.5 324-54.6 52.6-113.1 102-164.6 139-54.8 39.5-93.8 59.6-115.8 59.6zM295.4 127.5c-72.6 0-139.1 28.6-187.3 80.4-47.5 51.2-73.7 120.6-73.7 195.4 0 64.8 78.3 178.9 209.6 305.3 53.8 51.8 111.2 100.3 161.7 136.6 56.1 40.4 88.9 54.8 100.9 54.8s44.7-14.4 100.9-54.8c50.5-36.3 108-84.9 161.7-136.6 131.2-126.4 209.6-240.5 209.6-305.3 0-74.9-26.2-144.2-73.7-195.4-48.2-51.9-114.7-80.4-187.3-80.4-61.8 0-127.8 38.5-201.7 117.9-2.5 2.6-5.9 4.1-9.5 4.1s-7.1-1.5-9.5-4.1C423.2 166 357.2 127.5 295.4 127.5z" fill="#141414" p-id="2811"></path><path d="M353.9 415.6m-33.8 0a33.8 33.8 0 1 0 67.6 0 33.8 33.8 0 1 0-67.6 0Z" fill="#0F0F0F" p-id="2812"></path><path d="M659.3 415.6m-33.8 0a33.8 33.8 0 1 0 67.6 0 33.8 33.8 0 1 0-67.6 0Z" fill="#0F0F0F" p-id="2813"></path><path d="M411.6 538.5c0 52.3 42.8 95 95 95 52.3 0 95-42.8 95-95v-31.7h-190v31.7z" fill="#5B5143" p-id="2814"></path><path d="M506.6 646.5c-59.6 0-108-48.5-108-108v-31.7c0-7.2 5.8-13 13-13h190.1c7.2 0 13 5.8 13 13v31.7c0 59.5-48.5 108-108.1 108z m-82-126.7v18.7c0 45.2 36.8 82 82 82s82-36.8 82-82v-18.7h-164z" fill="#141414" p-id="2815"></path><path d="M450.4 578.9a54.7 27.5 0 1 0 109.4 0 54.7 27.5 0 1 0-109.4 0Z" fill="#EA64F9" p-id="2816"></path><path d="M256 502.7a32.1 27.5 0 1 0 64.2 0 32.1 27.5 0 1 0-64.2 0Z" fill="#EFAFF9" p-id="2817"></path><path d="M703.3 502.7a32.1 27.5 0 1 0 64.2 0 32.1 27.5 0 1 0-64.2 0Z" fill="#EFAFF9" p-id="2818"></path></svg>',
      click () {alert('捐赠地址：https://ld246.com/sponsor')},
    }],
})
```

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>name</td><td>唯一标示</td><td>-</td></tr><tr><td>icon</td><td>svg 图标</td><td>-</td></tr><tr><td>tip</td><td>提示</td><td>-</td></tr><tr><td>tipPosition</td><td>提示位置：'n', 'ne', 'nw', 's', 'se', 'sw', 'w', 'e'</td><td>-</td></tr><tr><td>hotkey</td><td>快捷键，格式为<kbd>⇧⌘</kbd>/<kbd>⌘</kbd>/<kbd>⌥⌘</kbd></td><td>-</td></tr><tr><td>suffix</td><td>插入编辑器中的后缀</td><td>-</td></tr><tr><td>prefix</td><td>插入编辑器中的前缀</td><td>-</td></tr><tr><td>click(event: Event, vditor: IVditor)</td><td>自定义按钮点击时触发的事件</td><td>-</td></tr><tr><td>className</td><td>样式名</td><td>''</td></tr><tr><td>toolbar?: Array&lt;options.toolbar&gt;</td><td>子菜单</td><td>-</td></tr></tbody></table>

#### options.toolbarConfig

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>hide</td><td>是否隐藏工具栏</td><td>false</td></tr><tr><td>pin</td><td>是否固定工具栏</td><td>false</td></tr></tbody></table>

#### options.counter

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>enable</td><td>是否启用计数器</td><td>false</td></tr><tr><td>tipPosition(length: number, counter: options.counter): void</td><td>字数统计回调</td><td>-</td></tr><tr><td>max</td><td>允许输入的最大值</td><td>-</td></tr><tr><td>type</td><td>统计类型：'markdown', 'text'</td><td>'markdown'</td></tr></tbody></table>

#### options.cache

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>enable</td><td>是否使用 localStorage 进行缓存</td><td>true</td></tr><tr><td>id</td><td>缓存 key，第一个参数为元素且启用缓存时<strong>必填</strong></td><td>-</td></tr><tr><td>after(html: string): string</td><td>缓存后的回调</td><td>-</td></tr></tbody></table>

⚠️：仅支持 wysiwyg 模式

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>enable</td><td>是否启用评论模式</td><td>false</td></tr><tr><td>add(id: string, text: string, commentsData: ICommentsData[])</td><td>添加评论回调</td><td>-</td></tr><tr><td>remove(ids: string[])</td><td>删除评论回调</td><td>-</td></tr><tr><td>scroll(top: number)</td><td>滚动回调</td><td>-</td></tr><tr><td>adjustTop(commentsData: ICommentsData[])</td><td>文档修改时，适配评论高度</td><td>-</td></tr></tbody></table>

#### options.preview

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>delay</td><td>预览 debounce 毫秒间隔</td><td>1000</td></tr><tr><td>maxWidth</td><td>预览区域最大宽度</td><td>800</td></tr><tr><td>mode</td><td>显示模式：both, editor</td><td>'both'</td></tr><tr><td>url</td><td>md 解析请求</td><td>-</td></tr><tr><td>parse(element: HTMLElement)</td><td>预览回调</td><td>-</td></tr><tr><td>transform(html: string): string</td><td>渲染之前回调</td><td>-</td></tr></tbody></table>

#### options.preview.hljs

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>enable</td><td>是否启用代码高亮</td><td>true</td></tr><tr><td>style</td><td>可选值参见 <a href="https://link.ld246.com/forward?goto=https%3A%2F%2Fxyproto.github.io%2Fsplash%2Fdocs%2Flonger%2Fall.html" target="_blank" rel="nofollow ugc">Chroma</a></td><td><code>github</code></td></tr><tr><td>lineNumber</td><td>是否启用行号</td><td>false</td></tr></tbody></table>

#### options.preview.markdown

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>autoSpace</td><td>自动空格</td><td>false</td></tr><tr><td>fixTermTypo</td><td>自动矫正术语</td><td>false</td></tr><tr><td>toc</td><td>插入目录</td><td>false</td></tr><tr><td>footnotes</td><td>脚注</td><td>true</td></tr><tr><td>codeBlockPreview</td><td>wysiwyg 和 ir 模式下是否对代码块进行渲染</td><td>true</td></tr><tr><td>mathBlockPreview</td><td>wysiwyg 和 ir 模式下是否对数学公式进行渲染</td><td>true</td></tr><tr><td>paragraphBeginningSpace</td><td>段落开头空两个</td><td>false</td></tr><tr><td>sanitize</td><td>是否启用过滤 XSS</td><td>true</td></tr><tr><td>listStyle</td><td>为列表添加 data-style 属性</td><td>false</td></tr><tr><td>linkBase</td><td>链接相对路径前缀</td><td>''</td></tr><tr><td>linkPrefix</td><td>链接强制前缀</td><td>''</td></tr><tr><td>mark</td><td>启用 mark 标记</td><td>false</td></tr></tbody></table>

#### options.preview.theme

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>current</td><td>当前主题</td><td>"light"</td></tr><tr><td>list</td><td>可选主题列表</td><td>{dark: "Dark", light: "Light", wechat: "WeChat"}</td></tr><tr><td>path</td><td>主题样式地址</td><td><code>https://cdn.jsdelivr.net/npm/vditor@${VDITOR_VERSION}/dist/css/content-theme</code></td></tr></tbody></table>

#### options.preview.math

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>inlineDigit</td><td>内联数学公式起始 $ 后是否允许数字</td><td>false</td></tr><tr><td>macros</td><td>使用 MathJax 渲染时传入的宏定义</td><td>{}</td></tr><tr><td>engine</td><td>数学公式渲染引擎：KaTeX, MathJax</td><td>'KaTeX'</td></tr></tbody></table>

#### options.preview.actions?: Array<IPreviewAction | IPreviewActionCustom>

默认值为 ["desktop", "tablet", "mobile", "mp-wechat", "zhihu"]。  
可从默认值中挑选进行配置，也可使用以下字段进行自定制开发。

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>key</td><td>按钮唯一标识，不能为空</td><td>-</td></tr><tr><td>text</td><td>按钮文字</td><td>-</td></tr><tr><td>tooltip</td><td>提示</td><td>-</td></tr><tr><td>className</td><td>按钮类名</td><td>-</td></tr><tr><td>click(key: string)</td><td>按钮点击回调事件</td><td>-</td></tr></tbody></table>

#### options.hint

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>parse</td><td>是否进行 md 解析</td><td>true</td></tr><tr><td>delay</td><td>提示 debounce 毫秒间隔</td><td>200</td></tr><tr><td>emoji</td><td>默认表情，可从 <a href="https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2F88250%2Flute%2Fblob%2Fmaster%2Fparse%2Femoji_map.go" target="_blank" rel="nofollow ugc">lute/emoji_map</a> 中选取，也可自定义</td><td>{'+1': '👍', '-1': '👎', 'heart': '❤️', 'cold_sweat': '😰'}</td></tr><tr><td>emojiTail</td><td>常用表情提示</td><td>-</td></tr><tr><td>emojiPath</td><td>表情图片地址</td><td><code>https://cdn.jsdelivr.net/npm/vditor@${VDITOR_VERSION}/dist/images/emoji</code></td></tr><tr><td>extend: IHintExtend[]</td><td>对 @/ 话题等关键字自动补全的扩展</td><td>[]</td></tr></tbody></table>

```
interface IHintExtend {
    key: string;

    hint?(value: string): Array<{
        html: string;
        value: string;
    }>;
}
```

#### options.upload

*   文件上传的数据结构如下。后端返回的数据结构不一致时，可使用 `format` 进行转换。

```
// POST data  
xhr.send(formData);  // formData = FormData.append("file[]", File)  
// return data  
{  
 "msg": "",  
 "code": 0,  
 "data": {  
 "errFiles": ['filename', 'filename2'],  
 "succMap": {  
   "filename3": "filepath3",  
   "filename3": "filepath3"  
   }  
 }  
}
```

*   为了防止站外图片失效， `linkToImgUrl` 可将剪贴板中的站外图片地址传到服务器端进行保存处理，其数据结构如下：

```
// POST data  
xhr.send(JSON.stringify({url: src})); // src 为站外图片地址  
// return data  
{  
 msg: '',  
 code: 0,  
 data : {  
   originalURL: '',  
   url: ''  
 }  
}
```

*   `success`，`format`，`error` 不会同时触发，具体调用情况如下：

```
if (xhr.status === 200) {
    if (vditor.options.upload.success) {
        vditor.options.upload.success(editorElement, xhr.responseText);
    } else {
        let responseText = xhr.responseText;
        if (vditor.options.upload.format) {
            responseText = vditor.options.upload.format(files as File [], xhr.responseText);
        }
        genUploadedLabel(responseText, vditor);
    }
} else {
    if (vditor.options.upload.error) {
        vditor.options.upload.error(xhr.responseText);
    } else {
        vditor.tip.show(xhr.responseText);
    }
}
```

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>url</td><td>上传 url</td><td>''</td></tr><tr><td>max</td><td>上传文件最大 Byte</td><td>10 * 1024 * 1024</td></tr><tr><td>linkToImgUrl</td><td>剪切板中包含图片地址时，使用此 url 重新上传</td><td>''</td></tr><tr><td>linkToImgCallback(responseText: string)</td><td>图片地址上传回调</td><td>-</td></tr><tr><td>linkToImgFormat(responseText: string): string</td><td>对图片地址上传的返回值进行格式化</td><td>-</td></tr><tr><td>success(editor: HTMLPreElement, msg: string)</td><td>上传成功回调</td><td>-</td></tr><tr><td>error(msg: string)</td><td>上传失败回调</td><td>-</td></tr><tr><td>token</td><td>CORS 上传验证，头为 X-Upload-Token</td><td>-</td></tr><tr><td>withCredentials</td><td>跨站点访问控制</td><td>false</td></tr><tr><td>headers</td><td>请求头设置</td><td>-</td></tr><tr><td>filename(name: string): string</td><td>文件名安全处理</td><td>name =&gt; name.replace(/\W/g, '')</td></tr><tr><td>accept</td><td>文件上传类型，同 <a href="https://link.ld246.com/forward?goto=https%3A%2F%2Fwww.w3schools.com%2Ftags%2Fatt_input_accept.asp" target="_blank" rel="nofollow ugc">input accept</a></td><td>-</td></tr><tr><td>validate(files: File[]) =&gt; string | boolean</td><td>校验，成功时返回 true 否则返回错误信息</td><td>-</td></tr><tr><td>handler(files: File[]) =&gt; string | null</td><td>自定义上传，当发生错误时返回错误信息</td><td>-</td></tr><tr><td>format(files: File[], responseText: string): string</td><td>对服务端返回的数据进行转换，以满足内置的数据结构</td><td>-</td></tr><tr><td>file(files: File[]): File[]</td><td>将上传的文件处理后再返回</td><td>-</td></tr><tr><td>setHeaders(): { [key: string]: string }</td><td>上传前使用返回值设置头</td><td>-</td></tr><tr><td>extraData: {[key: string]: string | Blob }</td><td>为 FormData 添加额外的参数</td><td>-</td></tr><tr><td>multiple</td><td>上传文件是否为多个</td><td>true</td></tr><tr><td>fieldName</td><td>上传字段名称</td><td>'file[]'</td></tr></tbody></table>

#### options.resize

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>enable</td><td>是否支持大小拖拽</td><td>false</td></tr><tr><td>position</td><td>拖拽栏位置：'top', 'bottom'</td><td>'bottom'</td></tr><tr><td>after(height: number)</td><td>拖拽结束的回调</td><td>-</td></tr></tbody></table>

#### options.classes

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>preview</td><td>预览元素上的 className</td><td>''</td></tr></tbody></table>

#### options.fullscreen

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>index</td><td>全屏层级</td><td>90</td></tr></tbody></table>

#### options.outline

<table><thead><tr><th></th><th>说明</th><th>默认值</th></tr></thead><tbody><tr><td>enable</td><td>初始化是否展现大纲</td><td>false</td></tr><tr><td>position</td><td>大纲位置：'left', 'right'</td><td>'left'</td></tr></tbody></table>

#### methods

<table><thead><tr><th></th><th>说明</th></tr></thead><tbody><tr><td>getValue()</td><td>获取 Markdown 内容</td></tr><tr><td>getHTML()</td><td>获取 HTML 内容</td></tr><tr><td>insertValue(value: string, render = true)</td><td>在焦点处插入内容，并默认进行 Markdown 渲染</td></tr><tr><td>focus()</td><td>聚焦到编辑器</td></tr><tr><td>blur()</td><td>让编辑器失焦</td></tr><tr><td>disabled()</td><td>禁用编辑器</td></tr><tr><td>enable()</td><td>解除编辑器禁用</td></tr><tr><td>getSelection(): string</td><td>返回选中的字符串</td></tr><tr><td>setValue(markdown: string, clearStack = false)</td><td>设置编辑器内容且选中清空历史栈</td></tr><tr><td>clearStack()</td><td>清空撤销和重做记录栈</td></tr><tr><td>renderPreview(value?: string)</td><td>设置预览区域内容</td></tr><tr><td>getCursorPosition():{top: number, left: number}</td><td>获取焦点位置</td></tr><tr><td>deleteValue()</td><td>删除选中内容</td></tr><tr><td>updateValue(value: string)</td><td>更新选中内容</td></tr><tr><td>isUploading()</td><td>上传是否还在进行中</td></tr><tr><td>clearCache()</td><td>清除缓存</td></tr><tr><td>disabledCache()</td><td>禁用缓存</td></tr><tr><td>enableCache()</td><td>启用缓存</td></tr><tr><td>html2md(value: string)</td><td>HTML 转 md</td></tr><tr><td>tip(text: string, time: number)</td><td>消息提示。time 为 0 将一直显示</td></tr><tr><td>setPreviewMode(mode: "both" | "editor")</td><td>设置预览模式</td></tr><tr><td>setTheme(theme: "dark" | "classic", contentTheme?: string, codeTheme?: string, contentThemePath?: string)</td><td>设置主题、内容主题及代码块风格</td></tr><tr><td>getCurrentMode(): string</td><td>获取编辑器当前编辑模式</td></tr><tr><td>destroy()</td><td>销毁编辑器</td></tr><tr><td>getCommentIds(): {id: string, top: number}[]</td><td>获取所有评论</td></tr><tr><td>hlCommentIds(ids: string[])</td><td>高亮评论</td></tr><tr><td>unHlCommentIds(ids: string[])</td><td>取消评论高亮</td></tr><tr><td>removeCommentIds(removeIds: string[])</td><td>删除评论</td></tr></tbody></table>

#### static methods

*   不需要进行编辑操作时，仅需引入 [`method.min.js`](https://link.ld246.com/forward?goto=https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Fvditor%2Fdist%2F) 后如下直接调用

```
Vditor.mermaidRender(document)
```

```
import VditorPreview from 'vditor/dist/method.min'  
VditorPreview.mermaidRender(document)
```

*   需要对页面中的 Markdown 进行渲染时可直接调用 `preview` 方法，参数如下：

```
previewElement: HTMLDivElement,   // 使用该元素进行渲染
markdown: string,  // 需要渲染的 markdown 原文
options?: IPreviewOptions {
  mode: "dark" | "light";
  anchor?: number;  // 为标题添加锚点 0：不渲染；1：渲染于标题前；2：渲染于标题后，默认 0
  customEmoji?: { [key: string]: string };    // 自定义 emoji，默认为 {}  
  lang?: (keyof II18nLang);    // 语言，默认为 'zh_CN'  
  emojiPath?: string;    // 表情图片路径 
  hljs?: IHljs; // 参见 options.preview.hljs 
  speech?: {  // 对选中后的内容进行阅读
    enable?: boolean,
  };
  math?: IMath; // 数学公式渲染配置
  cdn?: string; // 自建 CDN 地址
  transform?(html: string): string; // 在渲染前进行的回调方法
  after?(); // 渲染完成后的回调
  lazyLoadImage?: string; // 设置为 Loading 图片地址后将启用图片的懒加载
  markdown?: options.preview.markdown;
  theme?: options.preview.theme;
  renderers?: ILuteRender; // 自定义渲染 https://ld246.com/article/1588412297062
}
```

*   ⚠️ `method.min.js` 和 `index.min.js` 不可同时引入

<table><thead><tr><th></th><th>说明</th></tr></thead><tbody><tr><td>previewImage(oldImgElement: HTMLImageElement, lang: keyof II18n = "zh_CN", theme = "classic")</td><td>点击图片预览</td></tr><tr><td>mermaidRender(element: HTMLElement, cdn = options.cdn, theme = options.theme)</td><td>流程图 / 时序图 / 甘特图</td></tr><tr><td>flowchartRender(element: HTMLElement, cdn = options.cdn)</td><td>flowchart 渲染</td></tr><tr><td>codeRender(element: HTMLElement, lang: (keyof II18nLang) = "zh_CN")</td><td>为 element 中的代码块添加复制按钮</td></tr><tr><td>chartRender(element: (HTMLElement | Document) = document, cdn = options.cdn, theme = options.theme)</td><td>图表渲染</td></tr><tr><td>mindmapRender(element: (HTMLElement | Document) = document, cdn = options.cdn, theme = options.theme)</td><td>脑图渲染</td></tr><tr><td>plantumlRender(element: (HTMLElement | Document) = document, cdn = options.cdn)</td><td>plantuml 渲染</td></tr><tr><td>abcRender(element: (HTMLElement | Document) = document, cdn = options.cdn)</td><td>五线谱渲染</td></tr><tr><td>md2html(mdText: string, options?: IPreviewOptions): Promise&lt;string&gt;</td><td>Markdown 文本转换为 HTML，该方法需使用<a href="https://ld246.com/article/1546828434083?r=Vanessa#toc_h3_1">异步编程</a></td></tr><tr><td>preview(previewElement: HTMLDivElement, markdown: string, options?: IPreviewOptions)</td><td>页面 Markdown 文章渲染</td></tr><tr><td>highlightRender(hljsOption?: IHljs, element?: HTMLElement | Document, cdn = options.cdn)</td><td>为 element 中的代码块进行高亮渲染</td></tr><tr><td>mediaRender(element: HTMLElement)</td><td>为<a href="https://ld246.com/article/1589813914768">特定链接</a>分别渲染为视频、音频、嵌入的 iframe</td></tr><tr><td>mathRender(element: HTMLElement, options?: {cdn?: string, math?: IMath})</td><td>对数学公式进行渲染</td></tr><tr><td>speechRender(element: HTMLElement, lang?: (keyof II18nLang))</td><td>对选中的文字进行阅读</td></tr><tr><td>graphvizRender(element: HTMLElement, cdn?: string)</td><td>对 graphviz 进行渲染</td></tr><tr><td>outlineRender(contentElement: HTMLElement, targetElement: Element)</td><td>对大纲进行渲染</td></tr><tr><td>lazyLoadImageRender(element: (HTMLElement | Document) = document)</td><td>对启用懒加载的图片进行渲染</td></tr><tr><td>setCodeTheme(codeTheme: string, cdn = options.cdn)</td><td>设置代码主题，codeTheme 参见 options.preview.hljs.style</td></tr><tr><td>setContentTheme(contentTheme: string, path: string)</td><td>设置内容主题，contentTheme 参见 options.preview.theme.list</td></tr></tbody></table>

🏗 开发文档
-------

### 原理相关

*   [关于所见即所得 Markdown 编辑器的讨论](https://ld246.com/article/1579414663700)
*   [Vditor 实现 Markdown 所见即所得](https://ld246.com/article/1577370404903)
*   [Lute 一款对中文语境优化的 Markdown 引擎，支持 Go 和 JavaScript](https://ld246.com/article/1567047822949)

### 环境

1.  安装 [node](https://link.ld246.com/forward?goto=https%3A%2F%2Fnodejs.org%2F) LTS 版本
2.  [下载](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Farchive%2Fmaster.zip)最新代码并解压
3.  根目录运行 `npm install`
4.  `npm run start` 启动本地服务器，打开 http://localhost:9000
5.  修改代码
6.  `npm run build` 打包代码到 dist 目录

### CDN 切换

由于使用了按需加载的机制，默认 CDN 为 [https://cdn.jsdelivr.net/npm/vditor](https://link.ld246.com/forward?goto=https%3A%2F%2Fcdn.jsdelivr.net%2Fnpm%2Fvditor)@版本号

如果代码有修改或需要使用自建 CDN 的话，可按以下步骤进行操作：

*   初始化时，需对 `options` 及 `IPreviewOptions` 中的 `cdn`，`emojiPath`, `themes` 进行配置
*   `highlightRender` , `mathRender` , `abcRender` , `chartRender` , `mermaidRender`， `flowchartRender`，`mindmapRender`，`graphvizRender`，`setCodeTheme`，`setContentTheme` 方法中需添加 cdn 参数
*   将 build 成功的 dist 目录或 [jsDelivr](https://link.ld246.com/forward?goto=https%3A%2F%2Fwww.jsdelivr.com%2Fpackage%2Fnpm%2Fvditor%3Fpath%3Ddist) 中的 dist 目录拷贝至正确的位置

### 升级

版本升级时请**仔细阅读** [CHANGELOG](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fblob%2Fmaster%2FCHANGELOG.md) 中的**升级**部分

Ⓜ️ Markdown 使用指南
----------------

*   [基础语法](https://ld246.com/article/1583129520165)
*   [扩展语法](https://ld246.com/article/1583305480675)
*   [速查手册](https://ld246.com/article/1583308420519)

🏘️ 社区
------

*   [官网](https://link.ld246.com/forward?goto=https%3A%2F%2Fb3log.org%2Fvditor)
*   [讨论区](https://ld246.com/tag/vditor)
*   [报告问题](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2FVanessa219%2Fvditor%2Fissues%2Fnew)

📄 授权
-----

Vditor 使用 [MIT](https://link.ld246.com/forward?goto=https%3A%2F%2Fopensource.org%2Flicenses%2FMIT) 开源协议。

🙏 鸣谢
-----

*   [Lute](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2F88250%2Flute)：🎼 一款结构化的 Markdown 引擎，支持 Go 和 JavaScript
*   [highlight.js](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2Fhighlightjs%2Fhighlight.js)：JavaScript syntax highlighter
*   [mermaid](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2Fknsv%2Fmermaid)：Generation of diagram and flowchart from text in a similar manner as Markdown
*   [incubator-echarts](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2Fapache%2Fincubator-echarts)：A powerful, interactive charting and visualization library for browser
*   [abcjs](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2Fpaulrosen%2Fabcjs)：JavaScript library for rendering standard music notation in a browser

📽️ 历史
------

我们在开发 [Sym](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2F88250%2Fsymphony) 的初期是直接使用 WYSIWYG 富文本编辑器的。那时候基于 HTML 的编辑器非常流行，项目中引用起来也很方便，也符合用户当时的使用习惯。

后来，Markdown 的崛起逐步改变了大家的排版方式。再加上我们其他几个项目都是面向程序员用户的，所以迁移到 md 上也是大势所趋。我们选择了 [CodeMirror](https://link.ld246.com/forward?goto=https%3A%2F%2Fgithub.com%2Fcodemirror%2FCodeMirror)，这是一款优秀的编辑器，它对开发者提供了丰富的编程接口，对各种浏览器的兼容性也比较好。

再后来，随着我们项目业务需求方面的沉淀，使用 CodeMirror 有时候会感到比较 “笨重”。比如要实现 @自动完成用户名列表、插入 Emoji、上传文件等就需要比较深入的二次开发，而这些业务需求恰恰是很多项目场景共有且必备的。

终于，我们决定开始在 Sym 中自己实现编辑器。随着几个版本的迭代，Sym 的编辑器也日趋成熟。在我们运营的社区[链滴](https://ld246.com/)上陆续有人问我们是否能将编辑器单独抽离出来提供给大家使用。与此同时，我们的前端主程 [V](https://ld246.com/member/Vanessa) 同学对于维护分散在各个项目中的编辑器也感到有点力不从心，外加对 TypeScript 的好感，所以就决定使用 ts 来实现一个全新的浏览器端 md 编辑器。

于是，Vditor 就这样诞生了。

[Demo 源码](https://github.com/Vanessa219/b3log-index/tree/master/src/vditor/demo)

### 🏡 使用场景

- [完整示例](https://ld246.com/guide/markdown)
- [如何在 React 中使用](https://b3log.org/vditor/demo/react.html)
- [如何在 Vue 中使用](https://b3log.org/vditor/demo/vue.html)
- [如何在 Angular 中使用](https://b3log.org/vditor/demo/angular.html)

### 👗 页面渲染

- [完整示例](https://b3log.org/vditor/demo/preview.html)
- [自定义渲染](https://b3log.org/vditor/demo/preview-custom.html)
- [功能渲染](https://b3log.org/vditor/demo/preview-render.html) - Markdown2HTML / 大纲 / 数学公式 / 脑图 / 图表 / 流程图 / 甘特图 / 时序图 / 五线谱 / 多媒体 / 代码高亮 / 代码复制 /graphviz/flowchart/plantuml/ 图片预览
- [渲染配置](https://b3log.org/vditor/demo/preview-config.html) - 锚点 / 语音阅读 / 图片懒加载 / 渲染前回调 / 渲染后回调

### ⚙️️ 基本配置

- [编辑模式](https://b3log.org/vditor/demo/option-mode.html) - wysiwyg/ir/sv
- [图标配置](https://b3log.org/vditor/demo/option-icon.html) - Ant Design/Material
- [大小及自适应](https://b3log.org/vditor/demo/option-size.html)
- [多语言](https://b3log.org/vditor/demo/option-lang.html)
- [CDN 配置](https://ld246.com/article/1549638745630#CDN-切换)
- [回调事件](https://b3log.org/vditor/demo/option-callback.html) - 渲染完成 / 用户输入 / 聚焦 / 失焦 / 选择文字 / ESC/Ctrl+Enter
- [实用小特性](https://b3log.org/vditor/demo/option-other.html) - tab / 打字机模式 / 内容为空的提示 / 历史延时 / 全屏层级

### 👠 高级配置

- [Markdown 配置](https://b3log.org/vditor/demo/advanced-markdown.html) - 自动空格 / 段落开头空两格 / 矫正术语 / 启用目录 / 禁用脚注 / 启用 Mark 标记 /wysiwyg & ir 模式不渲染代码块 / 不过滤 XSS / 主题 / 为列表添加标记
- [工具栏](https://b3log.org/vditor/demo/advanced-toolbar.html) - 自定义按钮 / 新增按钮 / 固定 / 隐藏
- [文件上传](https://b3log.org/vditor/demo/advanced-upload.html)
- [大纲](https://b3log.org/vditor/demo/advanced-outline.html) - 显示大纲 / 大纲位置
- [预览](https://b3log.org/vditor/demo/advanced-preview.html) - 延迟解析 / HTML 字符串处理 / DOM 处理 / 预览请求
- [预览操作的配置及自定义](https://b3log.org/vditor/demo/advanced-preview-actions.html)
- [自动补全](https://b3log.org/vditor/demo/advanced-hint.html) - @、话题等关键字扩展 / 自定义表情 / 表情图片地址 / 表情提示
- [字数统计](https://b3log.org/vditor/demo/advanced-counter.html) - Markdown / 文本 / 最大字数提示 / 回调
- [拖拽调整编辑器高度](https://b3log.org/vditor/demo/advanced-resize.html) - 启用 / 位于底部 / 位于顶部 / 拖拽结束回调
- [代码块高亮](https://b3log.org/vditor/demo/advanced-hljs.html) - 启用高亮 / 代码块块样式 / 行号
- [数学公式](https://b3log.org/vditor/demo/advanced-math.html) - KaTeX，MathJax 引擎切换 / 设置 MathJax 宏定义 / 允许 $ 后出现数字
- [本地缓存](https://b3log.org/vditor/demo/advanced-cache.html) - 设置默认值 / 设置缓存 ID / 清除缓存 / 禁用缓存 / 启用缓存 / 缓存回调
- [划词评论](https://b3log.org/vditor/demo/advanced-comment.html) - 目前仅支持 wysiwyg 模式

### 🎨 基本方法

- [主题修改](https://b3log.org/vditor/demo/method-theme.html) - 编辑器 / 内容 / 代码块渲染 / [自定义主题](https://ld246.com/article/1549638745630#主题)
- [文本操作](https://b3log.org/vditor/demo/method-CRUD.html) - 更新内容 / 更新内容并清空历史栈 / 插入内容 / 更新选中内容 / 删除选中内容 / 设置预览区域内容
- [获取](https://b3log.org/vditor/demo/method-get.html) - Markdown/HTML/ 选中的文本 / 编辑器模式 / 光标位置 / HTML->Markdown
- [其他方法](https://b3log.org/vditor/demo/method-other.html) - 设置为只读 / 聚焦 / 失焦 / 消息提示 / 销毁 / 清空历史栈

### 💛 暖心示例

- [移动端最佳配置](https://b3log.org/vditor/demo/sweet-mobile.html)
- [多个编辑器共存](https://b3log.org/vditor/demo/sweet-two.html)
- 在 sv 模式下点击工具栏上的格式化可对 Markdwon 原文进行格式化
- 点击工具栏上的开发者工具可查看 Markdown 语法树

作者：Vanessa
链接：https://ld246.com/article/1549638745630
来源：链滴
协议：CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/