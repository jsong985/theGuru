#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 16:55:45 2018

@author: jsong985
"""

import helperFunctions as hf
import nltk

# Get query
query = "The quick brown fox jumps over the lazy dog."

# Break up into words
wordList = nltk.word_tokenize(query)

# Lemmatize words
posList = nltk.pos_tag(wordList)
wnLemmatizer = nltk.WordNetLemmatizer()
for idx, word in enumerate(wordList):
    try:
        wordList[idx] = wnLemmatizer.lemmatize(word, pos=hf.wordnetPOS(posList[idx][1]))
    except:
        continue

print(wordList)