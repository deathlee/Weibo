__author__ = 'zhuangli'
def PrintResult(commentPath,forwardPath,likePath,predictPath):
    comment = open(commentPath, 'r')
    for line in comment:
        commentList=line.split(" ")
    forward=open(forwardPath, 'r')
    for line in forward:
        forwardList=line.split(" ")
    like=open(likePath, 'r')
    for line in like:
        likeList=line.split(" ")
    predict=open(predictPath, 'r')
    idx=0
    for line in predict:
        stringLine=""
        predictList=line.split("\t")
        commentvalue=commentList[idx] if float(commentList[idx])>=0 else '0.0'
        forwardvalue=forwardList[idx] if float(forwardList[idx])>=0 else '0.0'
        likevalue=likeList[idx] if float(likeList[idx])>=0 else '0.0'
        stringLine+=predictList[0]+"\t"+predictList[1]+"\t"+forwardvalue+","+commentvalue+","+likevalue
        idx+=1
        with open("data/weibo_result_data", "a") as myfile:
            myfile.write(stringLine+'\n')
PrintResult("data/predictComment","data/predictForward","data/predictLike","data/weibo_predict_data.txt")