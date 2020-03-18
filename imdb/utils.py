from imdb.models import *
import json

# genres_list =[
#     "Comedy","Horror","Science Fiction","Romance","Thriller","Crime"
# ]

# languages_list = [
#     "Telugu","Hindi","English","Malayaalam","Tamil"
# ]

# actors_list =[
#         {
#             "actor_id": "actor_1",
#             "name": "Actor 1",
#             "gender":"M",
#             "date_of_birth":"2001-01-01"
#         },
#         {
#             "actor_id": "actor_2",
#             "name": "Actor 2",
#             "gender":"F",
#             "date_of_birth":"2002-01-01"
#         },
#         {
#             "actor_id": "actor_3",
#             "name": "Actor 3",
#             "gender":"M",
#             "date_of_birth":"2003-01-01"
#         },
#         {
#             "actor_id": "actor_4",
#             "name": "Actor 4",
#             "gender":"M",
#             "date_of_birth":"2004-01-01"
#         },
#         {
#             "actor_id": "actor_5",
#             "name": "Actor 6",
#             "gender":"F",
#             "date_of_birth":"2005-01-01"
#         },
#         {
#             "actor_id": "actor_6",
#             "name": "Actor 6",
#             "gender":"F",
#             "date_of_birth":"2006-01-01"
#         },
#         {
#             "actor_id": "actor_7",
#             "name": "Actor 7",
#             "gender":"M",
#             "date_of_birth":"2007-01-01"
#         },
#         {
#             "actor_id": "actor_8",
#             "name": "Actor 8",
#             "gender":"F",
#             "date_of_birth":"2008-01-01"
#         },
#         {
#             "actor_id": "actor_9",
#             "name": "Actor 9",
#             "gender":"F",
#             "date_of_birth":"2009-01-01"
#         },
#         {
#             "actor_id": "actor_10",
#             "name": "Actor 10",
#             "gender":"M",
#             "date_of_birth":"2010-01-01"
#         },
#         {
#             "actor_id": "actor_11",
#             "name": "Actor 11",
#             "gender":"F",
#             "date_of_birth":"2011-01-01"
#         },
#         {
#             "actor_id": "actor_12",
#             "name": "Actor 12",
#             "gender":"M",
#             "date_of_birth":"2012-01-01"
#         }
#     ]

