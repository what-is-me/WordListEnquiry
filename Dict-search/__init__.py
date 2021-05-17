'''
Author: what-is-me
E-mail: nt_cqc@126.com
Github: https://github.com/what-is-me
LeetCode: https://leetcode-cn.com/u/what-is-me/
Date: 2021-05-17 23:22:14
LastEditors: what-is-me
LastEditTime: 2021-05-18 00:57:58
Description: 查询单个单词/词组意思
'''
import re
import urllib.parse
import requests


class getimg:
    def youdao(html):
        html = html.split('</h2>')[-1]
        html = html.split('<span>网络释义</span>')[0]
        reg = r'<li>(.*?)</li>'
        img = re.compile(reg)
        img_list = re.findall(img, html)
        result = ""
        for s in img_list:
            if (s != ""):
                result = result + s + ";"
        result = "".join(result.split())
        result = re.sub(r'<(.*?)>', '', result)
        if result == '' or result[0:1] == '<a':
            return "未收录"
        return result

    def jinshan(html):
        reg = r'<ul class="Mean_part__1RA2V"><li>(.*?)</ul>'
        img = re.compile(reg)
        img_list = re.findall(img, html)
        result = "".join(img_list)
        result = re.sub('&lt;', '[', result)
        result = re.sub('&gt;', ']', result)
        result = re.sub(r'<(.*?)>', '', result)
        if result == "":
            return "未收录"
        return result

    def bing(html):
        reg = r'<meta name="description" content="(.*?)" />'
        img = re.compile(reg)
        result = re.search(img, html).group()
        result = result.split('<meta name="description" content="')[-1]
        result = result.split('" />')[0]
        result = re.sub('必应词典为您提供', '', result)
        result = re.sub('的释义', '', result)
        result = re.sub('英', '', result)
        result = re.sub('美', '', result)
        result = re.sub('，', '', result)
        result = result.split('网络释义：')[0]
        result = re.sub(r'\[(.*?)\]', '', result)
        if result == "" or result[0:3] == "必应词典":
            return "未收录"
        return result

    def haici(html):
        html = html.split('<div class="basic clearfix">')[-1]
        html = html.split('<li style="padding-top: 25px;">')[0]
        reg1 = r'<span>(.*?)</span>'
        img1 = re.compile(reg1)
        img_list1 = re.findall(img1, html)
        reg2 = r'<strong>(.*?)</strong>'
        img2 = re.compile(reg2)
        img_list2 = re.findall(img2, html)
        if len(img_list2) == 0:
            result = "未收录"
            return result
        result = ''
        if(len(img_list1) == 0):
            for i in range(0, len(img_list2)):
                result += img_list2[i]
        else:
            for i in range(0, len(img_list1)):
                result += "["+img_list1[i]+"]"
                result += img_list2[i]
        return result

    def youdao_jp(html):
        html = html.split('<!--日汉词典结果 -->')[-1]
        html = html.split('<!--网络翻译-->')[0]
        result = "".join(html.split())
        result = re.sub(r'<span class="keyword">(.*?)</span>', '', result)
        result = re.sub(r'<h4>(.*?)</sup>', '', result)
        result = re.sub(r'<sup>(.*?)</sup>', '', result)
        result = re.sub('<span>网络释义</span>', '', result)
        result = re.sub(r'例证:(.*?)li>', '', result)
        result = re.sub(r'谚语或成语:(.*?)li>', '', result)
        result = re.sub(r'<p class="exam-sen">(.*?)</p>', '', result)
        result = re.sub(r'<(.*?)>', '', result)
        if result[0] == "【":
            return "未收录,日语暂不支持有道翻译函数"
        result = result.split('【')[-1]
        return '【'+result

    def youdao_fr(html):
        html = html.split('<!--Title -->')[-1]
        html = html.split(
            '<div id="webTrans" class="trans-wrapper trans-tab">')[0]
        result = re.sub(r'<(.*?)>', '', html)
        return "".join(result.split())

    def de(html):
        html = html.split('<div id="ExpFCChild"  class="expDiv">')[-1]
        n = 0
        while(html[n] != '\n'):
            n += 1
        result = html[0:n-1]
        result = re.sub(r'<i>(.*?)</i>', '', result)
        result = re.sub(r'<span class=eg>(.*?)</span>', '', result)
        result = re.sub(r'<span id="phrase">(.*?)</span>', '', result)
        result = re.sub(r'<[a-zA-Z]{1,}(.*?)>', '', result)
        result = re.sub(r'<\/.*?>', '', result)
        result = re.sub(r'<\!.*?>', '', result)
        result = "".join(result.split())
        result = re.sub('赞踩改进更换举报initThumbnail', '', result)
        result = re.sub('欧路软件版权所有', '', result)
        result = re.sub('欧路软件', '', result)
        result = re.sub('德语助手', '', result)
        result = re.sub("()", '', result)
        return result


