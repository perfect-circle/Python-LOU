# HTML和CSS      
      
**HTML，CSS，JavaScript 是 Web 开发的基础，任何一个网页都离不开 HTML, CSS。HTML 标签组构建了网页的基本框架，而 CSS 则使得网页布局更加合理美观。**      
      
## HTML5      
      
### 环境准备      
1.基本的html页面：      
```html      
<!DOCTYPE html>	# 指示了页面的文档类型是HTML5      
<html>      
<head>	# 定义头部信息，描述了这个网页的一些信息，比如标签，编码，引用的CSS等信息      
    <!-- 指定页面编码 -->      
    <meta charset="utf-8">      
    <!-- 指定页面 title，显示在浏览器上的信息 -->      
    <title>HTML5 学习</title>      
    <link rel="stylesheet" href="style.css">      
</head>      
<body>	# 定义文档的主体      
    <!-- 页面正式内容 -->      
    <nav> 导航条 </nav>      
    <div class="container"> 主体内容 </div>      
    <footer>      
        &copy; Copyright 2017 by <a href="http://www.shiyanlou.com/">shiyanlou</a>      
    </footer>      
</body>      
</html>      
```      
      
2. HTML 页面上的所有标签组成了一颗树，比如所有 <body> 标签内的标签都称为 <body> 标签的子元素，<body> 称为父元素。      
      
3. 标签经过浏览器渲染显示的时候，可以按默认显示类型分为两种，一种是在行内显示，类似于 <span> 标签，其他大部分的标签都直接显示成一行，比如 <div>, <p> 标签。标签可以包含各种属性，比如 <link> 标签的 href 属性指定了加载的 CSS 文件路径。<div> 标签的 class 属性指定了标签的类名。大部分标签都有 class 和 id 这两个属性，前者指定了标签的类名，后者指定了标签内的标识符，一个 HTML 文档内不能有相同的 id 属性。      
      
4. 一些常用的标签：      
      
| 标签 | 用途 |      
| :----: | :----: |      
| <div> | 最常用的标签，可以包含各种标签，页面布局最常用的标签 |      
| <a> |	定义连接 |      
| <br> | 插入换行符 |      
| <button> | 定义按钮 |      
| <dl> | 定义列表 |      
| <dt> | 定义列表项 |      
| <fieldset> | 定义表单控件组 |      
| <form> | 定义表单 |      
| <input> | 定义输入框 |      
| <ul> | 定义无序列表 |      
| <script> | 定义加载的 JavaScript |      
| <table> | 定义表格 |      
| <img> | 定义图片 |      
      
### 语义标签      
1. 所谓语义标签是指从标签名就可以看出标签的用途。比如在前面出现的 <nav> 标签，一看就知道应该实现导航栏功能。使用老版本实现页面时，大部分时候都是通过标签的 class 和 id 属性来指明标签的含义, 比如下图：      
      
