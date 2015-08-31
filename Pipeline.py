__author__ = 'zhuangli'
# -*- coding: utf-8 -*-
from DataObj import  RawData
from DataObj import  Label
import re
import sys
import jieba.analyse
from nltk.parse import stanford
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
# -*- coding: utf-8 -*-
sys.path.append("./Chinese-Sentiment/Sentiment_features/Sentiment_dictionary_features")
sys.path.append("./Chinese-Sentiment/Preprocessing_module")
import pos_neg_senti_dict_feature as pn
import textprocessing as tp
from datetime import datetime
from numpy import *

def timeProcess(train_path,predict_path):
    train_f = open(train_path, 'r')
    maxTime=-sys.maxint - 1
    minTime=sys.maxint
    for line in train_f:
        values=line.split("\t")
        tmp=dateExtractor(values[2])
        if tmp >maxTime:
            maxTime=tmp
        if tmp<minTime:
            minTime=tmp
    train_f.close()
    predict_f = open(predict_path, 'r')
    for line in predict_f:
        values=line.split("\t")
        tmp=dateExtractor(values[2])
        if tmp >maxTime:
            maxTime=tmp
        if tmp<minTime:
            minTime=tmp
    predict_f.close()
    gap=maxTime-minTime
    return minTime,gap
def pipeline(train_path,predict_path,minTime,gap):
    features={}
    train_f = open(train_path, 'r')
    fidx=4
    for line in train_f:
        values=line.split("\t")
        stringLine=""
        data=RawData(values[0],values[1],double(dateExtractor(values[2])-minTime)/double(gap),values[6])
        labels=Label(values[3],values[4],values[5])
        forwardString="".join(str(labels.forward_count)+" "+ str(0)+":"+str(data.time)+" ")
        commentString="".join(str(labels.comment_count)+" "+ str(0)+":"+str(data.time)+" ")
        likeString="".join(str(labels.like_count)+" "+ str(0)+":"+str(data.time)+" ")
        fidx,stringLine=uidExtractor(data.uid,features,fidx,stringLine)
        fidx,stringLine=featureExtractor(data.content.decode('utf-8'),features,fidx,stringLine)
        forwardString+=stringLine
        commentString+=stringLine
        likeString+=stringLine
        with open("data/forward.data", "a") as myfile:
            myfile.write(forwardString+'\n')
        with open("data/comment.data", "a") as myfile:
            myfile.write(commentString+'\n')
        with open("data/like.data", "a") as myfile:
            myfile.write(likeString+'\n')
    train_f.close()
    predict_f = open(predict_path, 'r')
    for line in predict_f:
        stringLine=""
        values=line.split("\t")
        data=RawData(values[0],values[1],double(dateExtractor(values[2])-minTime)/double(gap),values[3])
        fidx,stringLine=uidExtractor(data.uid,features,fidx,stringLine)
        fidx,stringLine=featureExtractor(data.content.decode('utf-8'),features,fidx,stringLine)
        stringLine=str(0)+":"+str(data.time)+" "+stringLine
        with open("data/test.data", "a") as myfile:
            myfile.write(stringLine+'\n')
    predict_f.close()
def uidExtractor(uid,features,fidx,stringLine):
    if uid in features:
        stringLine=stringLine+str(features[uid])+":"+str(1)+" "
    else:
        features[uid]=fidx
        stringLine=stringLine+str(fidx)+":"+str(1)+" "
        fidx+=1
    return fidx,stringLine
def dateExtractor(date):
    format = "%Y-%m-%d"
    base = datetime.strptime(base_date, format)
    return (datetime.strptime(date, format) - base).days
