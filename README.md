# 英语单词批量查询软件

一个简单的爬虫程序，用于批量查询单词，有图形界面。

## **下载**

- 直接去Release下载，即https://github.com/what-is-me/wordlisttranslate/releases/
- Windows64位用户下载1.0.exe即可运行
- 有条件的(有python的)/其他系统用户直接下载源代码执行吧，顺便看看有没有bug

## **查词网站的选择：**

- 金山有时候会维护，无法使用
- 海词查询速度**最快**
- 当查询不到意思时，excel文件的输出会用有道翻译函数替代

## **文件格式**

- 被查询的单词列表必须是txt文件/xlsx文件
- txt必须每行一个单词/词组，每行多个单词会被视作词组
- excel必须第一列是单词/词组，运行程序后第二列会生成解释，第三列及以后就随便你写什么了

  excel第一列每一个单元格一个单词/词组，中间空行会出现错误

## **测试文件**

- txt文件可以用"sample.txt"进行测试
- excel文件可以用"sample.xlsx"进行测试

## **无法解决的bug**

- 查询特定单词时，会导致崩溃，这与网页有关

## **相关规定**

- 不应该爬取相关网站robots.txt里规定禁止爬取的内容
- 查询源分别为：


| 源 | 网站 | 爬虫协议 |
| :-: | :-: | :-: |
| 有道 | http://dict.youdao.com/w/ | http://dict.youdao.com/robots.txt |
| 金山 | https://www.iciba.com/word?w= | 无/未找到 |
| bing | https://cn.bing.com/dict/search?q= | https://cn.bing.com/robots.txt |
| 海词 | https://dict.cn/search?q= | https://dict.cn/robots.txt |
