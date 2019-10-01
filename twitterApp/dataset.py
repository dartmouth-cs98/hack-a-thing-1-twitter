#!/usr/bin/env python3

import pandas, numpy, nltk
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def read_dataset():
    #categories for labeling the Bayes Model
    categories = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

    #Use pandas to get csv data, turns into dataframe
    train = pandas.read_csv('../jigsaw/train.csv')
    test = pandas.read_csv('../jigsaw/test.csv')
    subm = pandas.read_csv('../jigsaw/sample_submission.csv')

    #to show data
    print("Here is an example entry: \n")
    print(train['comment_text'][1])
    print("\n\n")
    #describe generate states that summerize the shape of the datasets distribution
    #the dataset is using the labels above as categories
    train['none'] = 1-train[categories].max(axis=1)
    print('Here is information about the toxic comments dataset:\n')

    print(train.count())
    print(train.describe(include='all'))


    return train, test, subm, categories
