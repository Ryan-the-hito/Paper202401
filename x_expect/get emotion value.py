#!/usr/bin/env python3

import nltk
import re
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import pylab as pl
import matplotlib
import codecs
import numpy as np
import os

def remove_stopwords_from_text(text):
    tokens = nltk.word_tokenize(text)
    stopword_list = nltk.corpus.stopwords.words('english')
    filtered_tokens = []
    for token in tokens:
        if token not in stopword_list:
            filtered_tokens.append(token)
    result = ' '.join(filtered_tokens)
    return result

def remove_characters_from_text(text):
    text = text.strip()
    PATTERN = r'[^a-zA-Z0-9]'
    filtered_text = re.sub(PATTERN, r' ', text)
    return filtered_text

def normalize_text(text):
    text = remove_characters_from_text(text)
    text = remove_stopwords_from_text(text)
    return text

# 1


path = '/Users/ryanshenefield/Downloads/original data'
file_names = os.listdir(path)
file_names.remove('.DS_Store')
for r in range(len(file_names)):
    fullpath = os.path.join(path, file_names[r])
    name = '/Users/ryanshenefield/Downloads/emotion/'
    text = codecs.open(fullpath).read()
    text = text.split('文件')
    text.remove(text[-1])

    text_cleaned = []
    for i in text:
        if len(i) > 50:
            text_cleaned.append(i)

    targetlist = []
    dateline = codecs.open('date_full.txt', 'r', encoding='utf-8').read().split('\n')
    t = 0
    while 0 <= t <= len(dateline) - 1:
        print(dateline[t])
        for x in range(len(text_cleaned)):
            if dateline[t] in text_cleaned[x]:
                targetlist.append(text_cleaned[x])
            else:
                continue
        if targetlist != []:

            txt_list = []
            for i in targetlist:
                i = normalize_text(i)
                txt_list.append(i)

            print(len(txt_list))

            # 2

            senti_score = []
            for i in txt_list:
                a1 = TextBlob(i).sentiment
                senti_score.append(a1)
            print('TextBlobed')

            # 3

            pol = []
            sub = []
            for ele in senti_score:
                pol.append(ele.polarity)
                sub.append(ele.subjectivity)
            mean = np.mean(pol)
            print(str(mean))

            # 4
            result = dateline[t] + ',' + str(mean) + '\n'
            with open(name + file_names[r].replace('.txt', '') + '_end.csv', 'a', encoding='utf-8') as f0:
                f0.write(result)
            print('Saved')

        if targetlist == []:
            result = dateline[t] + ',' + '0'+ '\n'
            with open(name + file_names[r].replace('.txt', '') + '_end.csv', 'a', encoding='utf-8') as f0:
                f0.write(result)
            print('Saved')

        t += 1
        targetlist = []


# # 4
#
# mean = np.mean(pol)
# sd = np.std(pol)
# print(mean, sd)
# print(max(pol))
# print(min(pol))

# # 5
#
# myfont = matplotlib.font_manager.FontProperties(fname=r'ziti.ttf')
#
# plt.title(u'法国对制裁手段的情感分析', fontproperties=myfont)
# plt.xlabel(u'情感得分', fontproperties=myfont)
# plt.ylabel(u'频率', fontproperties=myfont)
# plt.hist(pol, bins=17, color='black', alpha=0.5, rwidth=0.9)
# plt.show()
