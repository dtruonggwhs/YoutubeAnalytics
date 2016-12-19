'''
Created on Dec 18, 2016

@author: DucTruong
'''
import pandas as pd


def MergeData():
    data1 = pd.read_csv('VideoStatistic_description.csv')
    data2 = pd.read_csv('VideoStatistic.csv')
    data3 = pd.read_csv('allChannelVideo.csv')
    data4 = pd.read_csv('VideoDuration.csv')
    data3 = data3[['categoryId','commentCount','likeCount','dislikeCount','viewCount']]
    data2 = data2[['videoId','tagcount','tagsentiment']]
    data1 = data1[['descriptioncount', 'descriptionsentiment']]
    data4 = data4[['duration']]
    mergedFrame = pd.concat([data1,data2,data3,data4],axis=1)
    print(mergedFrame)
    mergedFrame.to_csv('finalDataStatistic.csv')
    
MergeData()