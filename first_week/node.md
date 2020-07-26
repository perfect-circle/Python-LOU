## 字符串常见的属性和方法            
```python            
str = '   shiyanlou   '            
str.strip()	# 去掉两边空格            
str.split()	# 将字符串变为列表，默认以空格为分割符号            
str.split(':')	# 以冒号为分割符            
str.__len__()	# 相当于len(str)            
```            
            
## format格式化字符串            
```python            
'{} {}'.format('hello','world')		# 将参数依次填入字符串中            
```            
'hello world'            
            
```python            
'{1} {0} {1}'.format('hello','shiyanlou')            
```            
'shiyanlou hello shiyanlou'            
            
```python            
'元周率:{:.2f}'.format(3.1415926)            
```            
'元周率：3.14'            
            
```python            
'网站：{name},地址：{url}'.format(name='shiyanlou',url='www.shiyanlou.com')            
```            
'网站：实验楼，地址：www.shiyanlou.com'            
            
## 注释            
1. 注释在被注释的代码的上面或则左面。            
2. #!/usr/bin/env python3必须放在文件的第一行，\            
必须以#!开头，它的作用是告诉系统可以到 /usr/bin/env 目录下寻找 python3 的解释器。凡是在文件中添加了这一句，\            
然后使用chmod a+x xxx.py给文件赋予可执行权限，那么就可以使用命令./xxx.py运行该文件。            
3. -*- coding:utf-8 -*-一般都放在文件的第二行，当文件中出现中文的时候就必须使用它，它是告诉 Python 解释器文件的编码格式应该使用 utf-8。            
            
# 算数运算            
| 运算符 | 名称 | 描述 |            
| :----: | :----: | :----: |            
| + | 加 | 两个对象相加 |            
| - | 减 | 得到负数或是一个数减去另一个数 |            
| * | 乘 | 两个数相乘或是返回一个被重复若干次的字符串 |            
| / | 除 | x 除以 y |            
| % | 取模 | 返回除法的余数 |            
| ** | 幂 | 返回 x 的 y 次幂 |            
| // | 取整除 |	返回商的整数部分（向下取整）|            
            
## 逻辑运算符            
| 运算符 | 逻辑表达式 | 描述 |            
| :----: | :----: | :----: |            
| and |	x and y | 布尔 "与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值 |            
| or | x or y |	布尔 "或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值 |            
| not |	not x |	布尔 "非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True |            
            
## 身份运算符            
            
