from django.shortcuts import render
from django.template import loader
import json
from imdb.models import *

# Create your views here.
# class MovieTypeClass:
#     def __init__(name, average_rating,movie_id,release_date,box_office_collection_in_crores,director):
#         self.name = name
#         self.average_rating = averagte_rating
#         self.movie_id = movie_id
#         self.box_office_collection_in_crores = box_office_collection_in_crores
#         self.director = director

def home(request):
    movies_objs = list(Movie.objects.all())
    # movie_type_objects = [ obj.prepare_movie_type_class() for movie_obj in movies_objs ]
    return render(request,'imdb_home.html',{'movies':movies_objs})

def movie(request,movie_id):
    obj = Movie.objects.get(movie_id = movie_id)
    cast_list = list(Cast.objects.filter(movie=obj))
    context = {
        'casts':cast_list,
        'movie_obj':obj
        }
    return render(request,'imdb_movie.html',context)
def actor(request,actor_id):
    obj = Actor.objects.get(actor_id = actor_id)
    cast_list = list(Cast.objects.filter(actor=obj))
    context = {
        'casts':cast_list,
        'actor_obj':obj
    }
    return render(request,'imdb_actor.html',context)



def director(request,name):
    obj = Director.objects.get(name = name)
    movies = Movie.objects.filter(director = obj)
    context = {
        'movies':movies,
        'director_obj': obj
    }
    return render(request,'imdb_director.html',context)
def analytics(request):
    from .utils import movie_collections_in_polar_data,get_radar_chart_data,get_one_bar_plot_data,execute_sql_query,get_multi_line_plot_data,get_two_bar_plot_data,get_area_plot_data,get_doughnut_chart_data,get_pie_chart_data
    data_1 = execute_sql_query(
        """
            select d.name,
                max(m.box_office_collection_in_crores),
                avg(m.box_office_collection_in_crores)
                from (imdb_movie as m inner join imdb_director as d
                ON m.director_id = d.name)
                group by d.name
        """
    )
    data_2 = execute_sql_query(
        """
            select avg(box_office_collection_in_crores),
                strftime("%Y",release_date) as year
                from imdb_movie group by year
        """
    )
    data_3 = execute_sql_query(
        """
            select strftime("%Y",release_date) as year
                from imdb_movie where year >= '2000' group by year order by year  limit 10

        """
    )
    data_4 = execute_sql_query(
        """
            select strftime("%Y",m.release_date) as year,
                    a.gender,count(distinct(a.actor_id))
                from imdb_cast as c
                inner join imdb_actor as a
                inner join imdb_movie as m
                on c.actor_id = a.actor_id and
                c.movie_id = m.movie_id and year >= '2000'
                group by year,a.gender order by year  limit 10
        """
    )
    data_5 = execute_sql_query(
        """
            select g.name,
                sum(distinct(m.box_office_collection_in_crores)) 
                from imdb_genre as g
                inner join imdb_movie_genres as t
                inner join imdb_movie as m
                on t.genre_id = g.id and
                t.movie_id = m.movie_id and
                strftime("%Y",m.release_date)>= '2010' 
                group by g.id order by g.name 
        """
    )
    data_6 = execute_sql_query(
        """
            select max(box_office_collection_in_crores),
                strftime("%Y",release_date) as year,
                name
                from imdb_movie 
                group by year having max(box_office_collection_in_crores) limit 5
        """
    )
    

    dict_1 = get_one_bar_plot_data(data_6)
    dict_3 = get_multi_line_plot_data(data_3,data_4)
    dict_1.update(dict_3)
    dict_4 = get_two_bar_plot_data(data_1)
    dict_1.update(dict_4)
    dict_5 = get_area_plot_data(data_2)
    dict_1.update(dict_5)
    dict_6 = get_doughnut_chart_data(data_5)
    dict_1.update(dict_6)
    return render(request,'analytics.html',context = dict_1)