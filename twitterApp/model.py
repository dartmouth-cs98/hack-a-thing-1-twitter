#!/usr/bin/env python3

import pandas, numpy, nltk
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
nltk.download('stopwords')


#################### Building the Model #######################

import re, string


#Tokenizing function
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
def tokenize(s): return re_tok.sub(r' \1 ', s).split()

# basic naive bayes feature equation
def bayes_feat_eq(y_i, y):
    p = x[y==y_i].sum(0)
    return (p+1) / ((y==y_i).sum()+1)

def get_mdl(y):
    y = y.values
    r = np.log(bayes_feat_eq(1,y) / bayes_feat_eq(0,y))
    m = LogisticRegression(C=4, dual=True)
    x_nb = x.multiply(r)
    return m.fit(x_nb, y), r


def model_train(train, test, subm):
    #According to tutorial, must fill out empty comments or thing complains
    COMMENT = 'comment_text'
    train[COMMENT].fillna("unknown", inplace=True)
    test[COMMENT].fillna("unknown", inplace=True)

    n = train.shape[0]

    # Getting and processing nltk stopwords corpus
    stopwords_nltk = nltk.corpus.stopwords.words('english')

    stopwords_processed = [tokenize(i) for i in stopwords_nltk]
    #ngrams = choose which n-grams to create
    #        because this is naive bayes, only looking at single words
    #use_idf = use inverse-doc-frequency weighting
    #smooth_idf  = prevents 0 divisions by pretending every word has a doc
    #controlling words:
    #   - min_df,max_df control word frequency
    #   - stop_words list from nltk
    vec = TfidfVectorizer (
        ngram_range=(1,2),
        tokenizer=tokenize,
        min_df=3,
        max_df=0.9,
        stop_words = stopwords_nltk,
        strip_accents='unicode',
        use_idf=1,
        smooth_idf=1,
        sublinear_tf=1 )

    # Get term-doc matrix
    trn_term_doc = vec.fit_transform(train[COMMENT])
    test_term_doc = vec.transform(test[COMMENT])


    trn_term_doc, test_term_doc
    print("\nLearning Naive Bayes result: term-doc-matrix\n")
    print(trn_term_doc)
    print("Learning Naive Bayes result: model \n\n")
    print(test_term_doc)

    x = trn_term_doc
    test_x = test_term_doc


    preds = np.zeros((len(test), len(label_cols)))

    for i, j in enumerate(label_cols):
        print('fit', j)
        m,r = get_mdl(train[j])
        preds[:,i] = m.predict_proba(test_x.multiply(r))[:,1]

    submid = pd.DataFrame({'id': subm["id"]})
    submission = pd.concat([submid, pd.DataFrame(preds, columns = label_cols)], axis=1)
    submission.to_csv('submission.csv', index=False)
