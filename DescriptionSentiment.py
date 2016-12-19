'''
Created on Dec 18, 2016
@author: DucTruong
'''
import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
# nltk.download('vader_lexicon')
# nltk.download('wordnet')
# nltk.download()
from nltk.corpus import wordnet as wn
from nltk.tokenize import WordPunctTokenizer
from GenerateAllWords import GetAllWordList


allword = GetAllWordList()

def normalize_tweet(tweet):
    http_re = re.compile(r'\s+http://[^\s]*')
    https_re = re.compile(r'\s+https://[^\s]*')
    remove_ellipsis_re = re.compile(r'\.\.\.')
    at_sign_re = re.compile(r'\@\S+')
    punct_re = re.compile(r"[\"'\[\],.:;()\-&!]")
    price_re = re.compile(r"\d+\.\d\d")
    number_re = re.compile(r"\d+")
    remove_rt = re.compile(r"(rt)")
    remove_whitespace = re.compile(r"^\s+")
    t = tweet.lower()
    t = re.sub(price_re, '', t)
    t = re.sub(remove_ellipsis_re, '', t)
    t = re.sub(http_re, '', t)
    t = re.sub(https_re, '', t)
    t = re.sub(punct_re, '', t)
    t = re.sub(at_sign_re, '', t)
    t = re.sub(number_re, '', t)
    t = re.sub(remove_rt,'',t)
    t = re.sub(remove_whitespace,'',t)
    t = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",t)
    emoji_pattern = re.compile("["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
#     if tweetText is None:
    t = emoji_pattern.sub(r'', t)
    return t

def sentimentAnalysis(fileName):
    tknzr = WordPunctTokenizer()
    data = pd.read_csv(fileName)
#     data = data[:5500]
#     englishOnly = pd.DataFrame(data.loc[data['language'] == "en"])
#     removedDuplicate = data['tags'].drop_duplicates("first")
    
    allTweetSentence = []
    descriptionInAllWord = []
    descriptionSentiment = []
    for index,row in data.iterrows():
        filterForDescription = row['description']
        cleanTweet = normalize_tweet(filterForDescription)
        if len(cleanTweet) > 0:
            allTweetSentence.append(cleanTweet)
    
    # allTweetSentence.remove("")
    #print(allTweetSentence)
    # 
    sid = SentimentIntensityAnalyzer()
    for sentence in allTweetSentence:
        recognizedText = []
        decode_sentence = sentence.strip()
#         print(decode_sentence[1:])
        tokenizedTag = tknzr.tokenize(sentence[1:])
        #print(nltk.pos_tag(tokenizedTag))
        descriptionInAllWordCount = 0
        for t in tokenizedTag:
            if wn.synsets(t):
                recognizedText.append(t)
        for word in recognizedText:
            if word in allword:
                descriptionInAllWordCount = descriptionInAllWordCount + 1
#         print(tagInAllWord)
        ss = sid.polarity_scores(decode_sentence[1:])
        ss.pop('compound', None)
        if max(ss, key=ss.get)=='neu':
            descriptionSentiment.append(0)
        elif max(ss, key=ss.get)=='pos':
            descriptionSentiment.append(1)
        else:
            descriptionSentiment.append(2)
        descriptionInAllWord.append(descriptionInAllWordCount)
        #print(tagInAllWord, max(ss, key=ss.get))
    mergeData = pd.DataFrame({'descriptioncount':descriptionInAllWord,'descriptionsentiment':descriptionSentiment})
    print(mergeData)
#     mergedFrame = pd.concat(mergeData)
    mergeData.to_csv('VideoStatistic_description_2.csv')

sentimentData = sentimentAnalysis('allChannelVideo.csv')
# print(sentimentData)
