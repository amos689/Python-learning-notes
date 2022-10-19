import wordcloud as wc
import jieba as jb
txt1='life is short,you need python'
w1=wc.WordCloud(background_color='white')
w1.generate(txt1.replace(',',' '))
w1.to_file('wc2.png')
txt2='程序设计语言是用于书写计算机程序的语言。 语言的基础是一组记号和一组规则。 \
    根据规则由记号构成的记号串的总体就是语言。 在程序设计语言中，这些记号串就是程序。'
w2=wc.WordCloud(background_color='white',width=1000,height=700,font_path='msyh.ttc')
w2.generate(' '.join(jb.lcut(txt2)))
w2.to_file('wc3.png')