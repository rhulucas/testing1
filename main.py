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

@app.get("/descriptions/{video_id}")
def get_video_description(video_id: str):
     movie_new= Movie ("Some Title ")
     movie_description = movie_new.youtube_description(video_id)
     if movie_description:
         return movie_description
     else:
        raise HTTPException(status_code=404, detail="Description not found")
      
@app.get("/moviereviews/{language}/{movie_name}")
def get_find_movie_review_videos(language:str, movie_name:str):
    results = []
    if movie_name:
        moviesA = Movie(movie_name)
        translated_title = moviesA.find_movie_review_videos(language, movie_name)
        moviesA.youtube_search(max_result=10)
        return moviesA._review_videos
    return results