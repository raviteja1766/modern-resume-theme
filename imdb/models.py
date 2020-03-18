from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length = 200,primary_key=True)

    def __str__(self):
        return self.name

class Actor(models.Model):
    actor_id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 2)

class Genre(models.Model):
    name = models.CharField(max_length = 100,primary_key = True)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    movie_id = models.CharField(max_length=100,primary_key=True)
    release_date = models.IntegerField()
    box_office_collection_in_crores = models.FloatField()
    language = models.CharField(max_length = 50)
    imdb_link = models.CharField(max_length = 200,null = True)
    average_rating = models.CharField(max_length = 50)
    actors = models.ManyToManyField(Actor,through='Cast')
    genres = models.ManyToManyField(Genre)
    director = models.ForeignKey(Director,on_delete = models.CASCADE,null = True)
    
    # def prepare_movie_type_class(self):
        
    #     return MovieTypeClass(
    #         name=self.name,
    #         average_rating=self.average_rating(),
    #         movie_id = self.movie_id,
    #         release_date = self.release_date,
    #         box_office_collection_in_crores = self.box_office_collection_in_crores,
    #         director = self.director
    #     )

class Cast(models.Model):
    actor = models.ForeignKey(Actor,on_delete = models.CASCADE,)
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE,)
    role = models.CharField(max_length = 50,null = True)
    