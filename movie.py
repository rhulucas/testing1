import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

class Movie:
    def __init__(self, title):
        self._title = title
        self._review_videos = []
        self.youtube_service = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

    def youtube_search(self, max_result=10):
        try:
            search_response = self.youtube_service.search().list(
                q=self._title + " review",
                part='id,snippet',
                maxResults=max_result,
                type='video'
            ).execute()

            self._review_videos = []
  
            for search_result in search_response.get('items', []):
                if search_result['id']['kind'] == 'youtube#video':
                    video_title = search_result['snippet']['title']
                    video_id = search_result['id']['videoId']
                    video_description = search_result['snippet']['description']
                    video_info = {
                        'id': video_id,
                        'title': video_title,
                        'description': video_description
                    }
                    self._review_videos.append(video_info)
                        
        except HttpError as e:
            print (f'An HTTP error {e.resp.status} occurred:\n{e.content}') 
            return None