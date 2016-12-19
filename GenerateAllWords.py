'''
Created on Dec 18, 2016

@author: DucTruong
'''
import pandas as pd 

def GetAllWordList():
    data = pd.read_csv('popularkeywords.csv')
    
    allwordList = []
    for index, row in data.iterrows():
        allwordList.append(row[0])
    return allwordList