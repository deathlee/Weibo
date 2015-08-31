__author__ = 'zhuangli'
from sklearn.datasets import load_svmlight_file
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import sys
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
def polynomialRegression(train_file,predict_file,res):
    X_train, y_train = load_svmlight_file(train_file)
    X_test,y_test=load_svmlight_file(predict_file,n_features=X_train.shape[1])
    #X_train1=vectorizer.fit_transform(X_train.astype(str))
    #X_test1=vectorizer.transform(X_test.astype(str))
    #print X_train.shape
    #print X_train
    """
    clf = linear_model.LinearRegression()
    clf.fit(X_train,y_train)
    y=clf.predict(X_test)
    """
    model = make_pipeline(PolynomialFeatures(2))
    model.fit(X_train.todense(), y_train)
    y = model.predict(X_test.todense())

    for i in y:
        with open(res, "a") as myfile:
            myfile.write(str(i)+' ')
if __name__ == "__main__":
    if sys.argv[1]=='comment':
        polynomialRegression("data/comment_tune","data/final_test","data/predictComment")
    elif sys.argv[1]=='forward':
        polynomialRegression("data/forward_tune","data/final_test","data/predictForward")
    elif sys.argv[1]=='like':
        polynomialRegression("data/like_tune","data/final_test","data/predictLike")
    elif sys.argv[1]=='test':
        polynomialRegression("data/tune_test","data/test_predict","data/tempRes")