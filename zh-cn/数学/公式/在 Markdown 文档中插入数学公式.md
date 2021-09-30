# 在 Markdown 文档中插入数学公式



## 数学符号

### 上下标，正负无穷

| 数学表达式 | LaTeX代码 |
| ---------- | --------- |
| $x^2$      | x^2       |
| $y_1$      | y_1       |
| $\infty$   | \infty    |
| $-\infty$  | -\infty   |

### 运算符

#### 特殊运算符号

| 数学表达式 | LaTeX代码 | 数学表达式 | LaTeX代码 |
| ---------- | --------- | ---------- | --------- |
| $\pm$      | \pm       | $\mp$      | \mp       |
| $\div$     | \div      | $\times$   | \times    |
| $\geq$     | \geq      | $\leq$     | \leq      |
| $\approx$  | \approx   | $\neq$     | \neq      |
| $\sum$     | \sum      | $\equiv$   | \equiv    |
| $\log$     | \log      | $\prod$    | \prod     |
| $\lg$      | \lg       | $\ln$      | \ln       |
| $\int$     | \int      | $\sin$     | \sin      |
| $\lim$     | \lim      | $\iint$    | \iint     |
| $\notin$   | \notin    | $\in$      | \in       |
| $\subset$  | \subset   |            |           |



#### 关系运算符

| 数学表达式 | LaTeX代码 |
| ---------- | --------- |
| $\leq$     | \leq      |
| $\geq$     | \geq      |

#### 加减乘除四则运算, 上下标，分数，根号，省略号

| 数学表达式                                       | LaTeX代码                                  |
| ------------------------------------------------ | ------------------------------------------ |
| $a+b-c*d$                                        | a+b-c*d                                    |
| $a\div{b}$                                       | a\div{b}                                   |
| $a\pm{b}$                                        | a\pm{b}                                    |
| $A=x_1^2+x_2^2$                                  | `A=x_1^2+x_2^2`                            |
| $\frac{a}{b}$    $\frac{1}{2}$    $\dfrac{x}{y}$ | \frac{a}{b}    \frac{1}{2}    \dfrac{x}{y} |
| $\sqrt{b}$    $\sqrt{3}$    $\sqrt[3]{x}$        | \sqrt{b}     \sqrt{3}    \sqrt[3]{x}       |
| $\cdots$                                         | \cdots                                     |

#### 三角函数

| 数学表达式     | LaTeX代码    |
| -------------- | ------------ |
| $\sin{\theta}$ | \sin{\theta} |
| $\cos{\theta}$ | \cos{\theta} |
| $\tan{\theta}$ | \tan{\theta} |
| $\cot{\theta}$ | \cot{\theta} |

#### 矢量，累加累乘，极限

| 数学表达式                        | LaTeX代码                       |
| --------------------------------- | ------------------------------- |
| $\vec{F}$                         | \vec{F}                         |
| $\sum_{i=1}^{n}{a_i}$             | \sum_{i=1}^{n}{a_i}             |
| $\prod_{i=1}^{n}{a_i}$            | \prod_{i=1}^{n}{a_i}            |
| $\lim_{a\rightarrow+\infty}{a+b}$ | \lim_{a\rightarrow+\infty}{a+b} |

#### 集合

| 数学表达式  | LaTeX代码 | 数学表达式   | LaTeX代码  | 数学表达式  | LaTeX代码 |
| ----------- | --------- | ------------ | ---------- | ----------- | --------- |
| $\sum$      | \sum      | $\prod$      | \prod      | $\coprod$   | \coprod   |
| $\int$      | \int      | $\oint$      | \oint      | $\iint$     | \iint     |
| $\biguplus$ | \biguplus | $\bigcap$    | \bigcap    | $\bigcup$   | \bigcup   |
| $\bigoplus$ | \bigoplus | $\bigotimes$ | \bigotimes | $\bigodot$  | \bigodot  |
| $\bigvee$   | \bigvee   | $\bigwedge$  | \bigwedge  | $\bigsqcup$ | \bigsqcup |



### 数学结构

 $\vec x$

```text
 $\vec x$
```