# directors_list = [
#         "Director 1","Director 2","Director 3"
#     ]
# movies_list = [
#         {
#             "movie_id": "movie_1",
#             "name": "Movie 1",
#             "actors": [
#                 {
#                     "actor_id": "actor_1",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 },
#                 {
#                     "actor_id": "actor_2",
#                     "role": "villan",
#                     "is_debut_movie": True
#                 }
#             ],
#             "genres" : [
#                 {
#                     "id": 1
#                 },
#                 {
#                     "id": 3
#                 },
#                 {
#                     "id": 5
#                 }
#             ],
#             "languages":[
#                 {
#                     "id": 1
#                 },
#                 {
#                     "id":4
#                 }
#             ],
#             "box_office_collection_in_crores": "12.3",
#             "release_date": "2020-3-3",
#             "director_name": "Director 1"
#         },
#         {
#             "movie_id": "movie_2",
#             "name": "Movie 2",
#             "actors": [
#                 {
#                     "actor_id": "actor_3",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 },
#                 {
#                     "actor_id": "actor_4",
#                     "role": "villan",
#                     "is_debut_movie": True
#                 },
#                 {
#                     "actor_id": "actor_5",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 }
#             ],
#             "genres" : [
#                 {
#                     "id": 2
#                 },
#                 {
#                     "id": 4
#                 },
#                 {
#                     "id": 6
#                 }
#             ],
#             "languages":[
#                 {
#                     "id": 2
#                 },
#                 {
#                     "id":3
#                 }
#             ],
#             "box_office_collection_in_crores": "11.3",
#             "release_date": "2021-3-3",
#             "director_name": "Director 1"
#         },
#         {
#             "movie_id": "movie_3",
#             "name": "Movie 3",
#             "actors": [
#                 {
#                     "actor_id": "actor_5",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 },
#                 {
#                     "actor_id": "actor_6",
#                     "role": "villan",
#                     "is_debut_movie": True
#                 },
#                 {
#                     "actor_id": "actor_4",
#                     "role": "villan",
#                     "is_debut_movie": True
#                 }
#             ],
#             "genres" : [
#                 {
#                     "id": 1
#                 },
#                 {
#                     "id": 4
#                 }
#             ],
#             "languages":[
#                 {
#                     "id": 1
#                 },
#                 {
#                     "id":5
#                 }
#             ],
#             "box_office_collection_in_crores": "11.8",
#             "release_date": "2022-3-3",
#             "director_name": "Director 2"
#         },
#         {
#             "movie_id": "movie_4",
#             "name": "Movie 4",
#             "actors": [
#                 {
#                     "actor_id": "actor_7",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 },
#                 {
#                     "actor_id": "actor_8",
#                     "role": "villan",
#                     "is_debut_movie": True
#                 }
#             ],
#             "genres" : [
#                 {
#                     "id": 1
#                 },
#                 {
#                     "id": 2
#                 }
#             ],
#             "languages":[
#                 {
#                     "id": 2
#                 },
#                 {
#                     "id":3
#                 }
#             ],
#             "box_office_collection_in_crores": "12.6",
#             "release_date": "2023-3-3",
#             "director_name": "Director 2"
#         },
#         {
#             "movie_id": "movie_5",
#             "name": "Movie 5",
#             "actors": [
#                 {
#                     "actor_id": "actor_9",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 },
#                 {
#                     "actor_id": "actor_10",
#                     "role": "villan",
#                     "is_debut_movie": True
#                 }
#             ],
#             "genres" : [
#                 {
#                     "id": 2
#                 },
#                 {
#                     "id": 3
#                 },
#                 {
#                     "id": 6
#                 }
#             ],
#             "languages":[
#                 {
#                     "id": 1
#                 },
#                 {
#                     "id":5
#                 }
#             ],
#             "box_office_collection_in_crores": "12.8",
#             "release_date": "2023-3-3",
#             "director_name": "Director 3"
#         },
#         {
#             "movie_id": "movie_6",
#             "name": "Movie 6",
#             "actors": [
#                 {
#                     "actor_id": "actor_11",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 },
#                 {
#                     "actor_id": "actor_12",
#                     "role": "villan",
#                     "is_debut_movie": True
#                 }
#             ],
#             "genres" : [
#                 {
#                     "id": 1
#                 },
#                 {
#                     "id": 2
#                 },
#                 {
#                     "id": 4
#                 }
#             ],
#             "languages":[
#                 {
#                     "id": 2
#                 },
#                 {
#                     "id":4
#                 }
#             ],
#             "box_office_collection_in_crores": "11.6",
#             "release_date": "2019-3-3",
#             "director_name": "Director 3"
#         }
#     ]
# movie_rating_list = [
#         {
#             "movie_id": "movie_1",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 4,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_2",
#             "rating_one_count": 2,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 8,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_3",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 5,
#             "rating_five_count": 9
#         },
#         {
#             "movie_id": "movie_4",
#             "rating_one_count": 5,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 8,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_5",
#             "rating_one_count": 4,
#             "rating_two_count": 8,
#             "rating_three_count": 4,
#             "rating_four_count": 3,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_6",
#             "rating_one_count": 4,
#             "rating_two_count": 7,
#             "rating_three_count": 4,
#             "rating_four_count": 3,
#             "rating_five_count": 4
#         }
#     ]

# def populate_database(actors_list, movies_list, directors_list,
#                             movie_rating_list,genres_list,languages_list):
#     from imdb.models import Actor,Movie,Director,Cast,Rating

#     for actor in actors_list:
#         Actor.objects.create(actor_id = actor['actor_id'],
#         name=actor['name'],
#         date_of_birth=actor['date_of_birth'],
#         gender = actor['gender']
#         )
        
#     for director in directors_list:        
#         Director.objects.create(name=director)
#     for language in languages_list:
#         Language.objects.create(name = language)
#     for genre in genres_list:
#         Genre.objects.create(name = genre)

#     for movie in movies_list:
#         mid = Movie.objects.create(movie_id = movie['movie_id'],
#             name = movie['name'],
#             box_office_collection_in_crores = movie['box_office_collection_in_crores'],
#             release_date = movie['release_date'],
#             director = Director.objects.get(name = movie['director_name'])
#         )
#         for actor in movie['actors']:
#             Cast.objects.create(
#                     actor = Actor.objects.get(actor_id = actor['actor_id']),
#                     movie = Movie.objects.get(movie_id = movie['movie_id']),
#                     role = actor['role'],
#                     is_debut_movie = actor['is_debut_movie']
#             )
#         for genre in movie['genres']:
#             mid.genres.add(Genre.objects.get(id = genre['id']))

#         for language in movie['languages']:
#             mid.languages.add(Language.objects.get(id = language['id']))
    
