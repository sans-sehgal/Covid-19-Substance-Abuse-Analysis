'''
This code classifies our posts into [ritical, major, moderate, minor, cosmetic] using a transformer based zero-shot classification model  
Framewordks: Pytorch
Concepts: Transformers
System: Macbook Air M2
Code written by - Sanskar Sehgal
'''


from transformers import pipeline
import pandas as pd
import pickle
import praw
import datetime as dt
import glob
import math
import nltk
from nltk import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import seaborn as sns
import torch
from transformers import pipeline

# Load the zero-shot classification pipeline
classifier = pipeline("zero-shot-classification",
                      model="AIMH/mental-xlnet-base-cased")

directory_path = '/Users/sanskarsehgal/Desktop/Big Data/Project/Reddit Substance Abuse'
for file in glob.glob(directory_path + '/*'):
    if file[-5:] != 'ipynb' and file[-3:] != 'csv' and file[-3:] != 'pkl' and file[-2:] != 'py':
        print(file)
        critical = []
        major = []
        moderate = []
        minor = []
        cosmetic = []

        df = pd.read_csv(file)
        labels = ['critical', 'major', 'moderate','minor', 'cosmetic']
        for i in df.index:
            if (not pd.isna(df['Post Text'][i])) and (not pd.isna(df['Title'][i])):
                sequence_to_classify = str(df['Title'][i]) + " " + str(df['Post Text'][i])
            else: 
                if pd.isna(df['Post Text'][i]):
                    sequence_to_classify = df['Title'][i]
                elif pd.isna(df['Title'][i]):
                    sequence_to_classify = df['Post Text'][i]
                
            output = classifier(sequence_to_classify, labels)
            print(output)
            for j in range(len(output['labels'])):
                if output['labels'][j] == 'critical':
                    critical.append(output['scores'][j])
                elif output['labels'][j] == 'major':
                    major.append(output['scores'][j])
                elif output['labels'][j] == 'moderate':
                    moderate.append(output['scores'][j])
                elif output['labels'][j] == 'minor':
                    minor.append(output['scores'][j])
                elif output['labels'][j] == 'cosmetic':
                    cosmetic.append(output['scores'][j])
        
            if i % 100 == 0:
                print(i)
        df['critical'] = critical
        df['major'] = major
        df['moderate'] = moderate
        df['minor'] = minor
        df['cosmetic'] = cosmetic
        df.to_csv(file + '.csv')
            
