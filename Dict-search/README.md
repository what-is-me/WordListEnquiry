# wordlistenquiry
- 源自本人项目https://github.com/what-is-me/WordListEnquiry
## 各函数及用法
- 查询单个单词/词组的详细解释：
    `def search(word, choice=1):`
    
- 查询单词/词组列表，并生成[字典(dict)]：
    `def wordlist_todict(wordlist, choice=1):`
    
- 查询单词/词组列表，并生成[列表(list)]：
    `def wordlist_tolist(wordlist, choice=1, div=" : ", needword=True):`
    
    - div是输出的list里单词和意思之间的分隔符
        比如：`route` **:** `n.路线，航线；道路，公路；（交通工具的）固定路线；巡访；途径，渠道；递送路线；用于美国干线公路号码前;v.按特定路线发送，为……规定路线;`
        
    - needword为False则表示return纯解释列表
        比如：
        
        `needword = False`: `n.路线，航线；道路，公路；（交通工具的）固定路线；巡访；途径，渠道；递送路线；用于美国干线公路号码前;v.按特定路线发送，为……规定路线;`
        
        `needword = True`: `route : n.路线，航线；道路，公路；（交通工具的）固定路线；巡访；途径，渠道；递送路线；用于美国干线公路号码前;v.按特定路线发送，为……规定路线;`
    
- 上述3个函数中，默认查询源为“有道[英]”

- 帮助：
  `def help():`

## 各个查询源（使用choice选择）

- 英>>
    1.有道
    2.金山
    3.bing
    4.海词
- 日>>
    5.有道
- 法>>
    6.有道
- 德>>
    7.德语助手