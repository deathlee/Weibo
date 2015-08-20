__author__ = 'zhuangli'
# -*- coding: utf-8 -*-
from DataObj import  RawData
import re
import os
from nltk.parse import stanford
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
# -*- coding: utf-8 -*-
def Pipeline(path):
    f = open(path, 'r')
    featurelist=[]
    for line in f:
        values=line.split("\t")
        data = RawData(values[0],values[1],values[2],values[6],values[3],values[4],values[5])
        featureExtractor(data)
    return featurelist
def featureExtractor(data):
    atList,sentence=atExtractor(data.content)
    hashTagList,sentence=activityExtractor(sentence)
    mentionExtractor(sentence)
def activityExtractor(sentence):
    return re.findall("#.*#", sentence, re.I),re.sub("@", '', sentence)
def urlExtractor(sentence):
    return re.findall("http\S+", sentence, re.I),re.sub("http\S+", '', sentence)
def atExtractor(sentence):
    return re.findall("@.*\\s", sentence, re.I),re.sub("#", '', sentence)
def ifBlackQuoteExtractor(sentence):
    flag=0
    if re.match(r"【.*】",sentence):
        flag=1
    return flag,re.sub("】", '', re.sub("【", '', sentence))
def ifQuote(sentence):
    flag=0
    if re.match(r"[.*]",sentence):
        flag=1
    return flag,re.sub("[", '', re.sub("]", '', sentence))
def mentionExtractor(sentence):
    seg=segmenter.segment(sentence)
    mentions=[]
    mention=""
    lastWord=""
    for tuple in st.tag(seg.split()):
        len=0
        if tuple[1]!='O':
            if len==0:
                mention+=tuple[0]
            else:
                if mention==lastWord:
                    mention+=tuple[0]
                else:
                    mentions.append(mention)
                    mention=""
                    len=0
            len+=1
        else:
            if mention!="":
                mentions.append(mention)
                mention=""
                len=0
        lastWord=mention
    return mentions

#segmenter = StanfordSegmenter(path_to_jar="./stanford-segmenter-2014-08-27/stanford-segmenter-3.4.1.jar",path_to_sihan_corpora_dict="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data", path_to_model="./stanford-segmenter-2014-08-27/data/pku.gz", path_to_dict="./stanford-segmenter-2014-08-27/data/dict-chris6.ser.gz")
#st = StanfordNERTagger('./stanford-ner-2015-04-20/classifiers/stanford-chinese-corenlp-2015-04-20-models/edu/stanford/nlp/models/ner/chinese.misc.distsim.crf.ser.gz','./stanford-ner-2015-04-20/stanford-ner.jar')
#Pipeline("data/weibo_train_data.txt")
#featureExtractor(data)
#for word in mentionExtractor(u'快的打车红包 「快的小财神」送头彩啦！欢庆快的打车市场份额稳居第一！10个城市9个快，10张订单9张快，做快乐的大多数，打车就送超大红包！ 快的打车 即刻领红包：'):
#    print word
#print urlExtractor(u'陌陌礼物商城，真实礼物传递线上心意。下载地址：http://t.cn/RZnQCW9')[1]
print ifBlackQuoteExtractor("【更多的接入设备给企业移动性带来更多挑战】Nemertes Research公司副总裁兼服务部总监Irwin Lazar讨论了关于移动办公的趋势，阐述了设备管理、内容管理、网络性能方面企业面临的挑战，并提供了克服困难的解决策略。")[0]