'''
Created on Dec 18, 2016

@author: DucTruong
'''
import pandas as pd
import isodate

data = pd.read_csv('allChannelVideo.csv');

data = data[['video_id','videoDuration']]

durationList = []
videoid = []
for index, row in data.iterrows():
    formattedDuration=isodate.parse_duration(row['videoDuration'])
    formattedDuration2 = isodate.time_isoformat(formattedDuration, "%M")
    durationList.append(formattedDuration2)
    videoid.append(row['video_id'])
    
finalFrame = pd.DataFrame({'videoid': videoid,'duration':durationList})
finalFrame.to_csv('VideoDuration.csv')
    
