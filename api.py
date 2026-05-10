from typing import List

from django.shortcuts import get_object_or_404
from ninja import NinjaAPI, ModelSchema

from .models import Movie, Comment


api = NinjaAPI()


# =========================
# SCHÉMATA PRO MOVIE
# =========================

class MovieOut(ModelSchema):
    class Config:
        model = Movie
        model_fields = ["id", "title", "description", "year"]


class MovieIn(ModelSchema):
    class Config:
        model = Movie
        model_fields = ["title", "description", "year"]


# =========================
# SCHÉMATA PRO COMMENT
# =========================

class CommentOut(ModelSchema):
    class Config:
        model = Comment
        model_fields = ["id", "movie", "author", "text"]


class CommentIn(ModelSchema):
    class Config:
        model = Comment
        model_fields = ["movie", "author", "text"]


# =========================
# MOVIE ENDPOINTY
# =========================

@api.get("/movie", response=List[MovieOut])
def list_movies(request):
    return Movie.objects.all()


@api.get("/movie/{movie_id}", response=MovieOut)
def get_movie(request, movie_id: int):
    return get_object_or_404(Movie, id=movie_id)


@api.post("/movie", response=MovieOut)
def create_movie(request, data: MovieIn):
    movie = Movie.objects.create(**data.dict())
    return movie


@api.put("/movie/{movie_id}", response=MovieOut)
def update_movie(request, movie_id: int, data: MovieIn):
    movie = get_object_or_404(Movie, id=movie_id)

    for attr, value in data.dict().items():
        setattr(movie, attr, value)

    movie.save()
    return movie


@api.delete("/movie/{movie_id}")
def delete_movie(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    movie.delete()

    return {"success": True}


# =========================
# COMMENT ENDPOINTY
# dobrovolné rozšíření
# =========================

@api.get("/comment", response=List[CommentOut])
def list_comments(request):
    return Comment.objects.all()


@api.get("/comment/{comment_id}", response=CommentOut)
def get_comment(request, comment_id: int):
    return get_object_or_404(Comment, id=comment_id)


@api.post("/comment", response=CommentOut)
def create_comment(request, data: CommentIn):
    comment = Comment.objects.create(**data.dict())
    return comment


@api.put("/comment/{comment_id}", response=CommentOut)
def update_comment(request, comment_id: int, data: CommentIn):
    comment = get_object_or_404(Comment, id=comment_id)

    for attr, value in data.dict().items():
        setattr(comment, attr, value)

    comment.save()
    return comment


@api.delete("/comment/{comment_id}")
def delete_comment(request, comment_id: int):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()

    return {"success": True}
