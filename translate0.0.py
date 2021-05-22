# -*- coding: utf-8 -*-
import requests
import re
import codecs
youdao = "http://dict.youdao.com/w/eng/"
jinshan = "https://www.iciba.com/word?w="
title = input("title:")
title2 = title+'output'
f = open(title+".txt")
n = len(f.readlines())
f.close
cnt = 0
headers = {
    "User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
choice = 0
choice = input("1.youdao\n2.jinshan\n>>>")

if (choice == '1'):
    www = youdao
else:
    www = jinshan

for cnt in range(0, n):
    def getHtml(url):
        page = requests.get(url, headers=headers)
        page.encoding = 'utf-8'
        html = page.text
        return html

    f = open(title+".txt")
    w = codecs.open(title2+".txt", "a+", "utf-8")
    '''
    w = open(title2+".txt", "a+")
    '''
    word = f.readlines()[cnt]
    word = word.strip('\n')
    percent = (int)(cnt/n*100)
    print(percent, end='')
    print('%|', end='')
    num = int(percent/5)
    print(num*'='+'>'+(20-num)*' '+'|', end='')
    print(word, end='')
    w.write(word+":")
    iPos = 0
    if(len(word) > 0):
        the_url = www+word

    html = getHtml(the_url)

    def getImg(html):
        global iPos
        if(choice == '1'):
            reg = r'<li>(.*?)</li>'
            img = re.compile(reg)
            img_list = re.findall(img, html)
            if len(img_list) == 0:
                result = "未收录"
                return result
            for i in range(0, len(img_list)):
                element = ''.join(img_list[i])
                finding = '. '
                nPos = element.find(finding)
                if nPos >= 0:
                    iPos = i
            result = ''
            for c in range(0, iPos+1):
                '''if c == 0:
                s=''
                else:
                s='\n'
                '''
                result = result + '\t'+''.join(img_list[c])
            result = re.sub('<li>', '\t', result)
            result = re.sub(r'<(.*?)>', '\t', result)
            return result
        else:
            reg = r'<ul class="Mean_part__1RA2V"><li>(.*?)</ul>'
            img = re.compile(reg)
            img_list = re.findall(img, html)
            if len(img_list) == 0:
                result = "未收录"
                return result
            for i in range(0, len(img_list)):
                element = ''.join(img_list[i])
                finding = '. '
                nPos = element.find(finding)
                if nPos >= 0:
                    iPos = i
            result = ''
            for c in range(0, iPos+1):
                '''if c == 0:
                s=''
                else:
                s='\n'
                '''
                result = result + ''.join(img_list[c])
            '''for c in range(0,len(result)):
                if result[c]=='\n':
                    result.pop(c)
                    c-=1'''
            result = re.sub('<i>', ':', result)
            result = re.sub('&lt;', '[', result)
            result = re.sub('&gt;', ']', result)
            return re.sub(r'<(.*?)>', '', result)
    print(getImg(html), end='\n')
    w.write(getImg(html) + '\n')
    f.close()
    w.close()
