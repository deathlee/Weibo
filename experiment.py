__author__ = 'zhuangli'
# -*- coding: utf-8 -*-
from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
segmenter = StanfordSegmenter(path_to_jar="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/stanford-segmenter-3.4.1.jar",path_to_sihan_corpora_dict="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data", path_to_model="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data/pku.gz", path_to_dict="/Users/zhuangli/PycharmProjects/Weibo/stanford-segmenter-2014-08-27/data/dict-chris6.ser.gz")
sentence = u"我在澳洲国立大学读书"
seg=segmenter.segment(sentence)

st = StanfordNERTagger('/Users/zhuangli/PycharmProjects/Weibo/stanford-ner-2015-04-20/classifiers/stanford-chinese-corenlp-2015-04-20-models/edu/stanford/nlp/models/ner/chinese.misc.distsim.crf.ser.gz','/Users/zhuangli/PycharmProjects/Weibo/stanford-ner-2015-04-20/stanford-ner.jar')
print st.tag(seg.split())