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
def bayes_feat_eq(y_i, y,termDocMatrix):
    p = termDocMatrix[y==y_i].sum(0)
    #smoothing???
    return (p+1) / ((y==y_i).sum()+1)


def get_mdl(y,termDocMatrix):
    y = y.values
    r = numpy.log(bayes_feat_eq(1,y,termDocMatrix) / bayes_feat_eq(0,y,termDocMatrix))
    m = LogisticRegression(C=4, dual=True)
    x_nb = termDocMatrix.multiply(r)
    return m.fit(x_nb, y), r


def model_train(train, test, subm, categories):
    #According to tutorial, must fill out empty comments or thing complains
    COMMENT = 'comment_text'
    train[COMMENT].fillna("unknown", inplace=True)
    test[COMMENT].fillna("unknown", inplace=True)

    n = train.shape[0]

    #### Getting and processing nltk stopwords corpus
    stopwords_nltk = nltk.corpus.stopwords.words('english')
    #stopwords_processed = [tokenize(i) for i in stopwords_nltk]

    #### Create TF-IDF matrix
    ## This gives better priors fr BAyes feature equation, not sure why though.
    ## This create an inverse term-doc matrix with frquency of a word in the corpus.

    ##Using TfidVectorizer
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
    #The tuple represents: (document_id, token_id)
    #The value following the tuple represents the tf-idf score of a given token in a given document
    print(trn_term_doc[:100])
    print("First 100 feature names:\n")
    print(vec.get_feature_names()[:100])


    x = trn_term_doc
    test_x = test_term_doc

    # Return an array, preds, of the following shape filled with zeros
    preds = numpy.zeros((len(test), len(categories)))

    # Train the model on each category with priors from TD-IDF and others
    #i is the index of the category, while j is the category itself
    for i, j in enumerate(categories):
        print('fit', j)
        #get the hyperplane
        m,r = get_mdl(train[j],x)
        #fill in predicate list
        preds[:,i] = m.predict_proba(test_x.multiply(r))[:,1]

    submid = pandas.DataFrame({'id': subm["id"]})
    submission = pandas.concat([submid, pandas.DataFrame(preds, columns = categories)], axis=1)
    submission.to_csv('submission.csv', index=False)
