from fastapi.testclient import TestClient
from main import app
from googleapiclient.discovery import build
  
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hello World"} 
    
def test_get_movieview_by_name():
    response = client.get("/movie/test_movie")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
def test_get_video_description():
    response = client.get("/descriptions/EmABso6rgqM")
    assert response.status_code == 200
    print("Response JSON:", response.json())
    assert isinstance(response.json(), dict)
    
def test_get_find_movie_review_videos():
    language = "zh"
    movie_name = "three gorges"
    response = client.get(f"/moviereviews/{language}/{movie_name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)    