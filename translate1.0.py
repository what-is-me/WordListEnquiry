#===================================================================
#       Filename :		translate 1.0       
#       Creator:		what-is-me           
#       Created date:	2021/03/23
#       Location:       https://github.com/what-is-me/wordlisttranslate
#====================================================================


# -*- coding: utf-8 -*-


import requests
import re
import codecs
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as messagebox
import tqdm


def getHtml(url):
    #获得网址源代码
    headers = {
        "User-Agent": "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
    page = requests.get(url, headers=headers)
    page.encoding = 'utf-8'
    html = page.text
    return html


def getImg_youdao(html):
    iPos = 0
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
        result = result + '\t'+''.join(img_list[c])
    result = re.sub('<li>', '\t', result)
    result = re.sub(r'<(.*?)>', '\t', result)
    return result


def getImg_jinshan(html):
    iPos = 0
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
        result = result + ''.join(img_list[c])
    result = re.sub('<i>', '\t', result)
    result = re.sub('&lt;', '[', result)
    result = re.sub('&gt;', ']', result)
    return re.sub(r'<(.*?)>', '', result)

'''
def getImg_jinshanmobile(html):
    iPos = 0
    reg = r'<ul class="dic-basic-explain">(.*?)</ul>'
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
        result = result + ''.join(img_list[c])
    result = re.sub('<li>', '\t', result)
    result = re.sub('::before', '', result)
    result = re.sub('::after', '', result)
    return re.sub(r'<(.*?)>', '', result)
'''
#!TODO: 本来是想做一个手机版金山查询的，但是似乎出了一点问题，希望有大佬修复一下

def getImg(html, choice):
    if(choice == 1):
        return getImg_youdao(html)
    if(choice ==2):
        return getImg_jinshan(html)
    else:
        return getImg_jinshanmobile(html)


def url(choice):#选择翻译网站
    if(choice == 1):
        return "http://dict.youdao.com/w/eng/"
    if(choice==2):
        return "https://www.iciba.com/word?w="
    else:
        return "https://m.iciba.com/"


class Application(Frame):#图形化界面
    w=500
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):#图形化界面布局
        
        #文件路径的选择：
        self.path_var = "文件路径"
        self.xx = StringVar()
        self.result = StringVar()
        self.word = StringVar()
        Label(self, text="原文档：").grid(row=0, sticky="w")
        self.txt = Entry(self, width=70)
        self.txt.grid(row=0, column=1)
        self.txt.delete(0, "end")
        self.txt.insert(0, self.path_var)
        Label(self, text="翻译文档：").grid(row=1, sticky="w")
        self.save = Entry(self, width=70)
        self.save.grid(row=1, column=1)
        self.save.delete(0, "end")
        self.save.insert(0, self.path_var)
        Button(self, text="选择要翻\n译的文件", command=self.callback).grid(
            row=0, column=2, rowspan=2, sticky="n" + "s" + "w" + "e")
        
        #词典选择栏以及翻译（运行）按钮：
        Label(self, text="选 择\n你 的\n词 典").grid(row=2, sticky="w", rowspan=2)
        URL = [
            (" 有  道", 1),
            (" 金  山", 2)
            #("金山手机版",3)
        ]
        size=2
        self.v = IntVar()
        self.v.set(2)
        for choice, num in URL:
            self.b = Radiobutton(self, text=choice, variable=self.v, value=num)
            self.b.grid(row=num+1, column=1, sticky="w")
        self.alertButton = Button(
            self, text='translate', command=self.translate)
        self.alertButton.grid(row=2, column=2,rowspan=size)
        
        #进度条：
        Label(self, text='进度:').grid(row=size+2)
        self.canvas = Canvas(self, width=self.w, height=22, bg="white")
        self.canvas.grid(row=size+2,column=1)
        Label(self, textvariable=self.xx).grid(row=size+2, column=2)
        
        #每个单词的查询结果：
        Label(self, textvariable=self.word).grid(row=size+3)
        Label(self, textvariable=self.result,
                width=100).grid(row=size+3, column=1,columnspan=2)
    
    def change_schedule(self,now_schedule, all_schedule):
        #进度百分比
        self.xx.set(str(round((now_schedule+1)/all_schedule*100,2)) + '%')
        if round((now_schedule+1)/all_schedule*100, 2) == 100.00:
            self.xx.set("完成")

    def callback(self):
        filetypes = [("文本文件", "*.txt")]  # 设置可以选择的文件类型，不属于这个类型的，无法被选中
        file_name = askopenfilename(
            title='选择单个文件', filetypes=filetypes, initialdir='C:/Users/cqc/Desktop/')
        self.path_var = file_name
        self.txt.delete(0, "end")
        self.txt.insert(0, self.path_var)
        self.savepath_var = re.sub('.txt', '_translated.txt', self.path_var)
        self.save.delete(0, "end")
        self.save.insert(0, self.savepath_var)

    def translate(self):
        #翻译主程序
        try:
            title = self.path_var
            title_save = self.save.get()
            choice = self.v.get()
            f = open(title)
            n = len(f.readlines())
            f.close()
            cnt = 0
            fill_line = self.canvas.create_rectangle(
                    1.5, 1.5, 0, 23, width=0, fill="white")
            m = 500
            x = self.w / m
            self.canvas.coords(fill_line, (0, 0, self.w, 60))
            self.master.update()
            fill_line = self.canvas.create_rectangle(
                1.5, 1.5, 0, 23, width=0, fill="black")
            #for cnt in tqdm.trange(0, n):#控制台进度条
            for cnt in range(0, n):
                x = x + self.w / n
                self.canvas.coords(fill_line, (0, 0, x, 60))
                self.master.update()
                f = open(title)
                w = codecs.open(title_save, "a+", "utf-8")
                word = f.readlines()[cnt]
                word = word.strip('\n')
                if(len(word) > 0):
                    w.write(word)
                    html = getHtml(url(choice)+word)
                    ret = getImg(html, choice)
                    self.word.set(word+":")
                    self.result.set(ret)
                    w.write(ret + '\n')
                    self.change_schedule(cnt,n)
                f.close()
                w.close()
        except:
            messagebox.showerror("Translate 1.0 error", "ERROR!")


app = Application()
choice = 0
app.master.title('Translate 1.0')
app.mainloop()
