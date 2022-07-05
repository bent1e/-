# -*- coding: utf-8 -*-

from wordcloud import WordCloud
import jieba
import jieba.analyse as analyse
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
class WC(object):
    def draw_wordcloud(self):
        # 读入一个txt文件
        comment_text = open('C:/Users/Administrator/Desktop/test.txt', 'r').read()
        # 结巴分词，生成字符串，如果不通过分词，无法直接生成正确的中文词云
        cut_text = " ".join(jieba.cut(comment_text))
        result = jieba.analyse.textrank(cut_text, topK=1000, withWeight=True)
        # 生成关键词比重字典
        keywords = dict()
        array = ["A", 'B', "C", "D", "E"]
        for k in array:
            for i in result:
                keywords[i[0]] = i[1]
            image = np.array(Image.open("C:/Users/Administrator/Desktop/%s.png" %(k)))
            cloud = WordCloud(
                scale=3,
                font_path="C:/Windows/fonts/msyh.ttc",
                width=200,
                height=200,
                background_color='white',
                # 词云形状
                mask=image,
                # 允许最大词
                max_words=2000,
                # 最大号字体
                max_font_size=50)
            word_cloud = cloud.generate(cut_text)  # 产生词云
            word_cloud.to_file("C:/Users/Administrator/Desktop/画像%s.png" %(k))  # 保存图片
        #  显示词云图片
        plt.imshow(word_cloud)

        plt.axis('off')



if __name__ == '__main__':
    wc = WC()

    wc.draw_wordcloud()
