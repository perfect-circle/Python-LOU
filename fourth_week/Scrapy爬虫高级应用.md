# 简介          
1. 知识点          
          
* 页面追随          
* 图片下载          
* Item 包含多个页面数据          
* 模拟登录          
          
## 页面跟随          
1. 在前面实现课程爬虫和用户爬虫中，因为实验楼的课程和用户 URL 都是通过 id 来构造的，所以可以轻松构造一批顺序的 URLS 给爬虫。但是在很多网站中，URL 并不是轻松可以构造的，更常用的方法是从一个或者多个链接（start_urls）爬取页面后，再从页面中解析需要的链接继续爬取，不断循环。          
          
2. 例子          
```python          
import scrapy          
          
class CoursesFollowSpider(scrapy.Spider):          
	name = 'courses_follow'          
	start_urls = ['https://www.lanqiao.cn/courses/63']          
          
	def parse(self, response):          
		yield {          
			'name': response.css('h1.course-title::text').extract_first().strip(),          
			'author': response.css('p.teacher-info span::text').extract_first()          
			}          
          
		for url in response.css('div.course-item-box a::attr(href)'):          
			yield response.follow(url, callback=self.parse)          
```          
          
## 图片下载          
          
1. scrapy 内部内置了下载图片的 pipeline。下面以下载实验楼课程首页每个课程的封面图片为例展示怎么使用它。          
          
2. 首先需要在item.py中定义一个item，他包括两个必要的字段：          
          
[item.py]          
```python          
import scrapy          
          
class CourseImageItem(scrapy.Item):          
    # 要下载的图片 url 列表          
    image_urls = scrapy.Field()          
    # 下载的图片会先放在这里          
    images = scrapy.Field()          
```          
          
3. 运行 scrapy genspider courses_image shiyanlou.com/courses 生成一个爬虫，爬虫的核心工作就是解析所有图片的链接到 CourseImageItem 的 image_urls 中。          
[spider/courses_image]          
```python          
import scrapy          
          
from shiyanlou.items import CourseImageItem          
          
class CoursesImageSpider(scrapy.Spider):          
	name = 'courses_image'          
	start_urls = ['https://www.lanqiao.cn/courses/']          
          
	def parse(self, response):          
		item = CourseImageItem()          
		# 解析图片链接到item          
		item['image_urls'] = response.xpath(          
			'//img[@class="cover-image"]/@src'          
			).extract()          
		yield item          
```          
          
4. 代码完成后需要在 settings.py 中启动 scrapy 内置的图片下载 pipeline，因为 ITEM_PIPELINES 里的 pipelines 会按顺序作用在每个 item 上，而我们不需要 ShiyanlouPipeline 作用在图片 item 上，所以要把它注释掉：          
[settings.py]          
```python          
ITEM_PIPELINES = {          
    'scrapy.pipelines.images.ImagesPipeline': 100,          
    # 'shiyanlou.pipelines.ShiyanlouPipeline': 300          
}          
          
IMAGES_STORE = "images'		# 配置图片存储目录          
          
IMAGES_THUMBS = {		# 配置图片大小          
	'small': (50, 50)          
}          
```          
          
5. 运行程序          
```shell          
pip3 install pillow          
scrapy crawl courses_image          
```          
          
## 组成item的数据在多个页面          
1. 在前面几节实现的爬虫中，组成 item 的数据全部都是在一个页面中获取的。但是在实际的爬虫项目中，经常需要从不同的页面抓取数据组成一个 item。下面通过一个例子展示如何处理这种情况。          
          
有一个需求，爬取实验楼课程首页所有课程的名称、封面图片链接和课程作者。课程名称和封面图片链接在课程主页 https://www.shiyanlou.cn/courses/ 就能爬到，课程作者只有点击课程，进入课程详情页面才能看到，怎么办呢？          
          
scrapy 的解决方案是多级 request 与 parse 。简单地说就是先请求课程首页，在回调函数 parse 中解析出课程名称和课程图片链接，然后在 parse 函数中再构造一个请求到课程详情页面，在处理课程详情页的回调函数中解析出课程作者。          
          
