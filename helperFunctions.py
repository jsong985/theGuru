#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:57:42 2018

@author: jsong985
"""

from nltk.corpus import wordnet

def wordnetPOS(posTag):
    if posTag.startswith('N') or posTag.startswith('P'):
        return wordnet.NOUN
    elif posTag.startswith('V'):
        return wordnet.VERB
    elif posTag.startswith('J'):
        return wordnet.ADJ
    elif posTag.startswith('R'):
        return wordnet.ADV
    else:
        return 'No WordNet equivalent'