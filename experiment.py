__author__ = 'zhuangli'
# -*- coding: utf-8 -*-
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
import jieba.analyse
#segmenter = StanfordSegmenter(path_to_jar="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/stanford-segmenter-3.4.1.jar",path_to_sihan_corpora_dict="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data", path_to_model="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data/pku.gz", path_to_dict="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data/dict-chris6.ser.gz")
#sentence = u"我在澳洲国立大学读书"
#seg=segmenter.segment(sentence)

#st = StanfordNERTagger('/Users/zhuangli/PycharmProjects/Weibo/stanford-ner-2015-04-20/classifiers/stanford-chinese-corenlp-2015-04-20-models/edu/stanford/nlp/models/ner/chinese.misc.distsim.crf.ser.gz','/Users/zhuangli/PycharmProjects/Weibo/stanford-ner-2015-04-20/stanford-ner.jar')
#print st.tag(seg.split())
s = "我擦！！！@京东 上卖的这个平板支架货不对版，说明中说最大尺寸可拉伸至24.5，实际上22不到。刚好我准备夹上去的一个平板无法容纳，差了1厘米！！！[怒][怒][怒] http://t.cn/RPWR1E4"
for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))
from datetime import datetime

base_date = "2015-01-01"
data = ["2015-01-23", "2015-01-04", "2015-01-03"]
format = "%Y-%m-%d"

base = datetime.strptime(base_date, format)
print base
diff = [(datetime.strptime(d, format) - base).days for d in data]
print diff
feature={}
feature[u"天才"]=1
if u"天才" in feature:
    print u"天才"
