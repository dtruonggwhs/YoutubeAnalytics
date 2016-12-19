'''
Created on Nov 20, 2016

@author: DucTruong
'''

'''
Created on Nov 13, 2016

@author: DucTruong
'''
import numpy as np
import pandas as pd
import isodate
from collections import Counter


csvFile = pd.read_csv('allChannelVideo.csv');
videoDuration = csvFile['videoDuration']
videoDurationLike = csvFile[['videoDuration','likeCount']]
#print(videoDuration)
videoDurationLikeSorted = videoDurationLike.sort('likeCount', ascending=False)
top50videoDurationLike = pd.DataFrame(videoDurationLikeSorted[:1000])
#print(top50videoDurationLike['videoDuration'])
# #video duration frequency
# durationList = []
# for item in videoDuration.iteritems():
#     formattedDuration=isodate.parse_duration(item[1])
#     #print(isodate.time_isoformat(formattedDuration, "%M"))
#     durationList.append(isodate.time_isoformat(formattedDuration, "%M"))
# 
# listCount = Counter(durationList)
# top10Duration = pd.DataFrame(listCount.most_common(10))
# top10Duration.to_csv('top10Duration.csv', index=False)

#video duration and likes
durationList = []
for index, row in top50videoDurationLike.iterrows():
    formattedDuration=isodate.parse_duration(row['videoDuration'])
    formattedDuration2 = isodate.time_isoformat(formattedDuration, "%M")
    durationList.append(formattedDuration2)
    #print(formattedDuration2, row['likeCount'])
#     print(isodate.time_isoformat(formattedDuration, "%M"))
#     durationList.append(isodate.time_isoformat(formattedDuration, "%M"))
listCount = Counter(durationList)
print(listCount)
# top10LikedDuration = pd.DataFrame(listCount.most_common(10))
# top10LikedDuration.to_csv('topLikedDuration.csv', index=False)
# listCount = Counter(durationList)
# top10Duration = pd.DataFrame(listCount.most_common(10))
# top10Duration.to_csv('top10Duration.csv', index=False)

