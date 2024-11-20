from googleapiclient.discovery import build
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.environ['YOUTUBE_API_KEY']

def get_comment(api_key, video_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.commentThreads().list(
        part = 'snippet, replies',
        videoId = video_id,
    )

    df = pd.DataFrame(columns=['comment', 'replies', 'data', 'user_name'])

    response = request.execute()


    return response['items'][0]['snippet']['totalReplyCount']


print(get_comment(api_key=YOUTUBE_API_KEY, video_id='yj9r5bJtZDU' ))

