# 简介
1. Jinja2 是一个Python 软件包，实现了 HTML 模板语言。网页的渲染方式一般有两种，一种是后端渲染，一种是前端渲染。后端渲染时，一般都是通过 HTML 模板进行的，模板中可能包含若干逻辑，比如继承自其它基础模板。这些模板逻辑，继承功能都需要模板语言的支持，而 Jinja2 正是这样的一种语言。有了 Jinja2 以后，HTML 模板的编写将变得非常简单。
2. 知识点：
* Jinja语法
* Jinja基础
* Jinja模板
* Jinja过滤器

## Jinja语法
1. 创建了 templates 目录，Flask 默认已经整合了 Jinja, 会自动从 templates 目录加载相应的模板。接着在 app.py 中输入代码：
```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():

    teacher = {
        'name': 'Aiden',
        'email': 'luojin@simplecloud.cn'
    }

    course = {
        'name': 'Python Basic',
        'teacher': teacher,
        'user_count': 5348,
        'price': 199.0,
        'lab': None,
        'is_private': False,
        'is_member_course': True,
        'tags': ['python', 'big data', 'Linux']
    }
    return render_template('index.html', course=course)
```

2. 上面的代码中，创建了一个 Flask 应用，需要注意的是我们设置了 app.config['TEMPLATES_AUTO_RELOAD'] = True, 这使得每当模板发生改变时，会自动重新渲染模板。接着创建了 index 视图函数，其中定义了 course 字典，代表一门课程。该视图函数会渲染 index.html 模板，该模板位于app.py文件下的同级目录templates下的index.html。

