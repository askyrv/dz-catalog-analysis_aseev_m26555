movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
import math
def average_rating(movies):
    ratings = [movie["rating"] for movie in movies]
    total = sum(ratings)
    count = len(ratings)
    average = total / count
    return round(average, 1)

def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    avg = sum(ages) / len(ages)
    avg_rounded = math.ceil(avg)
    return oldest, newest, avg_rounded

def duration_in_hours(minutes):
    hours = minutes // 60
    more_minutes = minutes % 60
    return f"{hours}ч {more_minutes}м"

def rating_tier(rating):
    if rating >= 9.0:
         return f"шедевр"
    elif rating >= 7.0:
         return f"хорошо"
    elif rating >= 5.0:
         return f"средне"
    else:
         return f"слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return f"новые"
        case _ if 2015 <= year <= 2020:
            return f"недавние"
        case _ if year < 2015:
            return f"старые"

for movie in movies:
    film_genres = movie["genres"]
    if "comedy" in film_genres:
        continue
    print(movie["title"])

i = 0
while i < len(movies):
    current_movie = movies[i]
    rating = current_movie["rating"]
    if rating > 9.0:                   
        print(f"Найден шедевр: {current_movie['title']}")
        break                         
    i += 1                             
else:
    print("Шедевров не найдено") 

def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title):
    words = title.split()
    needed_title = []
    for word in words:
        big_first = word[0].upper() + word[1:]
        needed_title.append(big_first)
    return " ".join(needed_title)

def make_slug(title):
    lower_title = title.lower()
    slug = lower_title.replace(" ", "-")
    return slug

def format_report_line(movie):
    genres_str = ", ".join(sorted(movie["genres"]))
    report = (
        f"{movie['title']} ({movie['year']}) "
        f"- {movie['rating']}/10, "
        f"{duration_in_hours(movie['duration_min'])}, "
        f"жанры: {genres_str}"
    )
    return report

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    titles = [movie["title"] for movie in sorted_movies]
    return titles

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    top_movies = sorted_movies[:n]
    finaly = [(movie["title"], movie["rating"]) for movie in top_movies]
    return finaly

def count_by_genre(movies):
    genre_count = {}
    for movie in movies:
        genres = movie["genres"]
        for genre in genres:
            genre_count[genre] = genre_count.get(genre, 0) + 1
    return genre_count

def actor_filmography(movies):
    act_dic = {}
    for movie in movies:
        actors = movie["actors"]
        title = movie["title"]
        for actor in actors:
            if actor not in act_dic:
                act_dic[actor] = []
            act_dic[actor].append(title)
    return act_dic


def high_rated_dict(movies):
    rat = average_rating(movies)
    result = {
        movie["title"]: movie["rating"]
        for movie in movies 
        if movie["rating"] > rat
    }
    return result 

def all_genres(movies):
    uniq_genres = set()
    for movie in movies:
        uniq_genres = uniq_genres | movie["genres"]
    return uniq_genres

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genresA = set()
    for movie in movies_a:
        genresA.update(movie["genres"])
    genresB = set()
    for movie in movies_b:
        genresB.update(movie["genres"])
    return genresA - genresB

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

for movie in iter_high_rated(movies, min_rating=8.0):
    report_line = format_report_line(movie)
    print(report_line)
    

total_duration_minutes = sum(
    movie["duration_min"] 
    for movie in movies 
    if movie["rating"] > 7
)

def build_report(movies):
    print(f"ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг:", average_rating(movies))
    stats = catalog_age_stats(movies)
    average_age = stats[2]
    print(f"Средний возраст фильмов:", average_age, f"лет")
    print(f"Топ 3-фильма:")
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    top_3_movies = sorted_movies[:3]
    for i, movie in enumerate(top_3_movies, start=1):
        report_line = format_report_line(movie)
        print(f"{i}. {report_line}")
    print(f"Фильмов по жанрам:")
    genre_count = count_by_genre(movies)
    sorted_genres = sorted(genre_count.items(), key=lambda x: x[1], reverse=True)
    for genre, count in sorted_genres:
        print(f"- {genre}: {count}")
    genres_report = all_genres(movies)
    result = ", ".join(genres_report)
    print(f"Все жанры каталого:", result)
build_report(movies)