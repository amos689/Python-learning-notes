import jieba as jb
import wordcloud as wc
f=open('E:\learning notes\C_learing\pyexperiment\week7\F2.txt','r',encoding="UTF-8")
t=f.read()
f.close()
ls=jb.lcut(t)
txt=' '.join(ls)
w=wc.WordCloud(background_color='white',width=1000,height=700,font_path='msyh.ttc',\
    stopwords=['的','等','和','在','要','把','更','各','上','下','对','是','好','有','不','了','以','让','使','为','与','中','多','少','以上'],\
        max_words=100)
w.generate(txt)
w.to_file('wc2.png')