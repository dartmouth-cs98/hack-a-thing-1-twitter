#!/usr/bin/env python3
'''
Main program, calls other modules
- dataset : to read and parse the dataset
- model : to train and respond to the model

'''

import dataset, model

train, test, subm = dataset.read_dataset()

model.model_train(train)
