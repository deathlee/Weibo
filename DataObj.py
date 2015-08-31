__author__ = 'zhuangli'
class RawData:
    def __init__(self,uid,mid,time,content):
        self.uid=uid
        self.mid=mid
        self.time=time
        self.content=content
class Label:
    def __init__(self,forward_count,comment_count,like_count):
        self.forward_count=forward_count
        self.comment_count=comment_count
        self.like_count=like_count
class DataFeature:
    def __init__(self,uid,mid,time,contentlength,hashTag,url,at,sentiment,facenum,activity,rightPeople,mention,forward_count,comment_count,like_count):
        self.uid=uid
        self.mid=mid
        self.time=time
        self.contentlength=contentlength
        self.hashTag=hashTag
        self.url=url
        self.at=at
        self.facenum=facenum
        self.activity=activity
        self.sentiment=sentiment
        self.mention = mention
        self.rightPeople=rightPeople
        self.forward_count=forward_count
        self.comment_count=comment_count
        self.like_count=like_count