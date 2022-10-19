import jieba as jb
import wordcloud as wc
import numpy as np
from PIL import Image
pic = np.array(Image.open("E:\learning notes\C_learing\pyexperiment\week7\F1.png"))
f=open('E:\learning notes\C_learing\pyexperiment\week7\F1.txt','r',encoding="UTF-8")
t=f.read()
f.close()
ls=jb.lcut(t)
txt=' '.join(ls)
w=wc.WordCloud(background_color='white',font_path='msyh.ttc',\
    stopwords=['的','等','和','在','要','把','更','各','上','下','对','是','好','有','不','了','以','让','使','为','与','中','多','少','以上'],\
        mask=pic)
w.generate(txt)
w.to_file('wc2.png')