from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv
import pprint


load_dotenv()

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

def get_comment(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.commentThreads().list(
        part = 'snippet, replies',
        videoId = video_id,
    )

    data_dict = {'user_name': [], 'comment': [], 'replies_count': [], 'viewer_rating': [], 'likes_count': []}

    response = request.execute()

    user_name = response['items'][0]['snippet']['topLevelComment']['snippet']['authorDisplayName']
    comment = response['items'][0]['snippet']['topLevelComment']['snippet']['textDisplay']
    replies_count = response['items'][0]['snippet']['totalReplyCount']
    viewer_rating = response['items'][0]['snippet']['topLevelComment']['snippet']['viewerRating']
    likes_count = response['items'][0]['snippet']['topLevelComment']['snippet']['likeCount']

    data_dict['user_name'].append(user_name)
    data_dict['comment'].append(comment)
    data_dict['replies_count'].append(replies_count)
    data_dict['viewer_rating'].append(viewer_rating)
    data_dict['likes_count'].append(likes_count)

    df = pd.DataFrame(data_dict)
    return df


pprint.pp(get_comment(api_key=YOUTUBE_API_KEY, video_id='ddtxAk&ab'))

