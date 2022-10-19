'''
jieba库函数
1.精确模式:jieba.lcut(s)                返回一个列表型分词结果，不存在冗余
2.全模式:jieba.lcut(s,cut_all=True)     返回一个列表型分词结果，存在冗余
3.搜索引擎模式:jieba.lcut_for_search(s)  返回一个列表型分词结果，存在冗余
4.新增词:jieba.add_word(s)              向分词字典新增s
'''
import jieba
txt = open("E:\learning notes\C_learing\pyexperiment\week7\F1.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(15):
    word, count = items[i]
    print ("{0:<10}->{1:>5}次".format(word, count))