import pytest
from movie import Movie
from googleapiclient.errors import HttpError


@pytest.fixture
def movieA():
    movieA = Movie("Test Movie")
    return movieA


def test_init(movieA):
    assert movieA._title == "Test Movie"
    assert movieA._review_videos == []
    
def test_youtube_search(movieA):
    movieA.youtube_search(max_result=1)
    assert len(movieA._review_videos)>0
    
@pytest.fixture
def yt(mocker):
    yt_instance = Movie(" ")
    yt_instance.youtube_service = mocker.Mock()
    return yt_instance

def test_init_duplicate(movieA):
    assert movieA._title == "Test Movie"
    assert movieA._review_videos == []
    
def test_youtube_description_success(yt, mocker):
    mocker.patch.object(
        yt.youtube_service.videos().list(),
        'execute',
        return_value={'items':[{'snippet':{'description': 'description test'}}]}
    )
    result = yt.youtube_description("test_video_id")
    assert result == {'description': 'description test'}
  
def test_youtube_description_no_items(yt, mocker):
      mocker.patch.object(
          yt.youtube_service.videos().list(),
          'execute',
          return_value={'items':[]}
      )
      result = yt.youtube_description("test_video_id")
      assert result is None

def test_youtube_description_http_error(yt, mocker):
    mocker.patch.object(
        yt.youtube_service.videos().list(),
        'execute',
        side_effect=HttpError(mocker.Mock(status=404), b'Error')
    )
    result = yt.youtube_description("test_video_id")
    assert result is None         