#     for movie_rate in movie_rating_list:
#         Rating.objects.create(
#             movie = Movie.objects.get(movie_id = movie_rate['movie_id']),
#             rating_one_count = movie_rate['rating_one_count'],
#             rating_two_count = movie_rate['rating_two_count'],
#             rating_three_count = movie_rate['rating_three_count'],
#             rating_four_count = movie_rate['rating_four_count'],
#             rating_five_count = movie_rate['rating_five_count']
#         )

def populate_actors():
    obj = open("/home/ravi/project_imdb/imdb/complete_data/actors_5000.json","r")
    actor_json_list = obj.read()
    actor_list = json.loads(actor_json_list)
    for actor in actor_list:
        Actor.objects.create(actor_id = actor['actor_id'],
        name=actor['name'],
        gender = actor['gender']
        )
def populate_directors():
    obj = open("/home/ravi/project_imdb/imdb/complete_data/directors_5000.json","r")
    director_json_list = obj.read()
    director_list = json.loads(director_json_list)
    for director in director_list:
        Director.objects.create(name=director)

def populate_movies():
    obj = open("/home/ravi/project_imdb/imdb/complete_data/movies_5000.json","r")
    movie_json_list = obj.read()
    movie_list = json.loads(movie_json_list)
    for movie in movie_list:
        if movie['year_of_release']=='':
            movie['year_of_release']= '0'
        try:
            dir_obj = Director.objects.get(name = movie['director_name'])
        except Director.DoesNotExist:
            dir_obj = None
        Movie.objects.create(
            movie_id = movie['movie_id'],
            name = movie['name'],
            box_office_collection_in_crores = movie['box_office_collection_in_crores'],
            release_date = int(movie['year_of_release']),
            average_rating = movie['average_rating'],
            language = movie['language'],
            imdb_link = movie['imdb_link'],
            director = dir_obj
        )
        for actor in movie['actors']:
            Cast.objects.create(
                actor = Actor.objects.get(actor_id = actor['actor_id']),
                movie = Movie.objects.get(movie_id = movie['movie_id']),
                role = actor['role']
            )
        for genre in movie['genres']:
            try:
                movie.genres.add(Genre.objects.get(name = genre))
            except Genre.DoesNotExist:
                movie.genres.add(Genre.objects.create(name=genre))
        





def get_average_rating_of_movie(movie_obj):
    
    try:
        rate_obj = Rating.objects.get(movie = movie_obj)
        one = rate_obj.rating_one_count 
        two = rate_obj.rating_two_count 
        three = rate_obj.rating_three_count 
        four = rate_obj.rating_four_count  
        five = rate_obj.rating_five_count 
        sum_of_ratings = one + two * 2 + three * 3 + four * 4 + five * 5
        no_of_ratings = one + two + three + four + five
        return sum_of_ratings/no_of_ratings
    except ZeroDivisionError:
        return 0
    except Rating.DoesNotExist:
        return 0

def movie_collections_in_polar_data():
    import json
    from imdb.models import Movie
    movie_collections = list(Movie.objects.values_list('box_office_collection_in_crores',flat = True))
    movie_names = list(Movie.objects.values_list('name',flat = True))
    
    polar_chart_data = {
        "datasets": [{
            "data": movie_collections ,
            "backgroundColor": [
                "rgba(0, 0, 255,0.9)",
                "rgba(0, 255, 0,0.8)",
                "rgba(255, 0, 0,0.7)",
                "rgba(25,75,150,0.2)",
                "rgba(150, 75, 25,0.5)"
            ]

        }],
        "labels": movie_names
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Movie Collections'
    }	

