坚持就是胜利
====

不定期更新这个文档

# 几个基本问题

- 学会用google
- 遇到完全不明白的技术，先到百度找中文资料，快速了解以后，到官方网站找正式的文档再深入
- 囫囵吞枣地看文档，先了解大概，再有重点深入
- 看资料的时候，对着代码抄一遍才有感觉
- 有习惯地做总结和归纳，定期然后给别人讲（小黄鸭：同事或者我）
- 我只能给出知识点或者资料，需要你去看和理解以后，来给我讲，通过给我讲的过程，来查漏补缺。另外就是找能在工作中用到py的点，用得多自然就熟练

大概分三个阶段：

1. 入门（2-3周）：掌握基本的语法和简单的标准库，能写几个类和几十行的代码完全简单的任务
2. 熟练（2-3月）：掌握大部分的高级语法结构，在使用时不会因为语法导致工作无法继续。掌握几十个标准库和常用的第三方库（根据工作的需要）。在需要某个功能的时候，能够想到大概什么库里会有类似的功能。
3. 在掌握了基本功之后，就可以自行安排针对性的深入了。定期了解新版本的功能，关注pyCon，不断补充第三方库的使用，阅读更多的书籍，扩展工作的应用范围（例如大数据，机器学习等）

为了能更高效的学习，学习任务中除了python以外，还会在适当的时候插入一些其它内容，例如git。

# 第一阶段

## 入门1：3天

1. 安装python3环境。了解IDEL
https://www.python.org/downloads/
2. 安装pycharm ide。了解基本的使用：创建工程，查看代码，查找，运行，格式化代码等等
3. 基本语法知识点：基本类型（特别是字典和列表），分支循环，函数，模块

Python基础教程（第二版）1-6章

## 更多字符串：2天

字符串操作“非常”重要，大部时候写代码实际上都是在以各种形式进行字符串处理。字符串非常熟练的话，会节省非常多的时间。

1. 安装ipython和jupyter notebook
2. 熟悉markdown语法
3. str/unicode/string
4. hashlib/json/pickle

https://ipython.org/

ipython和notebook只是个工具。安装好了以后，就多用ipython的交互console，比原生的idel方便很多。

https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

快速了解md的语法，会在notebook中穿插使用python code block和markdown block。以后有要总结和记录的可以写成notebook。

https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
整个4.7节。对常用的函数都有个了解。

https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
4.8.1-4.8.4。对bytes有概念，知道str和bytes的区别。

https://docs.python.org/3/library/string.html
整个过一下，有个大概的概念

https://docs.python.org/3/howto/unicode.html
理解unicode的概念。能在python中清楚的知道什么时候在使用unicode什么时候在操作binary data。对于常见的en/decoding操作有概念，大概能猜到什么意思。

https://docs.python.org/3/library/hashlib.html
知道怎么计算字符串的md5/sha1/sha256。其他看不懂的算法不用看。

https://docs.python.org/3/library/json.html
知道怎么把简单的数据通过json编码和解码。customized en/decoder暂时不用看。

https://docs.python.org/3/library/pickle.html
了解pickle的作用，能够把简单的python对象进行序列化。

## 正则表达式：2天

http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html
通过这个中文教程30分钟入门。

https://docs.python.org/3/howto/regex.html#regex-howto
主要了解re的语法，和常见的用法。对于re库不用纠结。

https://docs.python.org/3/library/re.html
对于基本的函数一定要熟悉，不常见的函数有个了解就行。

## 官方入门：3天

python基础教程（第二版）7-11章

https://docs.python.org/3/tutorial/index.html

补全基本的语法知识。太高级的先不用看。
官方入门的体系写得很好，把基础知识都涵盖到了。

## 简单标准库：1天

datetime, os.path, pprint, math, random, os, sys, platform

把里面你认为可能能用到函数敲一遍试试。你觉得不太能用得到的函数，看个名字和例子，知道是干什么的就行。

## 命令行标准库：2天

shutil, argparse, glob, tempfile, signal

这些标准库能帮助你把原来用shell实现的功能python化。通过使用这些库，平时在工作中把重复操作变成脚本。一是练习，二是节省时间。

https://www.python.org/dev/peps/pep-0008/
https://www.python.org/dev/peps/pep-0020/

两篇关于code style的文章。理解python的规范，以后尽量遵守。

第一阶段结束后，给我来讲解一下学到的知识体系。

# 第二阶段

## Python学习手册（第4版），两周

https://book.douban.com/subject/6049132/

## 更多标准库

collections, enum, heapq, decimal 
itertools, functools

## 日志

logging

## 多线程

threading, multiprocessing, subprocess

## http client

urllib, request, pyquery

## shell

bash, grep/find/awk/sed/apt

## 工程相关

pip/virutualenv：1天

## 测试

pydoc/unittest/pytest/selenium

## docker

## git

https://git-scm.com/book/zh/v2 中文版
https://git-scm.com/book/en/v2
http://learngitbranching.js.org/

## 数据库

mysql：1天

sqlite3

redis


## stdlib: 全部过一圈，两周

https://docs.python.org/3/library/index.html

## Django: 一周

https://docs.djangoproject.com/en/1.11/intro/

fabric/ansible

http://python-guide-pt-br.readthedocs.io/en/latest/
