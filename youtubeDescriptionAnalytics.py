'''
Created on Nov 13, 2016

@author: DucTruong
'''
import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
import re
#import matplotlib.pyplot as plt
#import plotly.plotly as py
from collections import OrderedDict
from operator import itemgetter
import isodate


csvFile = pd.read_csv('allChannelVideo.csv');
descriptionDistribution = csvFile['description']
print(descriptionDistribution)

allWords=''
for item in descriptionDistribution.iteritems():
    
    emoji_pattern = re.compile("["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    
    # Remove single-character tokens (mostly punctuation)
    tweets = [tweet for tweet in item[1] if len(tweet) > 1]
    
    # Remove numbers
    tweets = [tweet for tweet in tweets if not tweet.isnumeric()]
    
    # Lowercase all words (default_stopwords are lowercase too)
    tweets = [tweet.lower() for tweet in tweets]
    print(tweets)
#     cleanWords = emoji_pattern.sub(r'', )
#     cleanWords = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', cleanWords, flags=re.MULTILINE)
#     print(cleanWords.encode('utf-8'))
    #tags = cleanTags.split(':')
    #allWords =   allWords + ' '.join(cleanWords)
    