1. id : 在 Python 语言中，一切皆对象。当我们创建一个 Python 对象，就会在内存中分配一段内存用来存储这个对象，这段内存会有一个十进制的编号，id 方法就用来获得这个内存地址的编号，举例如下：            
![例子](https://www.shiyanlou.com/courses/2554/learning/?id=42188)            
            
身份运算符就是用来判断两个变量所指向的对象是否存储在同一个内存单元中：            
| 运算符 | 描述 | 实例 |            
| :----: | :----: | :----: |            
| is | is 是判断两个标识符是不是引用自一个对象 | x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False |            
| is not | is not 是判断两个标识符是不是引用自不同对象 | x is not y ，类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False |            
            
>>> a = 'hello'            
>>> a is not 'hellllo'            
True            
>>> a is 'hello'            
True            
>>> c = 33            
>>> d = 33            
>>> c is d            
True            
>>> c is not d            
False            
>>> c is not a            
True            
            
## 条件判断            
1. 在布尔表达式中，会被 Python 解释器判断为”假“的有：False、None、0、”“、()、[]、{}            
2. 在程序开发过程中，当遇到一些代码暂时不写(等到后面写)又不想程序在执行的时候报错就可以使用 pass 关键字，程序执行遇到 pass 就会跳过这里的代码块继续执行后面的代码：            
>>> a = 3            
>>> if a<1:            
...     print("a<1")            
... else:            
...     pass            
...            
>>> #程序没有报错            
            
## 终端运行Python程序            
1. sys模块的sys.argv：获取脚本参数,sys.argv[0]为运行的程序文件，sys.argv[1]为运行程序的第一个参数。            
```python            
#!/usr/bin/env python3            
print('此时 __name__的值是：{}'.format(__name__))            
```            
            
![本地执行](https://doc.shiyanlou.com/document-uid13labid9150timestamp1543373053933.png/wm)             
            
```python            
import namefile.py            
```            
            
![引用模块](https://doc.shiyanlou.com/document-uid13labid9150timestamp1543373054145.png/wm)             
            
2. 通常情况下，一个 xxx.py 文件只有两种使用情况，要么是使用 python3 xxx.py 的方式被单独执行，要么是使用 import xxx 的方式被其它文件当作一个模块所引用。而且以模块的方式导入存在一个问题，被导入的模块中的代码会自上而下依次运行（参考上面的那张图），有的时候我们不想文件中的某些代码在导入的时候被执行，怎么办呢？            
            
这个时候 __name__的这个重要特性就发挥用场了，可以在文件中单独加一个判断进行控制， 当__name__ == '__main__'时才执行特定的代码。            
            
现在修改 courses.py 文件中的代码如下：            
```python            
#!/usr/bin/env python3            
            
print('此时 __name__ 的值是：{}'.format(__name__))            
            
if __name__ == '__main__':              
    print("shiyanlou has many courses.")  # 当以单独的文件运行时才打印            
```            
![运行结果](https://doc.shiyanlou.com/document-uid13labid9150timestamp1543373054355.png/wm)             
            
```python            
#!/usr/bin/env python3            
            
import courses            
print("this is louplus.py file")            
```            
            
![运行结果](https://doc.shiyanlou.com/document-uid13labid9150timestamp1543373054622.png/wm)             
            
## 引入模块            
1. 推荐引入顺序:在当前代码中引入模块，推荐的引入顺序为：标准库 > 第三方 > 自定义。也就是说：优先引用 Python 内置的模块，如果内置的模块没有需要的功能，再去查看第三方是否有现成的模块可以引用，如果依然没有才自定义模块进行使用。这样做主要是为了节省开发时间以及提高性能。            
2. 搜索模块路径：Python 中存在一个默认的模块搜索路径。在当前代码文件中导入一个模块时，Python 解释器先在当前包中查找模块，如果找不到就会在内置模块中查找，如果依然找不到就会按 sys.path 给定的路径查找对应的模块文件。sys.path 包括当前目录及系统中的一些 Python 模块的主要安装目录，可以通过下面的方法查看搜索路径：            
```python            
import sys            
sys.path            
```            
            
![运行结果](https://doc.shiyanlou.com/document-uid13labid9150timestamp1543373051066.png/wm)             
            
3. 包：包是一个文件夹，在其中可以定义多个模块或是多个子包。通常 Python 的第三方工具或是应用都是以包的形式发布的。在 Python 中文件夹可以被识别成一个包，前提是这个文件夹中有一个 __init__.py（注意 init 前后都是两个下划线）文件（注意从 Python3.3 之后不再需要这个文件了），文件中可以不用写任何内容。（从 Python3.3 开始，就不再需要目录下必须有 __init__.py 文件了）。            
4. 如果想要在/home/shiyanlou/Code目录下引入 courses 模块就可以用 import shiyanlou.courses 这种代码来引入，前提是 shiyanlou 目录已经放到了 Python 模块搜索的默认路径下了，可以通过sys.path.append(yourModulePath)。            
![引入包](https://doc.shiyanlou.com/document-uid13labid9150timestamp1543373051302.png/wm)            
5. 在 Python 包内部可以使用相对路径的方式来简化相对层级中包内模块的相互引用。比如在 shiyanlou 包的内部，如果想要在 louplus.py 文件中引入 courses 模块，可以使用 import courses 或是 from . import courses。如果想要单独运行 louplus.py 文件查看效果就需要在 /home/shiyanlou 目录下执行 python3 -m shiyanlou.louplus。            
            
Python 的 -m 参数用于将一个模块或包当作一个脚本运行。            
            
而如果想要在 totalnums.py 文件中引入 courses.py 文件中的 java 函数 ，可以使用 from ..courses import java。            
![运行包](https://doc.shiyanlou.com/document-uid13labid9150timestamp1543373051701.png/wm)             
            
## 异常处理            
1. finally 关键字是用来进行清理工作，经常和 except 一起使用，即无论是正常还是异常，这段代码都会执行。另外 except: 这个语句后不写任何参数，表示将处理所有 try 代码块中抛出的异常。            
```python            
filename = '/etc/protocols'            
f = open(filename)            
try:            
    f.write('shiyanlou')            
except:            
    print("File write error")            
finally:            
    print("finally")            
    f.close()            
```            
            
2. 抛出异常            
            
如果我们希望在程序执行过程中抛出一些异常，该如何操作呢？可以使用 raise 语句。            
```python            
raise 异常名称            
```            
            
例如，我们在代码里希望抛出一个 ValueError，直接使用：            
```python            
raise ValueError()            
```            
            
外部的代码就可以使用 except ValueError 进行捕获和处理了。            
            
## 包管理工具            
pip 的常见命令如下：(也可以在 pip 前加上 sudo ，获取 root 权限)            
            
显示版本和路径：pip3 --version            
* 升级 pip：sudo pip3 install --upgrade pip            
* 安装包：(sudo) pip3 install package，如果需要指定版本就是：pip3 install package==1.0.3 (写具体的版本号)            
* 卸载包：pip3 uninstall package            
* 升级包：pip3 install --upgrade package，可以使用 ==,>=,<=,<,> 来指定版本号            
* 查看安装已安装的包：pip3 freeze            
* 把需要安装的一系列包写入 requirements.txt 文件中，然后执行：pip3 install -r requirements.txt            
      
## 列表      
1. 列表是有顺序的，我们在执行所有的列表操作的过程中都要时刻记住这一点，有序的列表可以进行反转。      
2. 如果我们有两个列表，想合并到一起，一种方法是将其中一个列表合并到另外一个列表的末尾位置，可以使用 extend()。      
```python      
courses = ['Ruby', 'Linux', 'Python']      
new_courses = ['Cloud', 'C++']      
courses.extend(new_courses)      
```      
## 元组      
1. uple（元组）是一种特殊的列表，不同点是元组一旦创建就不能修改，上述的所有会修改列表内容的操作例如 sort()、append()等对于元组都不再适用      
2. 在编写程序的时候，元组比列表更安全，如果是只读的数据，尽可能使用元组，另外务必在使用过程中时刻记住元组是不可修改的，但是元组中如果包含可变的数据元素，这些数据元素是可以修改的，例如元组中包含一个列表，这个列表的内容是可以修改的。      
3. 需要提醒下如果要创建只有一个元素的元组，是不可以直接使用括号中一个元素的，需要在元素值后面跟一个逗号。      
      
## 集合      
1. set（集合）是一个无序不重复元素的数据集，对比列表的区别首先是无序的，不可以使用索引进行顺序的访问，另外一个特点是不能够有重复的数据      
2. 项目开发中，集合主要用在数据元素的去重和测试是否存在。集合还支持一些数学上的运算，例如：union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）。      
3. 创建集合的方法比较简单，使用大括号或者 set 函数，需要注意空的集合不能够使用 {} 创建，只能使用 set 函数，因为{} 创建的是一个空的字典 ：      
```python      
>>> courses = set()      
>>> type(courses)      
<class 'set'>      
>>> courses = {'Linux', 'C++', 'Vim', 'Linux'}      
>>> courses      
{'Linux', 'Vim', 'C++'}      
      
```      
4. 集合还可以直接由字符串与 set 函数进行创建，会将字符串拆散为不同的字符，并去除重复的字符：      
```python      
>>> nameset = set('shiyanlou.com')      
>>> nameset      
{'c', 'o', '.', 'm', 'u', 'h', 's', 'a', 'n', 'i', 'y', 'l'}      
```      
      
5. 集合操作      
现在我们尝试两个集合的运算：      
      
>>> set1 = {1,3,2,4 }      
>>> set2 = {3,4,5,6}      
      
'|' 操作，存在 set1 中或 set2 中的元素，等效于 union 操作：      
      
>>> set1 | set2      
{1, 2, 3, 4, 5, 6}      
>>> set1.union(set2)      
{1, 2, 3, 4, 5, 6}      
      
& 操作，返回即在 set1 又在 set2 的元素：      
      
>>> set1 & set2      
{3, 4}      
      
- 返回在 set1 不在 set2 的元素：      
      
>>> set1 - set2      
{1, 2}      
      
^ 操作，返回只存在两个集合中的元素：      
      
>>> set1 ^ set2      
{1, 2, 5, 6}      