| 数学表达式             | LaTeX代码            | 数学表达式            | LaTeX代码           |
| ---------------------- | -------------------- | --------------------- | ------------------- |
| $\frac{abc}{xyz}$      | \frac{abc}{xyz}      | $f'$                  | f'                  |
| $\overline{abc}$       | \overline{abc}       | $\underline{abc}$     | \underline{abc}     |
| $\overrightarrow{abc}$ | \overrightarrow{abc} | $\overleftarrow{abc}$ | \overleftarrow{abc} |
| $\underrightarrow{abc}$ | \underrightarrow{abc} | $\underleftarrow{abc}$ | \underleftarrow{abc} |
| $\sqrt{abc}$           | \sqrt{abc}           | $\sqrt[n]{abc}$       | \sqrt[n]{abc}       |
| $\widehat{abc}$        | \widehat{abc}        | $\widetilde{abc}$     | \widetilde{abc}     |
| $\overbrace{abc}$      | \overbrace{abc}      | $\underbrace{abc}$    | \underbrace{abc}    |
| $\vec x$ | \vec x | $\bar x$ |  |
| $\dot x$ |  | $\ddot x$ |  |

$$
\frac{\sqrt{1+abc}}{\sqrt{1-abc}}
$$

```latex
\frac{\sqrt{1+abc}}{\sqrt{1-abc}}
```

## 方程

$$
f'(x) = x^2 + x
$$

```text
$$
 f'(x) = x^2 + x
 $$
```

$$
\lim_{x\to0}\frac{9x^5+7x^3}{x^2+6x^8}
$$

```
\lim_{x\to0}\frac{9x^5+7x^3}{x^2+6x^8}
```

$$
\int_a^b f(x)\,dx
$$

```
\int_a^b f(x)\,dx
```

$$
\int_0^{+\infty}f(x)\,dx
$$



```
\int_0^{+\infty}f(x)\,dx
```


$$
\int_{x^2+y^2\leq R^2} \,f(x,y)\,dx\,dy = \int_{\theta=0}^{2\pi}\int_{r=0}^R \,f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta
$$


```
\int_{x^2+y^2\leq R^2} \,f(x,y)\,dx\,dy = \int_{\theta=0}^{2\pi}\int_{r=0}^R \,f(r\cos\theta,r\sin\theta)\,r\,dr\,d\theta
```

$$
\int\!\!\!\int_D f(x,y)dxdy
$$

```
\int\!\!\!\int_D f(x,y)dxdy
```

#### 二次方程求解

$\mathbf{a*x^2+b*x+c}$

$$x={\frac{-b \pm \sqrt{b^2-4ac}}{2a}}$$ or $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

```
$\mathbf{a*x^2+b*x+c}$

$$x={\frac{-b \pm \sqrt{b^2-4ac}}{2a}}$$ or $$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$
```



### 多行等式对齐

$$
\begin{aligned}
a&=b+c\\
&=d+e+f
\end{aligned}
$$

```latex
\begin{aligned}
a&=b+c\\
&=d+e+f
\end{aligned}
```



### 方程组

$$
\begin{cases}
3x+5y+z\\
7x-2y+4z\\
-6x+3y+2z
\end{cases}
$$

```latex
\begin{cases}
3x+5y+z\\
7x-2y+4z\\
-6x+3y+2z
\end{cases}
```