![语义标签](https://doc.shiyanlou.com/md04171522012052410554136.gif/wm)       
      
2. 实现同样的功能使用语义标签会更加清晰简洁，一些常用的语义标签如下表：      
      
| 标签 | 描述 |      
| :----: | :----: |      
| <header> | 表示内容的头部信息，比如一个页面内容的头部； |      
| <footer> | 表示内容的尾部信息，可以包含作者，版权信息等内容。|      
| <nav> | 表示导航信息； |      
| <section> | 表示节，比如文档的一节内容； |      
| <article> | 表示文档内容的一个独立片段， 比如博客条目或报纸上的文章。 |      
| <aside> | 表示与页面其他部分略微相关的内容片段。 |      
      
### 表单      
1. 表单是网页中必不可少的组件，用户可以通过表单输入各种数据，然后通过提交表单，将输入的数据提交给网站后台。在 HTML 中，通过 <form> <input> 等标签实现。HTML5 表单的功能进一步加强，可以自定义表单能够接受的数据类型，比如邮箱输入框只能接受邮箱，如果输入非邮箱字符串则不能提交表单。      
```html      
<legend>表单实例</legend>      
<form action="" method="POST" id="form1">      
	<input type="text" autofocus="autofocus" required name="auto" placeholder="必填测试项">      
	<input type="email" name="mail" placeholder="请输入邮箱">      
	<input type="url" name="url" placeholder="请输入正确的网址">      
	<input type="password" name="password" placeholder="请输入密码">      
	<br>      
	<br>      
	<input type="submit" value="提交表单">      
</form>      
```      
      
2. 第一个输入框通过 required 属性指明了该输入框是必填项，autofocus表明为第一个输入框。；第二个输入框使用 type 属性设置了输入的内容必须是邮件样式的文本，第三个输入框设置了输入的文本必须是 URL 类型的，最后一个输入框为 password 类型，当用户输入内容时，将以星号显示。      
      
## CSS      
1. CSS 全名叫层叠样式表，可以用于控制标签如何显示。      
2. 在 HTML 页面中使用 CSS 样式有两种方式，一种是通过 <style> 标签直接将 CSS 代码写在页面中，比如下面的代码：      
```html      
<style>      
body {background-color: powderblue;}      
h1   {color: blue;}      
p    {color: red;}      
</style>      
```      
      
3. 另外一种方式是将 CSS 代码单独写入文件，比如前文中我们创建的 style.css 样式表，然后在 HTML 页面中通过 <link> 标签引用该文件，就像上文中 index.html 内容一样。      
      
### 基础语法      
1. CSS 规则由两个主要的部分构成：选择器，以及一个或多个属性值，如下：      
```css      
selector {      
    property1: value1;       
    property2: value2;      
    ...       
    propertyN: valueN;      
}      
```      
      
![图片](https://doc.shiyanlou.com/userid20407labid248time1423292345665/wm)       
      
2. 可以理解为，选择器选择 HTML 页面中相应的标签，然后应用括号中定义的各种属性。把下面的代码写入 style.css 中：      
```css      
h1 {      
   color:red;      
   font-size: 40px;      
}      
```      
      
3. 然后把下面代码写入 index.html 中的 <body> 标签内部：      
```html      
<h1> 实验楼 </h1>      
```      
      
4. HTML 子元素将从父元素继承属性。看看下面这条规则，通过 CSS 继承，子元素将继承最高级元素（在本例中是 body）所拥有的属性。所有子元素都显示成绿色：      
```css      
body {      
    color：green;      
}      
```      
      
### 选择器      
1. CSS 有多种选择 HTML 元素的方式，下面我们将一一讲解。      
      
* 派生选择器      
通过依据元素在其位置的上下文关系来定义样式，可以使标记更加简洁。派生选择器允许你根据文档的上下文关系来确定某个标签的样式。通过合理地使用派生选择器可以使 HTML 代码变得更加整洁。比方说，你希望列表标签 <li> 中的所有 <strong> 元素变为红色，而不是通常的黑色，可以这样定义一个派生选择器：      
      
[style.css]      
```css      
li strong{      
    color: red;      
}      
```      
      
[index.html]      
```html      
<p>      
    <strong>我是黑色，因为我不在列表当中，所以这个规则对我不起作用</strong>      
</p>      
<u1>      
    <li><strong>我是红色。这是因为 strong 元素位于 li 元素内。</strong></li>      
</u1>      
```      
      
* ID选择器      
ID 选择器可以选择设置了相同 ID 值的 HTML 元素，ID 选择器以 # 字符开始，比如：      
      
[style.css]      
```css      
#pid a{      
    color:#00755f;      
}      
```      
      
[index.html]      
```html      
<p id="pid">      
    hello css <a href="www.shiyanlou.com">shiyanlou</a>      
</p>      
```      
      
* 类选择器      
在学习 HTML 的时候，我们知道标签可以定义类 class 属性，CSS 就可以基于该属性值也就是类名进行选择。类选择器以 . 字符开始。如下：      
[style.css]      
```css      
.container {      
    color: red;      
}      
```      
      
[index.html]      
```html      
<div class="container">      
    container 容器      
</div>      
```      
      
* 属性选择器      
HTML标签可以设置各种属性，CSS可以利用这些属性进行选择标签。如下：      
[style.css]      
```css      
[title=foo] {      
	color: red:      
}      
```      
      
[index.html]      
```html      
<p title="foo">属性和值选择器</p>      
```      
      
### 常用元素      
1. CSS 有许多常用属性，比如设置元素的背景图片，颜色，设置字体大小等。 如下代码：      
```css      
.container {      
   color: red;      
   text-align: center;      
   font-size: 20px;      
   font-weight: 400;      
}      
```      
      
[CSS属性文档](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)       
      
### 框模型      
1. 一个 HTML 标签元素经过浏览器渲染显示在页面上后，最内部分是实际的内容，包含内容的是内边距。内边距呈现了元素的背景。内边距的边缘是边框，边框以外是外边距，外边距默认是透明的，因此不会遮挡任何元素。先让我们看下例子：      
[style.css]      
```css      
* {      
    margin: 0;      
    padding: 0;      
}      
      
.box {      
    width: 70px;      
    height: 30px;      
    margin: 60px;      
      
    border-style: solid;      
    border-width: 50px;      
      
    padding: 50px;      
}      
```      
      
** 上面的代码，先通过 * 选择器设置所有元素的外边距和内边距为 0。这是因为浏览器默认情况下会设置元素的内边距和外边距，为了不影响效果所以这里首先将其清零。接着设置了 .box 元素的宽度和高度，然后设置了内边距，边框和外边距。其中设置了边框为实线，宽度为 50px。px 是像素单位，表示一个像素的大小。设置内边距，边框和外边距不会影响元素内容的尺寸，但是会增加元素框的总尺寸。 **      
[index.html]      
```html      
<div class="box">      
	模型框      
</div>      
```      
      
![图片](https://doc.shiyanlou.com/document-uid5348labid2994timestamp1504277765641.png/wm)       
      
![图片](https://doc.shiyanlou.com/document-uid5348labid2994timestamp1504277765641.png/wm)       
      
[CSS参考手册](https://css.doyoe.com/)       
