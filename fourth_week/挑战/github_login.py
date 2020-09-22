import scrapy


class GithubSpider(scrapy.Spider):
    name = 'github_login'

    start_urls = ['https://github.com/login']

    def parse(self, response):
        token = response.xpath('//form[@action="/session"]/input[1]/@value').extract_first()
        print("=" * 40)
        print('TOKEN:{}'.format(token))
        print("=" * 40)

        return scrapy.FormRequest.from_response(
                # 第一个参数为上次请求的响应对象，这是固定的写法
                response,
                # 将token字段和用户信息作为表单数据
                formdata = {
                    'authenticity_token': token,
                    'login': '账号',
                    'password': '密码'
                    },
                    callback = self.after_parse,
                )

    def after_parse(self, response):
           print('STATUS:', response.status)
           print('=' * 40)
