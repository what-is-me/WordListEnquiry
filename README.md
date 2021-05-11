# ~~英语~~外语单词批量查询软件
[![](https://img.shields.io/github/stars/what-is-me/wordlisttranslate.svg?style=flat-square&logo=github&logoWidth=20&label=Star)](https://github.com/what-is-me/wordlisttranslate/stargazers)

一个简单的爬虫程序，用于批量查询~~英语~~外语单词，有图形界面。

## 介绍

### **动机：）**

- 某天，英语老师课后发了个巨大的单词表，只有英文，没有中文解释
- 这个时候我回想起某年暑假，做完老师布置的一本阅读，兴致冲冲准备做一个生词表，整了几天没整出来~~太枯燥了，反正我也不会背~~
- 单词表整理出来，你不一定会背，但是不整理，一定不会去背，本项目旨在减少整理时间（你只要输入单词就行了）（虽然它挺慢，但也比你一个一个复制粘贴查询复制粘贴进表格快得多吧）

### **目标用户**

- 初中、高中生、考研党：你可以用它来大大减少你做完一组阅读理解后生词积累的查询时间（也更方便背诵），省下来的时间多做几道数学题不香吗[卷起来了]~~我当时要是有这玩意也不至于高考这么糟糕~~
- 老师：用法与学生类似，~~虽然有的老师喜欢查纸质词典~~这个程序或许可以让你早睡一会儿
- 小语种学员（法/日）：纯单词（无解释）考试大纲的

### **查词网站的选择：**

- 金山有时候会维护，无法使用
- 海词查询速度**最快**
- 当查询不到意思时，excel文件的输出会用有道翻译函数替代

### **文件格式**

- 被查询的单词列表必须是txt文件/xlsx文件
- txt必须每行一个单词/词组，每行多个单词会被视作词组
- excel必须第一列是单词/词组，运行程序后第二列会生成解释，第三列及以后就随便你写什么了

  excel第一列每一个单元格一个单词/词组，中间空行会出现错误（大概有？我没测试过）

### **测试文件**

- txt文件可以用"sample.txt"进行测试
- excel文件可以用"sample.xlsx"进行测试

### **无法解决的bug**

- 查询特定单词时，会导致崩溃，这与网页有关（目前只在**有道**遇到过）（这个单词本身也比较生僻~~居然是个比较常用的学术英语词汇呢~~）（好像是个p开头的）

### **相关规定**

- 不应该爬取相关网站robots.txt里规定禁止爬取的内容
- 查询源分别为：


|  源  |                网站                |             爬虫协议             |
| :----: | :----------------------------------: | :---------------------------------: |
| 有道 |     http://dict.youdao.com/w/     | http://dict.youdao.com/robots.txt |
| 金山 |   https://www.iciba.com/word?w=   |             无/未找到             |
| bing | https://cn.bing.com/dict/search?q= |  https://cn.bing.com/robots.txt  |
| 海词 |     https://dict.cn/search?q=     |    https://dict.cn/robots.txt    |

### **代码规范**

- 我自己的的代码就很丑了，也不强求，毕竟txt和excel的读写不一样，每个网页html也不同。
- 希望后继者多多使用函数/类。

### **关于贡献**

- 能精简代码，规范代码，提速的最好
- 增加查询源的需要修改
  - `class getimg`：网页html的处理
  - `url(choice)`：增添一个网址
  - `phrase(choice, word)`：增添其词组中空格的替换
  - `def unfind(choice)`：增添其查询不到单词的返回结果
  - `class Application(Frame) : createWidgets(self): size , URL`：size++，URL列表里再添一个
- 增加本地查询源的可能要修改得更多

## 版本更新：[download](https://github.com/what-is-me/wordlisttranslate/releases/)
ps：代码肯定是最新版本的
### [v1.0] 基础版本
- Windows64位用户（基本上内存大于4g的都是）下载1.0.exe即可运行
- 其他系统用户直接下载源代码执行吧，顺便看看有没有bug
- ps: 源代码运行需要python环境，并安装两个库，在cmd/power shell里输入：
  - `pip install openpyxl`
  - `pip install requests`

### [v1.1] 更加人性化的少量修改
- [[v1.1 download from gitee]](https://gitee.com/whatisme/wordlisttranslate/releases/v1.1)
- 更新内容：~~如果短语无法查询到结果，则**全部**替换为翻译函数~~如果短语无法查询到结果，且在第二列有值，则不会替换为翻译函数 

### [v1.2] 走向多语言
- 更新内容：
  - ~~英语单词批量查询软件~~外语单词批量查询软件
  - 增添了有道法语/日语查询源
  - ！！！日语请全部使用假名（平/片均可），含有汉字会无法查出