def get_one_bar_plot_data(data):
    import json
    names = [ f"{item[2]}-{item[1]}" for item in data]
    collections = [item[0] for item in data]
    print()
    print(names)
    print(collections)
    print()
    single_bar_chart_data = {
        "labels": names,
        "datasets":[
            {
            "data": collections,
            "name": "Single Bar Chart",
            "borderColor": "rgba(0, 123, 255, 0.9)",
            "border_width": "0",
            "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': "Year's Most Gross Collected Movie"
    }

def get_two_bar_plot_data(data):
    import json
    list_1 = [item[0] for item in data]
    list_2 = [item[1] for item in data]
    list_3 = [item[2] for item in data]
    multi_bar_plot_data = {
        "labels": list_1,
        "datasets": [
            {
                "label": "Average Movie's collections",
                "data": list_3,
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "Career Best Movie Collection",
                "data": list_2,
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0,0,0,0.07)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title':  "Director's Career with Best and Average Movie collection's"
    }


def get_multi_line_plot_data(data_3,data_4):
    import json
    from imdb.models import Movie
    # from collections import defaultdict
    # dict_1 = defaultdict(int)
    # male_dict = defaultdict(int)
    # female_dict = defaultdict(int)
    dict_1 = {}
    for item in data_3:
        dict_1[item[0]]=0
    male_dict = dict_1.copy()
    female_dict = dict_1.copy()
    for item in data_4:
        if item[1] == 'M':
            male_dict[item[0]] = item[2]
        elif item[1] == 'F':
            female_dict[item[0]] = item[2]
    years_list = [item[0] for item in data_3]
    females_list =[ value for value in female_dict.values()]
    males_list = [ value for value in male_dict.values()]
    # for i in range(0,len(data_4)):
    #     if not(i%2):
    #         females_list.append(data_4[i][2])
    # for i in range(0,len(data_4)):
    #     if (i%2):
    #         males_list.append(data_4[i][2])

    multi_line_plot_data = {
        "labels": years_list,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Male Actors",
            "data": males_list,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, {
            "label": "Female Actors",
            "data": females_list,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': "Male Vs Female Appearance in recent year's"
    }


def get_area_plot_data(data):
    import json
    list_2 = [item[1] for item in data]
    list_1 = [item[0] for item in data]
    area_plot_data = {
        "labels": list_2,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
            "data": list_1,
            "label": "Average Movie collections",
            "backgroundColor": 'rgba(0,103,255,.15)',
            "borderColor": 'rgba(0,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(0,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': 'Cine Industry Growth'
    }


def get_radar_chart_data():
    import json
    radar_chart_data = {
        "labels": [["Eating", "Dinner"], ["Drinking", "Water"], "Sleeping",
                   ["Designing", "Graphics"], "Coding", "Cycling", "Running"],
        "defaultFontFamily": 'Poppins',
        "datasets": [
            {
                "label": "My First dataset",
                "data": [65, 59, 66, 45, 56, 55, 40],
                "borderColor": "rgba(0, 123, 255, 0.6)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.4)"
            },
            {
                "label": "My Second dataset",
                "data": [28, 12, 40, 19, 63, 27, 87],
                "borderColor": "rgba(0, 123, 255, 0.7",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'radar_chart_data_one': json.dumps(radar_chart_data),
        'radar_chart_data_one_title': 'Title'
    }


def get_doughnut_chart_data(data):
    import json
    genre_list = [item[0] for item in data]
    genre_percentage = [item[1] for item in data]
    doughnut_graph_data = {
        "datasets": [{
            "data": genre_percentage,
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": genres_list
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': "Genre Total Collection's"
    }


def get_multi_line_plot_with_area_data():
    import json
    multi_line_plot_with_area_data = {
        "labels": [
            "January", "February", "March", "April", "May", "June",
            "July"],
        "defaultFontFamily": "Poppins",
        "datasets": [
            {
                "label": "My First dataset",
                "borderColor": "rgba(0,0,0,.09)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0,0,0,.07)",
                "data": [22, 44, 67, 43, 76, 45, 12]
            },
            {
                "label": "My Second dataset",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "1",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "pointHighlightStroke": "rgba(26,179,148,1)",
                "data": [16, 32, 18, 26, 42, 33, 44]
            }
        ]
    }

    return {
        'multi_line_plot_with_area_data_one': json.dumps(
            multi_line_plot_with_area_data),
        'multi_line_plot_with_area_data_one_title': 'Title'
    }


def get_pie_chart_data(data):
    import json
    genre_list = [item[0] for item in data]
    genre_percentage = [item[1] for item in data]
    pie_chart_data = {
        "datasets": [{
            "data": genre_percentage,
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": genre_list
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Title'
    }




def get_polar_chart_data():
    import json

    polar_chart_data = {
        "datasets": [{
            "data": [15, 18, 9, 6, 19],
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.8)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0,0,0,0.2)",
                "rgba(0, 123, 255,0.5)"
            ]

        }],
        "labels": [
            "Green1",
            "Green2",
            "Green3",
            "Green4",
            "Green5"
        ]
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Title'
    }


def execute_sql_query(sql_query):
    """
    Executes sql query and return data in the form of lists (
        This function is similar to what you have learnt earlier. Here we are
        using `cursor` from django instead of sqlite3 library
    )
    :param sql_query: a sql as string
    :return:
    """
    from django.db import connection
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        rows = cursor.fetchall()
    return rows