$$
\begin{equation}
% \begin{equation*} 加'*'去掉公式编号
\left\{
\begin{aligned}     %请使用'aligned'或'align*'
2x + y  &= 1  \\     %加'&'指定对齐位置
2x + 2y &= 2
\end{aligned}
\right.
\end{equation}
% \end{equation*}  加'*'去掉公式编号
$$



```
\begin{equation}
% \begin{equation*} 加'*'去掉公式编号
\left\{
\begin{aligned}     %请使用'aligned'或'align*'
2x + y  &= 1  \\     %加'&'指定对齐位置
2x + 2y &= 2
\end{aligned}
\right.
\end{equation}
% \end{equation*}   加'*'去掉公式编号

% 注意：在 markdown 环境下，某些特殊字符，如'\', '*'等，会首先被 markdown 语法转义，然后再被 Latex 转义。
% 因此有时候 '\{'需要写作'\\{'，'*'需要写作'\*'，'\\'需要写作'\\\\'等，视不同的解释环境而定
```

注：如果各个方程需要在某个字符处对齐（如等号对齐），只需在所有要对齐的字符前加上 & 符号。如果不需要公式编号，只需在宏包名称后加上 * 号。

分情况讨论方程式
$$
f(x) =
\begin{cases}
x^2 \qquad & a \gt 0 \\
e^x \qquad & a \le 0
\end{cases}
$$


```
f(x) =
\begin{cases}
x^2 \qquad & a \gt 0 \\
e^x \qquad & a \le 0
\end{cases}
```

### 条件表达式

$$
f(n)=
\begin{cases}
n/2,&\text{if }n\text{ is even}\\
3n+1,&\text{if }n\text{ is odd}
\end{cases}
$$

```latex
f(n)=
\begin{cases}
n/2,&\text{if }n\text{ is even}\\
3n+1,&\text{if }n\text{ is odd}
\end{cases}
```

$$
 f(x) = 
 \begin{cases}
 2x,\,\,x>0\\
 3x,\,\,x\le0\\
 \end{cases}
$$

```latex
 f(x) = 
 \begin{cases}
 2x,\,\,x>0\\
 3x,\,\,x\le0\\
 \end{cases}
```



## 表格

### 简易表格

$$
\begin{array}{|c|c|c|}
\hline 2&9&4\\
\hline 7&5&3\\
\hline 6&1&8\\
\hline
\end{array}
$$

```latex
\begin{array}{|c|c|c|}
\hline 2&9&4\\
\hline 7&5&3\\
\hline 6&1&8\\
\hline
\end{array}
```

开头结尾： \begin{array} ， \end{array}

定义式：例：{|c|c|c|}，其中 c l r 分别代表居中、左对齐及右对齐。

分割线：①竖直分割线：在定义式中插入 |， （|| 表示两条竖直分割线）。

②水平分割线：在下一行输入前插入 \hline，以下图真值表为例。

其他：每行元素间均须要插入 & ，每行元素以 \\ 结尾。

### 真值表

$$
\begin{array}{cc|c}
A&B&F\\
\hline0&0&0\\
0&1&1\\
1&0&1\\
1&1&1\\
\end{array}
$$

```latex
\begin{array}{cc|c}
A&B&F\\
\hline0&0&0\\
0&1&1\\
1&0&1\\
1&1&1\\
\end{array}
```



## 矩阵

### 简单矩阵

$$
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}\tag{1}
$$

```latex
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}\tag{1}
```

### 带左右括号的矩阵 (大中小括号)

#### 1.在 \begin{} 之前和 \end{} 之后添加左右括号的代码。

##### 大括号：

$$
\left\{
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}
\right\}\tag{2}
$$

```latex
\left\{
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}
\right\}\tag{2}
```

##### 中括号：

$$
\left[
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}
\right]\tag{3}
$$

```latex
\left[
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}
\right]\tag{3}
```

##### 小括号：

$$
\left(
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}
\right)\tag{4}
$$

```latex
\left(
\begin{matrix}
1&2&3\\
4&5&6\\
7&8&9
\end{matrix}
\right)\tag{4}
```

#### 2改变 \begin{matrix} 和 \end{matrix} 中 {matrix}

##### 大括号：

$$
\begin{Bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{Bmatrix}\tag{6}
$$

```latex
\begin{Bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{Bmatrix}\tag{6}
```

##### 中括号：

$$
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}\tag{7}
$$

```latex
\begin{bmatrix}
1&2&3\\
4&5&6\\
7&8&9
\end{bmatrix}\tag{7}
```

##### 小括号

$$
\begin{pmatrix}
0&1&2\\
3&4&5\\
6&7&8\\
\end{pmatrix}
$$

```latex
\begin{pmatrix}
0&1&2\\
3&4&5\\
6&7&8\\
\end{pmatrix}
```

##### 竖线

$$
\begin{vmatrix}
 0&1&2\\
 3&4&5\\
 6&7&8\\
 \end{vmatrix}
$$

```latex
\begin{vmatrix}
 0&1&2\\
 3&4&5\\
 6&7&8\\
 \end{vmatrix}
```

##### 双竖线

$$
\begin{Vmatrix}
 0&1&2\\
 3&4&5\\
 6&7&8\\
 \end{Vmatrix}
$$

```latex
\begin{Vmatrix}
 0&1&2\\
 3&4&5\\
 6&7&8\\
 \end{Vmatrix}
```



### 包含希腊字母与省略号

行省略号 \cdots，列省略号 \vdots，斜向省略号（左上至右下）\ddots
$$
\left\{
\begin{matrix}
1&2&\cdots&5\\
6&7&\cdots&10\\
\vdots&\vdots&\ddots&\vdots\\
\alpha&\alpha+1&cdots&\alpha+4
\end{matrix}
\right\}
$$

