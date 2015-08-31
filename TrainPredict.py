__author__ = 'zhuangli'
from PyML import *
from PyML.classifiers.svm import SVR
import sys
def train(trainfile,tempRes,predictFile):
    s=SVR()
    data = SparseDataSet(trainfile,numericLabels = True)
    s.train(data)
    s.save(tempRes)
    new_svm = SVR()
    new_svm.load(tempRes, data)
    test_data=SparseDataSet("data/test.data",numericLabels = True)
    results = new_svm.test(test_data)
    for i in results:
        for predict in i.Y:
            with open(predictFile, "a") as myfile:
                myfile.write(str(predict)+' ')
if __name__ == "__main__":
    if sys.argv[1]=='comment':
        train("data/comment.data","data/tempResComment","data/predictComment")
    elif sys.argv[1]=='forward':
        train("data/forward.data","data/tempResForward","data/predictForward")
    elif sys.argv[1]=='like':
        train("data/like.data","data/tempResLike","data/predictLike")
