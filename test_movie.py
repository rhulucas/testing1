import pytest
from movie import Movie


@pytest.fixture
def movie():
    return Movie("Test Movie")

def test_init(movie):
    assert movie._title == "Test Movie"
    assert movie._review_videos == []
    
def test_youtube_search(movie):
    movie.youtube_search(max_result=1)
    assert len(movie._review_videos)>0