```latex
\left\{
\begin{matrix}
1&2&\cdots&5\\
6&7&\cdots&10\\
\vdots&\vdots&\ddots&\vdots\\
\alpha&\alpha+1&cdots&\alpha+4
\end{matrix}
\right\}
```



## 希腊字母

当希腊字母的 LaTex 语法首字母大写时，即输出大写的希腊字母；首字母小写时，输出小写的希腊字母。

| 数学表达式                | LaTeX代码 | 大写          | 大写代码 | 汉语名称    | 常用指代意义                                                 |
| ------------------------- | --------- | ------------- | -------- | ----------- | ------------------------------------------------------------ |
| $\alpha$                  | \alpha    | $\Alpha$      | \Alpha | 阿尔法      | 角度、系数、角加速度、第一个、电离度、转化率                 |
| $\beta$                   | \beta     | $\Beta$       | \Beta | 贝塔        | 角度、系数、磁通系数                                         |
| $\gamma$    | \gamma    | $\Gamma$      | \Gamma | 伽玛        | 电导系数、角度、比热容比                                     |
| $\delta$                  | \delta    | $\Delta$      | \Delta | 德尔塔      | 变化量、焓变、熵变、屈光度、一元二次方程中的判别式、化学位移 |
| $\epsilon$  $\varepsilon$ | \epsilon  | $\Epsilon$    | \Epsilon | 艾普西隆    | 对数之基数、介电常数、电容率、应变                           |
| $\zeta$                   | \zeta     | $\Zeta$       | \Zeta | 泽塔        | 系数、方位角、阻抗、相对黏度                                 |
| $\eta$                    | \eta      | $\Eta$        | \Eta | 伊塔        | 迟滞系数、机械效率                                           |
| $\theta$  $\vartheta$       | \theta    | $\Theta$      | \Theta | 西塔        | 温度、角度                                                   |
| $\iota$                   | \iota     | $\Iota$       | \Iota | 约 (yāo) 塔 | 微小、一点                                                   |
| $\kappa$                  | \kappa    | $\Kappa$      | \Kappa | 卡帕        | 介质常数、绝热指数                                           |
| $\lambda$                 | \lambda   | $\Lambda$     | \Lambda | 拉姆达      | 波长、体积、导热系数、普朗克常数                             |
| $\mu$                     | \mu       | $\Mu$         | \Mu | 谬          | 磁导率、微、动摩擦系（因）数、流体动力黏度、货币单位、莫比乌斯函数 |
| $\nu$                     | \nu       | $\Nu$         | \Nu | 纽          | 磁阻系数、流体运动粘度、光波频率、化学计量数                 |
| $\xi$                     | \xi       | $\Xi$         | \Xi | 克西        | 随机变量、（小）区间内的一个未知特定值                       |
| $\omicron$                | \omicron  | $\Omicron$    | \Omicron | 奥米克戎    | 高阶无穷小函数                                               |
| $\pi$  $\varpi$           | \pi       | $\Pi$         | \Pi | 派          | 圆周率、π(n) 表示不大于 n 的质数个数、连乘                   |
| $\rho$  $\varrho$         | \rho      | $\Rho$        | \Rho | 柔          | 电阻率、柱坐标和极坐标中的极径、密度、曲率半径               |
| $\sigma$  $\varsigma$     | \sigma    | $\Sigma$      | \Sigma | 西格马      | 总和、表面密度、跨导、应力、电导率                           |
| $\tau$                    | \tau      | $\Tau$        | \Tau | 陶          | 时间常数、切应力、2π（两倍圆周率）                           |
| $\upsilon$                | \upsilon  | $\Upsilon$    | \Upsilon | 阿普西隆    | 位移                                                         |
| $\phi$  $\varphi$         | \phi      | $\Phi$        | \Phi | 斐          | 磁通量、电通量、角、透镜焦度、热流量、电势、直径、欧拉函数、空集、相位、孔隙度 |
| $\chi$                    | \chi      | $\Chi$        | \Chi | 恺          | 统计学中有卡方 (χ^2) 分布                                    |
| $\psi$                    | \psi      | $\Psi$        | \Psi | 普西        | 角速、介质电通量、ψ 函数、磁链                               |
| $\omega$                  | \omega    | $\Omega$      | \Omega | 欧米伽      | 欧姆、角速度、角频率、交流电的电角度、化学中的质量分数、有机物的不饱和度 |
|                           |           |               |          |             |                                                              |
| $\nabla$                  | \nabla |       |          |             |                                                              |

