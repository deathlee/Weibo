__author__ = 'zhuangli'
from sklearn.datasets import load_svmlight_file
X_train, y_train = load_svmlight_file("data/comment_test")
print X_train
print y_train