def getImg(html, choice):
    if(choice == 1):
        return getimg.youdao(html)
    if(choice == 2):
        return getimg.jinshan(html)
    if(choice == 3):
        return getimg.bing(html)
    if(choice == 4):
        return getimg.haici(html)
    if(choice == 5):
        return getimg.youdao_jp(html)
    if(choice == 6):
        return getimg.youdao_fr(html)
    if(choice == 7):
        return getimg.de(html)


def url(choice):  # 选择翻译网站
    if(choice == 1):
        return "http://dict.youdao.com/w/eng/"
    if(choice == 2):
        return "https://www.iciba.com/word?w="
    if(choice == 3):
        return "https://cn.bing.com/dict/search?q="
    if(choice == 4):
        return "https://dict.cn/search?q="
    if(choice == 5):
        return "http://www.youdao.com/w/jap/"
    if(choice == 6):
        return "http://www.youdao.com/w/fr/"
    if(choice == 7):
        return "http://www.godic.net/dicts/de/"


def phrase(choice, word):  # 如果是词组，就将空格替换
    if(choice == 1):
        return re.sub(' ', '%20', word)
    if(choice == 2):
        return re.sub(' ', '%20', word)
    if(choice == 3):
        return re.sub(' ', '+', word)
    if(choice == 4):
        return re.sub(' ', '+', word)
    if(choice == 5):
        return re.sub(' ', '%20', word)
    if(choice == 6):
        return re.sub(' ', '%20', word)
    if(choice == 7):
        ans = urllib.parse.quote(word)
        return ans


def getHtml(url):
    # 获得网址源代码
    headers = {
        "User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    page = requests.get(url, headers=headers)
    page.encoding = 'utf-8'
    html = page.text
    return html


def help():
    help = '''
==================================================================================
            Help:
choice:
英>>
    1. 有道
    2. 金山
    3. bing
    4. 海词
日>>
    5. 有道
法>>
    6. 有道
德>>
    7. 德语助手
默认有道查询源
functions:
    查询单个单词/词组：
        search_word(word, choice=1)
    查询单词/词组列表，并生成[字典(dict)]：
        search_words_todict(wordlis, choice=1)
    查询单词/词组列表，并生成列表：
        search_words_tolist(wordlist, choice=1, div = " : ", needword = True)
        div是输出的list里单词和意思之间的分隔符
        needword为False则表示return纯解释列表
==================================================================================
'''
    print(help)


def search_word(word, choice=1):
    _url = url(choice) + phrase(choice, word)
    _html = getHtml(_url)
    return getImg(_html, choice)


def search_words_todict(wordlist, choice=1):
    _dict = {}
    for word in wordlist:
        _dict[word] = search_word(word, choice)
    return _dict


def search_words_tolist(wordlist, choice=1, div=" : ", needword=True):
    result_list = []
    for word in wordlist:
        result_list.append(
            ((word + div)if needword else "") + search_word(word, choice))
    return result_list