2. 首先在items.py中创建相应的Item类：          
```python          
class MultipageCourseItem(scrapy.Item):          
    name = scrapy.Field()          
    image = scrapy.Field()          
    author = scrapy.Field()          
```          
          
3. 创建爬虫          
```shell          
scrapy genspider multipage www.lanqiao.cn          
```          
          
4. 解析内容：          
```python          
import scrapy          
          
from shiyanlou.items import MultipageCourseItem          
          
          
class MultipageSpider(scrapy.Spider):          
    name = 'multipage'          
    start_urls = ['https://www.lanqiao.cn/courses/']          
          
    def parse(self, response):          
        for course in response.css('div.col-md-3'):          
            item = MultipageCourseItem(          
                # 解析课程名称          
                name=course.css('h6.course-name::text').extract_first().strip(),          
                # 解析课程图片          
                image=course.css('img.cover-image::attr(src)').extract_first()          
            )          
            # 构造课程详情页面的链接，爬取到的链接是相对链接，调用 urljoin 方法构造全链接          
            course_url = course.css('a::attr(href)').extract_first()          
            full_course_url = response.urljoin(course_url)          
            # 构造到课程详情页的请求，指定回调函数          
            request = scrapy.Request(full_course_url, self.parse_author)          
            # 将未完成的 item 通过 meta 传入 parse_author          
            request.meta['item'] = item          
            yield request          
          
    def parse_author(self, response):          
        # 获取未完成的 item          
        item = response.meta['item']          
        # 解析课程作者          
        item['author'] = response.css('p.teacher-info span::text').extract_first()          
        # item 构造完成，生成          
        yield item          
```          
          
## 模拟登录          
1. 有些网页需要登录后才能访问，例如任何网站的用户个人主页。有些网页中的部分内容需要登录后才能看到，例如 GitHub 中的私有仓库          
          
2. 在登录界面的POST请求中，Form Data中需要的数据有authticity_token, login, password。           
          
3. token 字段是关键信息，为了防止跨域伪造攻击，网站通常会在表单中添加一个隐藏域来放置这个 token 字段。当浏览器发送携带表单的 POST 请求时，服务器收到请求后会比对表单中的 token 字段与 Cookies 中的信息以判断请求来源的可靠性。          
          
4. 获取token，在登录界面中打开开发者工具-打开源码-搜索token，制作爬虫：          
```python          
import scrapy          
          
          
class GithubSpider(scrapy.Spider):          
    name = 'github_login'          
    start_urls = ['https://github.com/login']          
          
    def parse(self, response):          
        token = response.xpath('//form/input[1]/@value').extract_first()          
        print('==================================')          
        print('TOKEN:', token)          
        print('==================================')          
```          
          
5. 在执行 scrapy runspider 命令时，可以使用 -L 选项设置打印信息的级别。为了避免多余的普通信息出现在屏幕上，我们设置打印级别为 ERROR ，也就是只打印错误信息。          
```shell          
scrapy runspider -L ERROR github_login.py          
```          
          
6. 模拟登录          
```python          
import scrapy          
          
          
class GithubSpider(scrapy.Spider):          
    name = 'github_login'          
    start_urls = ['https://github.com/login']          
          
    def parse(self, response):          
        # 获取 token 字段          
        token = response.xpath('//form/input[1]/@value').extract_first()          
        print('==================================')          
        print('TOKEN:', token)          
        print('==================================')          
        # 构造 POST 登录请求          
        return scrapy.FormRequest.from_response(          
                # 第一个参数为上次请求的响应对象，这是固定写法          
                response,          
                # 将 token 字段和用户信息作为表单数据          
                formdata = {          
                    'authenticity_token': token,          
                    'login': '用户名',          
                    'password': '密码'          
                },          
                callback = self.after_parse,          
        )          
          
    def after_parse(self, response):          
        print('STATUS:', response.status)          
        print('==================================')          
```          
