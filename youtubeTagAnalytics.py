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



csvFile = pd.read_csv('allChannelVideo.csv');
tagDistribution = csvFile['tags']
#print(tagDistribution)

allWords=''
for item in tagDistribution.iteritems():
    http_re = re.compile(r'\s+http://[^\s]*')
    https_re = re.compile(r'\s+https://[^\s]*')
    remove_ellipsis_re = re.compile(r'\.\.\.')
    at_sign_re = re.compile(r'\@\S+')
    punct_re = re.compile(r"[\"'\[\],.:;()\-&!]")
    price_re = re.compile(r"\d+\.\d\d")
    number_re = re.compile(r"\d+")
    remove_rt = re.compile(r"(rt)")
    remove_whitespace = re.compile(r"^\s+")
    emoji_pattern = re.compile("["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
#     if tweetText is None:
    cleanTags = emoji_pattern.sub(r'', item[1])
    cleanTags = re.sub(price_re, '', cleanTags)
    cleanTags = re.sub(remove_ellipsis_re, '', cleanTags)
    cleanTags = re.sub(http_re, '', cleanTags)
    cleanTags = re.sub(https_re, '', cleanTags)
    cleanTags = re.sub(punct_re, '', cleanTags)
    cleanTags = re.sub(at_sign_re, '', cleanTags)
    cleanTags = re.sub(number_re, '', cleanTags)
    cleanTags = re.sub(remove_rt,'',cleanTags)
    cleanTags = re.sub(remove_whitespace,'',cleanTags)
    cleanTags = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",cleanTags)
    tags = cleanTags.split(':')
    allWords =   allWords + ' '.join(tags)
    
#print(allWords)
# NLTK's default German stopwords
default_stopwords = set(nltk.corpus.stopwords.words('english'))

words = nltk.word_tokenize(allWords)

# Remove single-character tokens (mostly punctuation)
words = [word for word in words if len(word) > 1]

# Remove numbers
words = [word for word in words if not word.isnumeric()]

# Lowercase all words (default_stopwords are lowercase too)
words = [word.lower() for word in words]

# Stemming words seems to make matters worse, disabled
# stemmer = nltk.stem.snowball.SnowballStemmer('german')
# words = [stemmer.stem(word) for word in words]

# Remove stopwords
words = [word for word in words if word not in default_stopwords]

# Calculate frequency distribution
fdist = nltk.FreqDist(words)

#top50 = fdist.most_common(20)
# Output top 50 words

#print(top50)
top50list = {}

#for word, frequency in fdist.most_common(40):
for word, frequency in fdist.most_common(500):
    top50list[word]=frequency
    #print(u'{};{}'.format(word, frequency))

#print(top50list)
top50list.pop(' ', None)
top50list.pop('', None)
top50list.pop('\'s', None)
top50list.pop('\"', None)
top50list.pop('\'\'', None)
top50list.pop('"', None)

top50list_sorted = sorted(top50list.items(), key=itemgetter(1), reverse=True)
top50TagFreq = pd.DataFrame(top50list_sorted)
#print(top50TagFreq)
#top50list_sorted  = OrderedDict(sorted(top50list.items(), key=itemgetter(1), reverse=True))
top50TagFreq.to_csv('top500TagFreq.csv', index=False)
#top50TagFreq = pd.DataFrame.from_dict(top50list_sorted)
#print(top50TagFreq)
# top50list = sorted(top50list.items(), key=top50list.get)
# plt.bar(range(len(top50list_sorted)), top50list_sorted.values())
# plt.xticks(range(len(top50list_sorted)), top50list_sorted.keys())
# plt.xticks(rotation=90)
#      
#  # plt.plot(fdist.most_common(50))
# plt.show()

#print(words)
