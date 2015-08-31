__author__ = 'zhuangli'
from sklearn.datasets import load_svmlight_file
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
from sklearn.feature_selection import VarianceThreshold
from sklearn.feature_selection import RFE
def sortTrainData(train_path,tune_path):
    train_f = open(train_path, 'r')
    count=0
    for line in train_f:
        feature={}
        cells=line.strip().split(" ")
        stringline=cells[0]+" "
        for i in range(1,len(cells)):
            key,value=cells[i].split(":")
            feature[int(key)]=value
        for key in sorted(feature):
            stringline+= (str(key)+":"+feature[key]+" ")
        with open(tune_path, "a") as myfile:
            myfile.write(stringline+"\n")
        print count
        count+=1
def sortTestData(predict_path,tune_path):
    predict_f = open(predict_path, 'r')
    count=0
    for line in predict_f:
        feature={}
        cells=line.strip().split(" ")
        stringline="0"+" "
        for i in range(0,len(cells)):
            key,value=cells[i].split(":")
            feature[int(key)]=value
            print key
        for key in sorted(feature):
            stringline+= (str(key)+":"+feature[key]+" ")
        with open(tune_path, "a") as myfile:
            myfile.write(stringline+"\n")
        print count
        count+=1
def modifyTest(train_path,predict_path,modify_path):
    train_f = open(train_path, 'r')
    feature=set()
    for line in train_f:
        cells=line.strip().split(" ")
        for i in range(1,len(cells)):
            key,value=cells[i].split(":")
            feature.add(key)
    predict_f = open(predict_path, 'r')
    count=0
    for line in predict_f:
        cells=line.strip().split(" ")
        stringline=cells[0]+" "
        for i in range(1,len(cells)):
            key,value=cells[i].split(":")
            if key in feature:
                stringline+= (key+":"+value+" ")
        with open(modify_path, "a") as myfile:
            myfile.write(stringline+"\n")
        count+=1
modifyTest("data/comment.data","data/test_tune","data/final_test")
#sortTrainData("data/comment.data","data/comment_tune")
#sortTrainData("data/forward.data","data/forward_tune")
#sortTrainData("data/like.data","data/like_tune")
#sortTestData("data/test.data","data/test_tune")
def featureSelector(train_path,predict_path):
    X, y = load_svmlight_file("data/comment_test")
    Xt, yt = load_svmlight_file("data/test_predict")
    estimator = SVR(kernel="linear")
    selector = RFE(estimator, step=1)
    newX = selector.fit(X, y)
    newtX=selector.transform(Xt)
    print newtX

    """
    sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
    newX=sel.fit_transform(X)
    print newX
    """
#featureSelector("","")