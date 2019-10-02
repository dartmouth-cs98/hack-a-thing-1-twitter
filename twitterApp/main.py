#!/usr/bin/env python3
'''
Main program, calls other modules
- dataset : to read and parse the dataset
- model : to train and respond to the model

'''

import dataset, model

train, test, subm, categories = dataset.read_dataset()

cat_info, test_x = model.model_train(train, test, subm, categories)
model.model_read_input(test_x, categories, cat_info)
