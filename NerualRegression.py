__author__ = 'zhuangli'
from sklearn.datasets import load_svmlight_file
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from pybrain.datasets import SupervisedDataSet
from pybrain.datasets import UnsupervisedDataSet
import numpy, math
import sys
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
def polynomialRegression(train_file,predict_file,res):
    X_train, y_train = load_svmlight_file(train_file)
    dim=X_train.shape[1]
    X_test,y_test=load_svmlight_file(predict_file,n_features=X_train.shape[1])
    train = SupervisedDataSet(dim, 1)
    test=UnsupervisedDataSet(dim)
    trainM=X_train.todense()

    for x, y in zip(trainM, y_train):
        train.addSample(x, y)
    testM=X_test.todense()
    for x in testM:
        test.addSample(x)
    from pybrain.structure import SigmoidLayer, LinearLayer
    from pybrain.tools.shortcuts import buildNetwork
    print X_train.shape[1]
    net = buildNetwork(dim,
                   100, # number of hidden units
                   1,
                   bias = True,
                   hiddenclass = SigmoidLayer,
                   outclass = LinearLayer
                   )
#----------
# train
#----------
    from pybrain.supervised.trainers import BackpropTrainer
    trainer = BackpropTrainer(net, train, verbose = True)
    trainer.trainUntilConvergence(maxEpochs = 100)

#----------
# evaluate
#----------
    result=[]
    for x in testM:
        result.append(net.activate(np.asarray(x).flatten())[0])
    print result
    print y_train
    for i in result:
        with open(res, "a") as myfile:
            myfile.write(str(i)+' ')
if __name__ == "__main__":
    if sys.argv[1]=='comment':
        polynomialRegression("data/filterComment","data/filterTest","data/predictCommentNerual")
    elif sys.argv[1]=='forward':
        polynomialRegression("data/filterForward","data/filterTest","data/predictForwardNerual")
    elif sys.argv[1]=='like':
        polynomialRegression("data/filterLike","data/filterTest","data/predictLikeNerual")
    elif sys.argv[1]=='test':
        polynomialRegression("data/tune_test","data/test_predict","data/tempRes")