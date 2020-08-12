# Scrapy介绍          
1. Scrapy 是使用 Python 实现的一个开源爬虫框架。秉承着 “Don’t Repeat Yourself” 的原则，Scrapy 提供了一套编写爬虫的基础框架和编写过程中常见问题的一些解决方案。Scrapy 主要拥有下面这些功能和特点：          
* 内置数据提取器（Selector），支持XPath 和 Scrapy 自己的 CSS Selector 语法，并且支持正则表达式，方便从网页提取信息。          
* 交互式的命令行工具，方便测试 Selector 和 debugging 爬虫。          
* 支持将数据导出为 JSON，CSV，XML 格式。          
* 内置了很多拓展和中间件用于处理：          
* 可扩展性强，可以运行自己编写的特定功能的插件          
          
2. 除了列出的这些，还有很多小功能，比如内置的文件、图片下载器等等。另外，Scrapy 基于 twisted 这个高性能的事件驱动网络引擎框架，也就是说，Scrapy 爬虫拥有很高的性能。          
   
3. Scrapy 是一个非常容易上手的成熟的爬虫框架，为了帮助大家梳理架构细节和常用命令，我们整理了一份脑图包含了 Scrapy 爬虫框架的基础知识。这份脑图大家可以在本周每个实验中都能去进行对照学习，让动手实践过程中学习到的知识点建立更加清晰的体系。          
[Scrapy爬虫基础知识脑图](http://naotu.baidu.com/file/dd56a350fe7be1d871103ffea6d4ea54?token=dbdf171ff27dee77)           
          
   
   [Scrapy官方文档](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)           
             

## 实验准备          
1. 建立虚拟环境，并下载scrapy库。          
```shell          
virtualenv env          
pip3 install scrapy          
```

## 数据提取器          
1. 在开始编写爬虫前，我们先来学习一下 Scrapy 的数据提取器（Selector），因为爬虫的本质就是为了获取数据，所以在编写爬虫的过程中需要编写很多数据提取的代码。          
   
2. Scrapy 内置两种数据提取语法： CSS 和 XPath 。下面通过例子来看看怎么使用，有这样一个 HTML 文件：          
```html          
<html>          
 <head>          
  <base href='http://example.com/' />          
  <title>Example website</title>          
 </head>          
 <body>          
  <div id='images'>          
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>          
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>          
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>          
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>          
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>          
  </div>          
 </body>          
</html>          
```

这是 scrapy 官方提供的一个网页，方便我们练习 Selector，它的地址是：http://labfile.oss.aliyuncs.com/courses/923/selectors-sample1.html          
          
3. Scrapy 提供了一个交互式的 Python 解释器环境方便我们测试和 DEBUG ，使用方法是：          
```shell           
scrapy shell http://labfile.oss.aliyuncs.com/courses/923/selectors-sample1.html          
```

### CSS Selector          
1. 顾名思义，css selector 就是 css 的语法来定位标签。例如要提取例子网页中 ID 为 images 的 div 下所有 a 标签的文本，使用 css 语法可以这样写：          
```python          
response.css('div#images a::text').extract()          
```

2. 网页的 HTML 源码是由各种各样不同的标签组成，一个标签可以有很多属性，每个属性可以有很多属性值，属性值在源码中表现为由空格分隔的字符串，例如：<a class="one two three" href="front.index">首页</a> , 这是一个完整的标签，标签名为 a ，它有两个属性 class 和 href，其中 class 属性有三个属性值：one、two、three，class 又称为类属性，“首页” 二字就是标签的 text 值，也叫做标签文本。          
   
3. 在 CSS 提取器中，div#images 表示 id 属性的值为 images 的 div 标签，如果是类属性的值为 images，这里就写成 div.images。div a 表示 div 标签下所有的 a 标签，::text 表示提取文本，extract 方法执行提取操作，返回一个列表。如果只想要列表中第一个 a 标签下的文本，可以使用 extract_first 方法：          
   
4. extract_first() 方法支持对没有匹配到的元素提供一个默认值，div#images 下面并没有 p 标签，所以会返回提供的默认值。如果不提供 default 值的话会返回 None。：          
```python          
>>> response.css('div#images p::text').extract_first(default='默认值')          
'默认值'          
```

5. 如果要提取所有 a 标签的 href 链接，可以这样写：          
```python          
>>> response.css('div#images a::attr(href)').extract()          
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']          
```
6. 如果 div 标签中的 class 属性有多个属性值，用 css 提取器可以写为 div[class="r1 r2 r3"] 或者 div.r1.r2.r3          
          
### XPath          
1. XPath (XML Path Language) 是一门路径提取语言，最初被设计用来从 XML 文档中提取部分信息，现在它的这套提取方法也可以用于 HTML 文档上。          
   
2. 假设有下面这样一份 HTML 文档，它列出了一些世界知名的 IT 公司及其相关信息，将这份文档保存为 example.html。          
          
```html          
<!DOCTYPE html>          
<html>          
<head>          
  <title>xpath</title>          
</head>          
<body>          
  <div class="companies">          
    <div class="company">          
      <h2>阿里巴巴</h2>          
      <a href="alibaba.com"><img src="alibaba.jpg"></a>          
      <p class="location">杭州</p>          
    </div>          
    <div class="company">          
      <h2>腾讯</h2>          
      <a href="qq.com"><img src="qq.jpg"></a>          
      <p class="location">深圳</p>          
    </div>          
    <div class="company">          
      <h2>Facebook</h2>          
      <a href="facebook.com"><img src="facebook.jpg"></a>          
      <p class="location">硅谷</p>          
    </div>          
    <div class="company">          
      <h2>微软</h2>          
      <a href="microsoft.com"><img src="microsoft.jpg"></a>          
      <p class="location">西雅图</p>          
    </div>          
  </div>          
</body>          
</html>          
```

3. 什么是节点          
在使用 xpath 前，大家首先要把几个概念弄明白。首先，什么是 节点(node)，以上面的文档为例子，每个标签都是一个节点：          
```html          
<div class="company">          
  <h2>腾讯</h2>          
    <img src="tencent.jpg">          
  <p class="location">深圳</p>          
</div>          
```

**这里最外层的 div 是整个文档的一个子节点，里面包含的公司信息标签都是 div 的子节点，节点标签之间的内容称为这个节点的文本(text)，如 腾讯 是 h2 标签的文本。节点标签内部称为节点的属性(attribute)，如 src 是 img 标签的一个属性，每个标签都可以有 class 属性。每个属性都有一个或多个对应的值（class 属性可以有多个值）。那么爬虫的主要目的其实就是从一个文档中获取需要的文本或者属性的值。**       
          

4. 节点的选择规则：          
| 表达式 | 描述 |
| :----: | :----: |
| nodename | 选取此节点的所有子节点。 |
| / | 从根节点选取。 |
| // | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。 |
| .  | 选取当前节点。 |
| .. | 选取当前节点的父节点。 |

5. 将 example.html 文档手动构建成 response 对象，然后就可以在 response 对象上直接使用 xpath 方法了：          
```python          
>>> from scrapy.http import HtmlResponse          
# body 的数据类型是字符串          
>>> body = open('example.html').read()            
# HtmlResponse 接收两个参数，url 为自定义的网址          
# body 参数的值应为字节码，所以需要使用字符串的 encode 方法进行编码          
>>> response = HtmlResponse(url='http://example.com', body=body.encode('utf-8'))          
```

6. / 表示从根节点开始选取，比如，你想要选取 title 节点，就需要按标签的阶级关系来定位：          
```python          
>>> response.xpath('/html/head/title').extract()          
['<title>xpath</title>']          
```

7. 而使用 // 就可以不必管标签在文档中的位置：          
```python          
>>> response.xpath('//title').extract()          
['<title>xpath</title>']          
>>> response.xpath('//h2').extract()          
```


8. 同 CSS 提取器的方法类似，extract 会返回一个列表，比如我们选取所有公司的名称所在的 h2 标签：          
```python          
>>> response.xpath("//h2").extract()          
["<h2>阿里巴巴</h2>", "<h2>腾讯</h2>", "<h2>Facebook</h2>", "<h2>微软</h2>"]          
```

9. 可以在选择表达式后面加上 text() 来指定只返回文本：          
```python          
>>> response.xpath('//h2/text()').extract()          
['阿里巴巴', '腾讯', 'Facebook', '微软']          
```

10. 而如果想要选取属性值，在属性名称前面加上 @ 符号就可以了，比如我们选取所有 img 的 src 属性：          
```python          
>>> response.xpath('//img/@src').extract()          
['alibaba.jpg', 'qq.jpg', 'facebook.jpg', 'microsoft.jpg']          
```

11. 我们同样可以用属性来定位节点，比如我们要选取所有 class 属性值为 location 的 p内的文本：          
```python          
>>> response.xpath('//p[@class="location"]/text()').extract()          
['杭州', '深圳', '硅谷', '西雅图']          
```

12. 在节点名称后面加上 [n] ，n 是一个数字，这样可以获取到该节点下某个子节点的第 n 个，比如我们要获取 div.companies 下的第二个 div 子 节点，也就是腾讯所在的 div 节点，那么可以这样写：          
```python          
>>> response.xpath("//div[@class='companies']/div[2]")          
[<Selector xpath="//div[@class='companies']/div[2]" data='<div class="company">\n      <h2>腾讯</h2>\n'>]          
```

13. scrapy 中，对 xpath 方法选取到的对象可以进一步运用 xpath 方法，比如上一步中，我们获取到了腾讯所在的 div 标签，现在我们想在当前结果基础上进一步获取公司的网址，你可能会写出这样的代码：          
```python          
>>> response.xpath('//div[@class="companies"]/div[2]').xpath('//a/@href').extract()          
['alibaba.com', 'qq.com', 'facebook.com', 'microsoft.com']          
```

14. 这时候你发现返回的其实是所有 a 标签的 href，这是因为 // 是基于整个文档来选择的，如果想要基于当前已经选择了的部分运用 xpath 方法，则要在 // 前面加上 . 号：          
```python          
>>> response.xpath('//div[@class="companies"]/div[3]').xpath('.//a/@href').extract()          
['facebook.com']          
```

15. 前面我们说到过，一个标签的属性值可以存在多个，比如 <div class=“name1 name2 name3”>hello</div>，这种情况下进行定位的时候，把所有类名都写上就比较麻烦。这时候可以选取一个能唯一代表该 div 的类名，假设我们选了 name2，然后可以使用 contains(@attr, "value") 方法，该方法表示，只要标签的属性包含指定的值就可以：          
```python          
>>> response.xpath('//div[contains(@class, "name2")]/text()').extract()           
['hello']          
```

### re和re_first方法          
1. 除了 extract() 和 extract_first()方法， 还有 re() 和 re_first() 方法可以用于 css() 或者 xpath() 方法返回的对象。          
   
2. 使用 extract() 直接提取的内容可能并不符合格式要求，比如上面的 CSS 提取器例子中，获取的第一个 a 标签的 text 是这样的：Name: My image 1 ，现在要求不要开头的 Name: 和结尾的空格，这时候就可以使用 re() 替代 extract 方法，使用正则表达式对提取的内容做进一步的处理：          
```python          
>>> response.css('div#images a::text').re('Name: (.+) ')          
['My image 1', 'My image 2', 'My image 3', 'My image 4', 'My image 5']          
```

re() 方法中定义的正则表达式会作用到每个提取到的文本中，只保留正则表达式中的子模式匹配到的内容，也就是 () 内的匹配内容。          
          
### Scrapy爬取实验楼课程信息          
```python          
# -*- coding: utf-8 -*-          
           
import scrapy          
          
class ShiyanlouCoursesSpider(scrapy.Spider):          
    name = 'shiyanlou'          
          
    def start_requests(self):          
        url_list = [          
                'https://www.lanqiao.cn/courses',          
                'https://www.lanqiao.cn/courses/?page=2',          
                'https://www.lanqiao.cn/courses?page=3'          
                ]          
        for url in url_list:          
            yield scrapy.Request(url=url```allback=self.parse)          
          
    def parse(self,response):          
	# 循环class类为"col-sm-12 col-md-3"属性的div标签
        for course in response.xpath('//div[@class="col-sm-12 col-md-3"]'):          
            yield {          
                    'name': course.xpath(          
                        './/h6[@class="course-name"]/text()'          
                        ).extract_first().strip(),          
                    'description': course.xpath(          
                    './/div[@class="course-description"]/text()'          
                    ).extract_first().strip(),          
                    'type': course.xpath(          
                    './/span[contains(@class,"course-type")]/text()'          
                    ).extract_first('免费').strip(),          
                    'stuents': course.xpath(          
                    './/span[@class="students-count"]/span/text()'          
                    ).extract_first().strip()          
                    }          
```
