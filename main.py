from fastapi import FastAPI, HTTPException
from movie import Movie

app =FastAPI()
#video_id = MovieID()

@app.get("/")
def root():
    return{"message": "Hello World"}

@app.get("/movie/{movie_name}")
def get_movieview_by_name(movie_name: str):
    results = []
    if movie_name:
        movies = Movie(movie_name)
        movies.youtube_search(max_result=10)
        return movies._review_videos
    return results