def featureExtractor(sentence,features,fidx,stringLine):
    if sentimentExtractor(sentence):
        stringLine=stringLine+str(1)+":"+str(1)+" "
    if ifBlackQuoteExtractor(sentence):
        stringLine=stringLine+str(2)+":"+str(1)+" "
    if ifQuoteExtractor(sentence):
        stringLine=stringLine+str(3)+":"+str(1)+" "
    actList=activityExtractor(sentence)
    for act in actList:
        if act in features:
            stringLine=stringLine+str(features[act])+":"+str(1)+" "
        else:
            features[act]=fidx
            stringLine=stringLine+str(fidx)+":"+str(1)+" "
            fidx+=1
    urlList=urlExtractor(sentence)
    for url in urlList:
        if url in features:
            stringLine=stringLine+str(features[url])+":"+str(1)+" "
        else:
            features[url]=fidx
            stringLine=stringLine+str(fidx)+":"+str(1)+" "
            fidx+=1
    atList=atExtractor(sentence)
    for at in atList:
        if at in features:
            stringLine=stringLine+str(features[at])+":"+str(1)+" "
        else:
            features[at]=fidx
            stringLine=stringLine+str(fidx)+":"+str(1)+" "
            fidx+=1
    keyList=keyWordExtractor(sentence)
    for keyWord in keyList:
        if keyWord in features:
            stringLine=stringLine+str(features[keyWord])+":"+str(1)+" "
        else:
            features[keyWord]=fidx
            stringLine=stringLine+str(fidx)+":"+str(1)+" "
            fidx+=1
    return fidx,stringLine
def activityExtractor(sentence):
    return re.findall("#.*#", sentence, re.I)
    #,re.sub("@", '', sentence)
def urlExtractor(sentence):
    return re.findall("http\S+", sentence, re.I)
    #,re.sub("http\S+", '', sentence)
def atExtractor(sentence):
    return re.findall("@.*\\s", sentence, re.I)
    #,re.sub("#", '', sentence)
def sentimentExtractor(sentence):
    list=pn.single_review_sentiment_score(sentence)
    if list[0]>list[1]:
        return True
    else:
        return False
def ifBlackQuoteExtractor(sentence):
    flag=False
    if re.findall(r"【.*】",sentence):
        flag=True
    return flag
    #,re.sub("】", '', re.sub("【", '', sentence))
def ifQuoteExtractor(sentence):
    flag=False
    if re.findall(r"\[.+\]",sentence):
        flag=True
    return flag
    #,re.sub("\[", '', re.sub("\]", '', sentence))
def keyWordExtractor(sentence):
    list=[]
    for x, w in jieba.analyse.textrank(sentence, withWeight=True):
        list.append(x)
    return list
"""
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
"""
"""
segmenter = StanfordSegmenter(path_to_jar="./stanford-segmenter-2014-08-27/stanford-segmenter-3.4.1.jar",path_to_sihan_corpora_dict="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data", path_to_model="./stanford-segmenter-2014-08-27/data/pku.gz", path_to_dict="./stanford-segmenter-2014-08-27/data/dict-chris6.ser.gz")
st = StanfordNERTagger('./stanford-ner-2015-04-20/classifiers/stanford-chinese-corenlp-2015-04-20-models/edu/stanford/nlp/models/ner/chinese.misc.distsim.crf.ser.gz','./stanford-ner-2015-04-20/stanford-ner.jar')
"""
base_date = "2015-01-01"
minTime,gap = timeProcess("data/weibo_train_data.txt","data/weibo_predict_data.txt")
pipeline("data/weibo_train_data.txt","data/weibo_predict_data.txt",minTime,gap)
#featureExtractor(data)
#for word in mentionExtractor(u' 【Socket.IO：支持WebSocket协议、用于实时通信和跨平台的框架】Socket.IO是完全由JavaScript实现、基于Node.js、支持WebSocket的协议用于实时通信、跨平台的开源框架，其目标是构建能在不同浏览器和移动设备上使用的实时应用，如在线聊天室、在线客服系统、评论系统、WebIM等'):
#    print word
#print urlExtractor(u'陌陌礼物商城，真实礼物传递线上心意。下载地址：http://t.cn/RZnQCW9')[1]
#for word in keyWordExtractor(u"Google 出品的 Year in Search 2014 真心 Amazing 啊！来自 Porter Robinson 的 Divinity 作为 Soundtrack 真心 Amazing~ 推荐一个~ "):
#    print word.encode('utf-8')
#print dateExtractor("2015-01-03")
#print val[0]
#print val[1]