## Jinja基础
1. Jinja2 的语法中，使用一些特殊字符包含需要解析执行的代码，没有被这些特殊字符包含的代码则不进行解析处理。主要包括以下几种特殊字符 (... 字符代表省略的需要执行的代码)：
* {% ... %} 包含的代码是可以被执行的语句，比如循环语句，继承语法。
* {{ ... }} 包含的是Python对象，用于解析出这些对象的值，经常用于打印内容。
* {# ... #} 用于添加注释，这些注释不会被处理，但是也不会输出到HTML源码中。

### 变量
1. 在 Jinja2 中，变量可以通过 {{ variable }} 的形式显示，可以通过 . 访问变量的属性，如果传递给模板的变量是一个字典，也可以通过 . 访问字典的字段。在前文中，我们创建的 app.py 文件中，已经将一个 course 对象传递给了 index.html 模板，现在将 index.html 模板修改成以下内容，重新刷新浏览器就可以看到 course 的各种属性了：
```html
<p> name: {{ course.name }}</p>
<p> user count: {{ course.user_count }}</p>
<p> teacher: {{course.teacher }} </p>
<p> is_private: {{ course.is_private }} </p>
<p> not exist: {{ course.not_exist }} </p>
```

2. 还可以发现，如果访问一个不存在的属性，则会简单的返回空值，不会发生异常，这与在 Python 代码中访问不存在的属性是不一样的。

3. Jinja2 也支持赋值操作，有的时候执行方法可能消耗很多资源，这个时候可以将执行结果通过 set 关键字赋值给 Jinja2 变量，在后续的所有访问中，都通过该变量访问，如下代码：
```python
{% set result = ['one', 'two', 'hello', 'shiyanlou'] %}
{% for n in result %}
  <p>{{ n }}</p>
{% endfor %}
```

### 逻辑比较
1. Jinja 中的逻辑比较可以通过 if 语句，如下代码：
```python
{% if course.is_private %}
    <p> course {{course.name}} is private </p>
{% elif course.is_member_course %}
    <p> course {{course.name}} is member course </p>
{% else %}
    <p> course {{course.name}} is normal course </p>
{% endif %}
```

### 循环
1.在 Jinja 中循环主要通过 for 语句完成，语法如下：
```python
{% for tag in course.tags %}
    <span> {{ tag }} </span>
{% endfor %}
```

### 宏
1.在 Python 中可以定义各种函数，同样的在 Jinja2 中，可以定义宏，相当于 Python 中的函数。可以将常用的 HTML 代码写成一个宏，这样在任何地方调用宏就可以生成同样的 HTML 代码，提高了代码复用度。宏通过 macro 关键字进行定义。比如可以将渲染一门课程信息的代码写成一个宏:
```python
{% macro course_item(course, type="bootstrap") %}
    <div>
        <p> type: {{ type }} </p>
        <p> name: {{ course.name }}</p>
        <p> user count: {{ course.user_count }}</p>
        <p> teacher: {{course.teacher }} </p>
        <p> is_private: {{ course.is_private }} </p>
    </div>
{% endmacro %}

<div> {{ course_item(course) }} </div>
<p>{{ '=' * 20 }}</p>
<div> {{ course_item(course, type="louplus") }} </div>
```

2. course_item()相当于一个函数，括号里的为他的参数。

### 模板
1. 上文中定义的宏有可能需要被其他模板引用，好在 Jinja2 也支持模块功能。首先我们在 /home/shiyanlou/Code/templates 目录中创建 macro.html 文件，然后将上文中定义 course_item 宏的代码写入该文件。然后就可以在 index.html 中通过 import 关键字导入宏了，如下代码：
```python
{% from 'macro.html' import course_item %}
<div> {{ course_item(course) }} </div>
```

### 模板继承
1. Jinja2 同样支持模板间的继承。网页中，很多组件是共用的，比如网页的标题栏和尾部，通过继承功能可以很方便的共用组件。继承功能通过 extends, block 等关键字实现。首先在templates 目录中创建 base.html 模板，然后写入以下代码：
[base.html]
```python
<body>
    <div> 
        {% block header %}
            <p> this is header </p>
        {% endblock %}
    </div>
    <div>{% block content %}{% endblock %}</div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2017 by <a href="http://www.shiyanlou.com/">shiyalou</a>.
        {% endblock %}
    </div>
</body>
```

2. 上面的代码中，通过 block 定义了 header, content, footer 三个块，可以被其他模板重写，如果未被其他模板重写则显示默认内容。在 index.html 中输入以下代码：
[index.html]
```python
{% extends "base.html" %}
{% from 'macro.html' import course_item %}

{% block header %}
    <h1> header </h1>
{% endblock %}

{% block content %}
    {{ course_item(course) }}
{% endblock %}
```

3. 上面的代码中，首先通过 extends 关键字告诉 Jinja2 模板从 base.html 继承而来，接着使用 import 关键字从上一节实验中定义的 macro.html 导入了宏 course_item。接着使用 block 关键字覆盖了 base.html 模板中定义的 header, content 块，而 footer 块将显示默认内容。刷新浏览器，效果如下图：

![图片](https://doc.shiyanlou.com/document-uid5348labid2994timestamp1504177402133.png/wm)

## 过滤器
1. Jinja2 中还支持过滤器，过滤器通过 | 方式执行，比如 {{ var | abs }}, 通过 abs 过滤器对 var 求绝对值。 Jinja2 有很多内置的过滤器，比如:

* abs 求绝对值；
* capitalize 将字符串首字母变成大写，其他转换为小写；
* first 获取列表的第一个元素；
* int 转换为整数；
* length 求列表的长度；

2. Jinja2 也支持自定义过滤器，通过 Flask 添加过滤器非常简单，修改 app.py 为如下代码：
[app.py]
```python
# -*- coding:utf-8 -*-

from flask import Flask, render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

def hidden_email(email):
    parts = email.split('@')
    parts[0] = '*****'
    return '@'.join(parts)

app.add_template_filter(hidden_email)

@app.route('/')
def index():

    teacher = {
        'name': 'Aiden',
        'email': 'luojin@simplecloud.cn'
    }

    course = {
        'name': 'Python Basic',
        'teacher': teacher,
        'user_count': 5348,
        'price': 199.0,
        'lab': None,
        'is_private': False,
        'is_member_course': True,
        'tags': ['python', 'big data', 'Linux']
    }
    return render_template('index.html', course=course)

```

2. 以上代码，通过 app.add_template_filter 方法注册了 hidden_email 过滤器，该过滤器隐藏邮箱前缀。接着在 index.html 文件中输入下面的代码：
[index.html]
```python
{% extends "base.html" %}
{% from 'macro.html' import course_item %}

{% block content %} 
    <p> teacher email: {{ course.teacher.email | hidden_email }}</p>
    <p> course tag length: {{ course.tags | length }} </p>
{% endblock %}
```

3. 刷新浏览器，效果如下：

![图片](https://doc.shiyanlou.com/document-uid5348labid2994timestamp1504178638315.png/wm) 

### url_for
1. url_for也可以在 Jinja 中使用，使用方法与 Flask 中相同，但需要在前后增加两个大括号才能在 Jinja 中解析成正确的 URL 地址：
```python
{{ url_for('user_index', username='testuser') }}
```

2. 此外，还有一个常用的 static 目录的用法，开发一个 Web 应用的时候需要将一些图片、js、css 等文件放到一个统一的 static 目录，Jinja2 中默认的 static 目录是和 templates 目录同一层次的目录。只要将图片、js、css 等文件放到这个 static 目录下就可以使用这种方法获得文件的 URL 地址了。获取这些文件的地址的方式可以用下面的方式：
```python
{{ url_for('static', filename='css/style.css') }}
```

## 扩展阅读
[Jinja2官方文档](http://docs.jinkan.org/docs/jinja2/) 
