import random 
text = {
    'subject':["man","women",'girl','boy'],
    'predicate':[
        #主谓宾结构
        [ 'buy','buying','bought']
    ],
    "accusative" : ['phone','ring','book']
}

attribute =[
    #不定代词
    ['some','every','all','most','any'],
    #形容词
    [
        ['tall','short','fat','slim'],
        ['faddish'],
        ['expensive'],
        ['intersting']
    ],
    #名词
    [
        #修饰人的
        ['middle age','youth'],
        #修饰手机
        ['huawei','sansung'],
        #修饰戒指
        ['diamond','gold'],
        #修饰书
        ['story','fairy']
    ],
    #介词短语
    [
        ['with a big nose','in red','with a glasses'],
        ['with a big screen'],
        ['with an intricate pattern'],
        [' with a story']
    ],
    #句子
    [
        ['that I know','that I hate','that i like'],
        ['that I like'],
        ['that I want','that I have been buying'],
        ['that went to sale yeaterday']
    ],
    #过去分词
    [
       ['sent to beijing'],
       ['made in chian'],
       ['made in USA'],
       ['written by xxx']
    ]
]

def create():
    # 句子结构固定为主谓宾
    #随机主语
    