## 编号

### 插入编号

使用 `\tag` 指令指定公式的具体编号，并使用 `\label` 指令埋下锚点。如 `y=x^2 \tag{1.5a} \label{eq:test}`：
$$
y=x^2 \tag{1.5a} \label{eq:test}
$$


### **引用编号**

使用 `\eqref` 指令引用前面埋下的锚点，`\eqref{eq:test}` 将显示为：![[公式]](https://www.zhihu.com/equation?tex=%5Ceqref%7Beq%3Atest%7D)。(简书里还不支持公式编号的锚点引用)。



## 样式

### 行内公式 `$` + `esc`

 在 `$$` 的中间加入需要的公式

先按 `$` ，再按 `esc`

### 行间公式 `$$`+`回车`

输入 `$$`，再按下回车

### 间隔

紧贴 + 无空格 + 小空格 + 中空格 + 大空格 + 真空格 + 双真空格
$$
a\!b + ab + a\,b + a\;b + a\ b + a\quad b + a\qquad b
$$

```latex
a\!b + ab + a\,b + a\;b + a\ b + a\quad b + a\qquad b
```

紧贴 `\!`

无空格 小空格 `\,` 中空格 `\;` 大空格 `\    `

真空格 `\quad` 双真空格 `\qquad`

###换行 `\\`、空格 `\:`

### 居中 `$$**$$`

### 加粗（mathbf）、斜体（mathit）

$\mathbf{加粗}$

```
\mathbf{加粗}
```

$\mathit{斜体}$

```
\mathit{斜体}
```



### 大小

$$
{\displaystyle \int f(x)\,dx}
$$

```text
 $$
 {\displaystyle \int f(x)\,dx}
 $$
```

$$
{\textstyle \int f(x)\,dx}
$$

```
{\textstyle \int f(x)\,dx}
```

$$
\scriptstyle \int f(x)\,dx
$$

```
\scriptstyle \int f(x)\,dx
```

$$
\scriptscriptstyle \int f(x)\,dx
$$

```
\scriptscriptstyle \int f(x)\,dx
```

$\tiny 萌萌哒$

$\scriptsize 萌萌哒$

$\small 萌萌哒$

$\normalsize 萌萌哒(正常)$

$\large 萌萌哒$

$\Large 萌萌哒$

$\huge 萌萌哒$

$\Huge 萌萌哒$

```
$\tiny 萌萌哒\\$
$\scriptsize 萌萌哒\\$
$\small 萌萌哒\\$
$\normalsize 萌萌哒(正常)\\$
$\large 萌萌哒\\$
$\Large 萌萌哒\\$
$\huge 萌萌哒\\$
$\Huge 萌萌哒\\$
```

### 颜色

$\color{Red}{Red}$, $\color{blue}{Blue}$,  $\color{orange}{Orange}$,  
$\color{Green}{Green}$,  $\color{gray}{Gray}$,  $\color{purple}{Purple}$.

```
$\color{Red}{Red}$, $\color{blue}{Blue}$,  $\color{orange}{Orange}$,  
$\color{Green}{Green}$,  $\color{gray}{Gray}$,  $\color{purple}{Purple}$.
```



### 字体

 $\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}$

```latex
\mathbf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}
```

 $\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}$

```
\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}
```

 $\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}$

```
\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}
```

$\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}$

```
\mathsf{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}
```

 $\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}$

```
\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZabc123}
```



## 通过 Python 生成 LaTeX 表达式

step1：安装 latexify-py 模块

step2：编写代码

```python
import math
import latexify
@latexify.with_latex
def f(x,y,z):
    pass
	return result
print(f)
```

**step3：在输出区得到需要的 LaTeX 数学表达式**

**特别说明**，生成的表达式为**定义式**，即 ，如果只需要等式 ，可以把生成表达式中的 `\triangleq` 改成 `=` ！

更多细节和实例可以浏览我新的文章：

[点点星河：使用 Python 一键生成 LaTeX 数学公式zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/270596333)













[Typora 数学公式汇总（Markdown）]:https://zhuanlan.zhihu.com/p/261750408

[Markdown 语言 —— 数学公式]:https://zhuanlan.zhihu.com/p/138532124
[篇文章教会你如何在 Markdown 文档中插入数学公式]:https://zhuanlan.zhihu.com/p/158156773

[Markdown 中的常用 LaTex 数学公式]:https://zhuanlan.zhihu.com/p/95886235

