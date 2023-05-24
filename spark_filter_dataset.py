'''
Team Members: Sanskar Sehgal, Akhilesh Boppana, Vivek Golani, Nikhil Desha
This code filters relevant data for our project based on selected subreddits. It filters from the 15GB reddit-covid-dataset.   
Framewordks: PySpark
Concepts: Transformations and Actions in PySpark
System: Macbook Air M2
Code written by - Sanskar Sehgal
'''




# Import necessary modules
from pyspark import SparkContext, SparkConf



def create_key_val_pairs(row):
    vals = row.split(',')
    if len(vals) != 12:
        return ()
    return (vals[3], (vals[5], vals[9], vals[10])) 

# Create a SparkContext object
sc = SparkContext()
conf = SparkConf().setAppName("Filter Data")

# Load data as a csv file
data_rdd = sc.textFile('/Users/sanskarsehgal/Desktop/Big Data/Project/archive/the-reddit-covid-dataset-posts.csv')

# Filter data based on certain subreddits
subreddits = ['addiction', 'alcoholism', 'REDDITORSINRECOVERY', 'stopdrinking','OpiatesRecovery', 
              'addictionrecovery', 'addictedtotheneedle','leaves', 'cocaine', 'StopSpeeding', 
              'redditorsinrecovery','Sober','alcoholicsanonymous', 'NarcoticsAnonymous', 
             'benzorecovery', 'dryalcoholics', 'mentalhealth','depression','anxiety', 'bipolar',
              'ADHD','OCD','PTSD','psychology','therapy', 'mentalillness',
              'SuicideWatch','EatingDisorders','HealthAnxiety','insomnia','mentalhealthsupport']

# filtered_data = data.filter(data.subreddit.isin(subreddits))
header = data_rdd.first() # Read header
data_rdd = data_rdd.filter(lambda x: x != header) # Filter out header
split_data_rdd = data_rdd.map(lambda x: create_key_val_pairs(x))
filtered_rdd = split_data_rdd.filter(lambda x: len(x) != 0 and x[0] in subreddits)
filtered_rdd.saveAsTextFile('/Users/sanskarsehgal/Desktop/Big Data/Project/reddit_data')

