from fastapi import FastAPI, HTTPException

app =FastAPI()
#video_id = MovieID()

@app.get("/")
def root():
    return{"message": "Hello World"}