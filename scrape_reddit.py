'''
Team Members: Sanskar Sehgal, Akhilesh Boppana, Vivek Golani, Nikhil Desha
This code scrapes data from relevant subreddits and is added to our previously filtered dataset     
Framewordks: 
Concepts: 
System: Macbook Air M2
Code written by - Sanskar Sehgal
'''

import praw
import datetime


# Enter your Reddit API credentials
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

# Specify the subreddit name and time frame to scrape posts from
subreddits = []


for subreddit_name in subreddits:
    subreddit = reddit.subreddit(subreddit_name)
    posts = subreddit.top(time_filter = "all", limit = None)
    print(subreddit_name)
    start_date = '01-01-18 00:00:00'
    start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()
    
    posts_dict = {"ID": [], 
                  "Title": [], 
                  "Post Text": [],
                  "Score": [], 
                  "Created On":[]
                 }

    # Get the subreddit and limit the number of posts to retrieve
    count = 0
    
    # Loop through each post and print out the title, score, and date/time created
    for post in posts:
        
        date = post.created_utc
        if date > start_date:
            
           
            created = dt.datetime.fromtimestamp(post.created_utc)
            posts_dict["Title"].append(post.title)

            # Text inside a post
            posts_dict["Post Text"].append(post.selftext)

            # Unique ID of each post
            posts_dict["ID"].append(post.id)

            # The score of a post
            posts_dict["Score"].append(post.score)

            # Date the post was Created
            posts_dict["Created On"].append(created)

            count += 1

    print(count)
    df = pd.DataFrame(posts_dict)
    df.to_csv('/Users/sanskarsehgal/Desktop/Big Data/Project/Reddit Substance Abuse/{}'.format(subreddit_name))

