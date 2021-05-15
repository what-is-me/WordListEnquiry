# 外语单词批量查询软件

这是一个简单的爬虫程序，用于批量查询外语（不只有英语哦）单词。<br>
我为它做了有图形界面，以方便教师和学生使用。<br>
希望有一颗小星星鼓励一下⭐<br>
参考于17年停更的老项目[QueryMoreWords](https://github.com/ztjryg4/QueryMoreWords)

## **为谁准备的**（目标用户）

- 初中、高中生、考研党、老师：在做完一批外文阅读后，你记录下了一批生词，准备自己背诵/做成ppt讲解。这时你决定：
  1. 使用有道/欧路/金山一个一个查，并在`Ctrl+C`，`Ctrl+V`的帮助下做成《单词-解释》表格。
  2. 使用本软件简化上述步骤。
- 小语种学员（法/日）：你有一份纯单词的（无解释）考试大纲，准备在考前背诵。这时你打算：
  1. 在百度文库上下载~~排版可能不符合你心意的~~付费的别人做好的表格。
  2. 使用本软件**免费**制作带解释的考试大纲。

## **查词源的选择**

- **金山**有时候会维护，无法使用
- **海词**查询速度**最快**
- **法语、日语**目前只有有道源
- **德语**目前只有德语助手这个源
- 某些源查特定单词会崩溃，是网页问题

### **被查询的单词列表文件格式**

- 必须是`xxx.txt`/`xxx.xlsx`
- 文档格式要求：<br>
    <tr>
      <td style='text-align:center;' >&nbsp;</td>
      <td style='text-align:center;' >单词/词组放在哪</td>
    </tr>
    <tr>
      <td style='text-align:center;' >"xxx.txt"</td>
      <td style='text-align:center;' >每行一个，可以空行</td>
    </tr>
    <tr>
      <td style='text-align:center;' >"xxx.xlsx"</td>
      <td style='text-align:center;' >A列，从第1行开始，每个单元格一个，不要空行</td>
    </tr>
- 各语言情况：<br>
    <tr>
      <td style='text-align:center;' >语言</td>
      <td style='text-align:center;' >支持</td>
    </tr>
    <tr>
      <td style='text-align:center;' >英语</td>
      <td style='text-align:center;' >支持词组</td>
    </tr>
    <tr>
      <td style='text-align:center;' >日语</td>
      <td style='text-align:center;' >仅支持假名</td>
    </tr>
    <tr>
      <td style='text-align:center;' >法语</td>
      <td style='text-align:center;' >支持词组</td>
    </tr>
    <tr>
      <td style='text-align:center;' >德语</td>
      <td style='text-align:center;' >不支持词组</td>
    </tr>

## 下载：[download](https://github.com/what-is-me/wordlisttranslate/releases/)
## 各版本更新情况：
### [v1.0]
- 拥有`有道`,`金山`,`bing`,`海词`四个英语单词查询源。

### [v1.1]
- [[v1.1 download from gitee]](https://gitee.com/whatisme/wordlisttranslate/releases/v1.1)
- 更新内容：
  - ~~如果短语无法查询到结果，则**全部**替换为翻译函数~~如果短语无法查询到结果，且在第二列有内容，则不会替换为翻译函数 。

### [v1.2]
- 更新内容：
  - 增添了有道法语/日语查询源（有道）。
  - 日语请全部使用假名（平/片均可），含有汉字会无法查出。

### [v1.3]
- 更新内容：
  - 增加了德语（仅限单词）（德语助手）
