#!/usr/bin/env python3

import os
import sys
import urllib
import requests
from bs4 import BeautifulSoup
import json
import pytest
import collections
import functools
import datetime
import re
from collections import Counter
from datetime import time

# print("reload success in %s" % datetime.datetime.now())

class Movies:
    """
    Анализ данных из файла movies.csv
    """
    def __init__(self, path_to_the_file):
        """
        Поместите сюда любые поля, которые, по вашему мнению, вам понадобятся.
        """

        self.movies_list = []
        self.count_genres = {}
        # https://stackoverflow.com/questions/18893390/splitting-on-comma-outside-quotes
        # with open(path_to_the_file) as f:
        #     lines_from_file = f.readlines()
        with open(path_to_the_file) as f:
            next(f)
            for line in f:
                arr = re.split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', line.rstrip())

                # take id
                mv_id = arr[0]

                # take name and year
                film_str = arr[1].strip('"')
                film_year = re.findall(r'^(.*?) \((\d{4})\)\s*?$|^(.*?)$', film_str)
                mv_film = film_year[0][0]
                mv_year = film_year[0][1] if len(film_year[0]) >= 2 else None

                # take genres
                mv_genres = arr[2].split("|")

                # count genres
                mv_count_genres = len(mv_genres)

                # main array of movies
                self.movies_list.append((mv_id, mv_film, mv_year, mv_genres, mv_count_genres))

                # dict of count genres for each movie
                self.count_genres[mv_film] = mv_count_genres

        self.count_genres = {k: v for k, v in sorted(self.count_genres.items(), key=lambda item: -item[1])}

        # создаем dict для year: count
        self.release_years = {}
        for movie in self.movies_list:
            self.release_years[movie[2]] = self.release_years.get(movie[2], 0) + 1
        self.release_years = {k: v for k, v in sorted(self.release_years.items(), key=lambda item: -item[1])}

    # создаем dict для genres: count
    self.genres = {}
    for movie in self.movies_list:
        for genre in movie[3]:
            self.genres[genre] = self.genres.get(genre, 0) + 1
    self.genres = {k: v for k, v in sorted(self.genres.items(), key=lambda item: -item[1])}


def dist_by_release(self) -> dict:
    """
    Метод возвращает dict или OrderedDict, где ключи - годы, а значения - числа.
    Вам нужно извлечь годы из названий. Отсортируйте по убыванию количества.
    """
    return self.release_years


def dist_by_genres(self) -> dict:
    """
    Метод возвращает словарь, в котором ключи являются жанрами, а значения - счетчиками.
    Отсортируйте по убыванию количества.
    """
    return self.genres

def most_genres(self, n: int) -> dict:
    """
    Метод возвращает dict с топ-n фильмами, где ключи - названия фильмов, а
    значения - это количество жанров фильма. Сортировать по номерам по убыванию.
    """
    return dict(list(self.count_genres.items())[:n])

def average(rait_list: list[int]) -> int:
    """
    вспомогательный метод чтобы посчитать среднее по списку
    """
    if(len(rait_list) != 0):
        return round(sum(rait_list)/len(rait_list), 2)
    return None

def median(rait_list: list) -> int:
    """
    вспомогательный метод чтобы посчитать медиану по списку
    """
    len_rait = len(rait_list)
    if(len_rait != 0):
        rait_list.sort()
        if (len_rait % 2 == 1):
            return round(rait_list[len_rait//2], 2)
        else:
            return round((rait_list[len_rait//2-1]+rait_list[len_rait//2])/2,2)
    return None

class Ratings:
    """
    Анализ данных из rating.csv
    """
    def __init__(self, path_to_the_file):
        """
        Поместите сюда любые поля, которые, по вашему мнению, вам понадобятся.
        Put here any fields that you think you will need.
        """

        self.ratings_list = []
        with open(path_to_the_file) as f:
            next(f)
            for line in f:
                arr = re.split(',', line.rstrip())
                userId = int(arr[0])
                movieId = int(arr[1])
                rating = float(arr[2])
                timestamp = int(arr[3])
                year = int(datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y'))
                # создаем список рейтингов общих
                self.ratings_list.append((userId, movieId, rating, timestamp, year))

        # создаем базу по фильмам
        self.movies = Ratings.Movies(self.ratings_list)

        # создаем базу по пользователям
        self.users = Ratings.Users(self.ratings_list)

    class Movies:
        def __init__(self, rating_list):
            # dict -> movie_id : list_of_ratings_current_films
            movies_dict_w_listratings = {}
            # dict -> year : count_of_values
            years_dict = {}
            # dict -> raiting : count_of_values
            rating_dict = {}
            # dict -> movie_id : count_of_values
            movies_dict = {}

            for rating in rating_list:

                # наполняем базу по фильмам
                raiting_list_of_film = movies_dict_w_listratings.get(rating[1], list())
                raiting_list_of_film.append(rating[2])
                movies_dict_w_listratings[rating[1]] = raiting_list_of_film

                # наполняем базу по годам
                years_dict[rating[4]] = years_dict.get(rating[4], 0) + 1

                # наполняем базу по рейтингам
                rating_dict[rating[2]] = rating_dict.get(rating[2], 0) + 1

                # наполняем базу по фильмам
                movies_dict[rating[1]] = movies_dict.get(rating[1], 0) + 1


            # отсортируем чтобы в большинстве случаев отдавать как есть
            years_dict = {k: v for k, v in sorted(years_dict.items(), key=lambda item: item[0])}
            rating_dict = {k: v for k, v in sorted(rating_dict.items(), key=lambda item: item[0])}
            movies_dict = {k: v for k, v in sorted(movies_dict.items(), key=lambda item: -item[1])}

            self.movies_dict_w_listratings = movies_dict_w_listratings
            self.years_dict = years_dict
            self.rating_dict = rating_dict
            self.movies_dict = movies_dict


        def dist_by_year(self) -> dict:
            """
            Метод возвращает dict, где ключи - годы, а значения - числа.
            Сортировать по годам по возрастанию.
            Вам нужно извлечь годы из меток времени.
            
            The method returns a dict where the keys are years and the values are counts.
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            return self.years_dict

        def dist_by_rating(self) -> dict:
            """
            Метод возвращает словарь, в котором ключи являются рейтингами, а значения - счетчиками.
            Сортировать по рейтингам по возрастанию.
            
            The method returns a dict where the keys are ratings and the values are counts.
            Sort it by ratings ascendingly.
            """
            return self.rating_dict


        def top_by_num_of_ratings(self, n: int) -> dict:
            """     
            Метод возвращает топ-n фильмов по количеству оценок.
            Это dict, где ключи - это названия фильмов, а значения - числа.
            Сортировать по номерам по убыванию.
            """
            return dict(list(self.movies_dict.items())[:n])

        def top_by_ratings(self, n, metric=average) -> dict:
            """
            Метод возвращает топ-n фильмов по среднему или медианному значению оценок.
            Это словарь, где ключи - это названия фильмов, а значения - это метрические значения.
            Сортировать по метрике по убыванию.
            Значения следует округлить до 2 десятичных знаков.
            """

            # создадим новый справочник
            res_dict = {}
            # получим метрику для фильма на основе справочника movies_dict_w_listratings
            for key, value in self.movies_dict_w_listratings.items():
                res_dict[key] = metric(value)
            # отсторитруем по метрике от большего к меньшему
            res_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: (-item[1], item[0]))}
            # вернем n значений
            return dict(list(res_dict.items())[:n])

        def top_controversial(self, n) -> dict:
            """
            Метод возвращает топ-n фильмов по дисперсии оценок.
            Это определение, в котором ключи - это названия фильмов, а значения - дисперсии.
            Отсортируйте по убыванию дисперсии.
            Значения следует округлить до 2 десятичных знаков.
            """

            # создадим новый справочник
            res_dict = {}
            # получим дисперсию на основе справочника movies_dict_w_listratings
            # (ВАЖНО!) дисперсию считаем для генеральной совокупности
            for key, value in self.movies_dict_w_listratings.items():
                m = average(value)
                res_dict[key] = round(sum([(xi - m)**2 for xi in value]) / (len(value)),2)
            # отсторитруем по метрике от большего к меньшему
            res_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: (-item[1], item[0]))}
            # вернем n значений
            return dict(list(res_dict.items())[:n])

    class Users:
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
        Inherit from the class Movies. Several methods are similar to the methods from it.
        """

        def __init__(self, rating_list):
            # справочник:
            # self.ratings_list.append((userId, movieId, rating, timestamp, year))

            # dict -> user_id : list_of_ratings_current_films
            users_dict_w_listratings = {}
            # dict -> user : count_of_values
            users_dict = {}

            for rating in rating_list:

                # наполняем базу по пользователям
                raiting_list_of_film = users_dict_w_listratings.get(rating[0], list())
                raiting_list_of_film.append(rating[2])
                users_dict_w_listratings[rating[0]] = raiting_list_of_film

                # наполняем базу по пользоватлеям по кол-ву оценок
                users_dict[rating[0]] = users_dict.get(rating[0], 0) + 1


            # отсортируем чтобы в большинстве случаев отдавать как есть
            users_dict = {k: v for k, v in sorted(users_dict.items(), key=lambda item: -item[1])}

            self.users_dict_w_listratings = users_dict_w_listratings
            self.users_dict = users_dict

        def dist_by_users(self) -> dict:
            """
            Первая возвращает распределение пользователей по количеству выставленных ими оценок.
            """
            return self.users_dict

        def dist_by_metric(self, metric=average) -> dict:
            """
            Вторая возвращает распределение пользователей по средним или медианным оценкам, сделанным ими.
            """
            # создадим новый справочник
            res_dict = {}
            # получим метрику для фильма на основе справочника movies_dict_w_listratings
            for key, value in self.users_dict_w_listratings.items():
                res_dict[key] = metric(value)
            # отсторитруем по метрике от большего к меньшему
            res_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: (-item[1], item[0]))}
            # вернем n значений
            return res_dict

        def top_controversial(self, n) -> dict:
            """
            Третье место возвращает первых n пользователей с наибольшим разбросом их оценок.
            """

            # создадим новый справочник
            res_dict = {}
            # получим дисперсию на основе справочника movies_dict_w_listratings
            # (ВАЖНО!) дисперсию считаем для генеральной совокупности
            for key, value in self.users_dict_w_listratings.items():
                m = average(value)
                res_dict[key] = round(sum([(xi - m)**2 for xi in value]) / (len(value)),2)
            # отсторитруем по метрике от большего к меньшему
            res_dict = {k: v for k, v in sorted(res_dict.items(), key=lambda item: (-item[1], item[0]))}
            # вернем n значений
            return dict(list(res_dict.items())[:n])

class Tags:
    """
    Analyzing data from tags.csv
    """

    def __init__(self, path_to_the_file):
        self.path = path_to_the_file
        self.datas = {'userID': [], 'movieID': [], 'tag': [], 'timestamp': [], 'tag_2': []}
        if os.path.isfile(self.path) is None:
            raise FileNotFoundError
        with open (self.path, 'r') as file:
            for line in file:
                str_ = line.strip().split(',')
                if len(str_) != 4:
                    raise Exception
                if str_[0].strip('\'') == 'userId':
                    continue
                self.datas['userID'].append(int(str_[0].strip('\'')))
                self.datas['movieID'].append(int(str_[1].strip('\'')))
                self.datas['tag'].append(str_[2].strip('\'').lower().split())
                self.datas['tag_2'].append(str_[2].strip('\'').lower())
                self.datas['timestamp'].append(int(str_[3].strip('\'')))

    def most_words(self, n) -> dict:
        """
        Метод возвращает теги top-n, в которых больше всего слов. Это диктат
        где ключи - это теги, а значения - количество слов внутри тега.
        Отбросьте дубликаты. Сортировать по номерам по убыванию.
        """
        big_tags = dict()
        lst_of_lsts_tag = sorted(self.datas['tag'], key=lambda x: -len(x))
        i = 0
        while len(big_tags) < n and i < len(lst_of_lsts_tag):
            tag = ''
            for word in lst_of_lsts_tag[i]:
                tag += word + ' '
            tag = tag.strip()
            if tag not in big_tags:
                big_tags[tag] = len(lst_of_lsts_tag[i])
            i += 1
        big_tags = sorted(big_tags.items(), key=lambda item: -item[1])
        # почему то возвращает не словарь, а лист tuple - найти причину
        return dict(big_tags)

    def longest(self, n) -> list:
        """
        Метод возвращает n самых длинных тегов по количеству символов.
        Это список тегов. Отбросьте дубликаты. Сортировать по номерам по убыванию.
        """
        big_tags = list()
        lst_of_tag = sorted(self.datas['tag_2'], key=lambda x : -len(x))
        i = 0
        while len(big_tags) < n and i < len(lst_of_tag):
            if lst_of_tag[i] not in big_tags:
                big_tags.append(lst_of_tag[i])
            i += 1
        big_tags = sorted(big_tags, key=lambda item: -len(item))
        return big_tags

    def most_words_and_longest(self, n) -> list:
        """
        Метод возвращает пересечение между тегами top-n с большинством слов внутри и
        top-n самых длинных тегов по количеству символов.
        Отбросьте дубликаты. Это список тегов.
        """
        big_tags = []
        d = self.most_words(n)
        lst = self.longest(n)
        for key in d:
            if key in lst:
                big_tags.append(key)
        return big_tags

    def most_popular(self, n) -> dict:
        """
        Метод возвращает самые популярные теги.
        Это словарь, где ключи - это теги, а значения - это счетчики.
        Отбросьте дубликаты. Отсортируйте по убыванию количества.
        """
        popular_tags = dict(Counter(self.datas['tag_2']).most_common(n))
        # сортировка не работает
        return popular_tags

    def tags_with(self, word) -> list:
        """
        Метод возвращает все уникальные теги, которые включают слово, указанное в качестве аргумента.
        Отбросьте дубликаты. Это список тегов. Отсортируйте его по именам тегов в алфавитном порядке.
        """
        tags_with_word = list(set([x for x in self.datas['tag_2'] if word in x]))
        return tags_with_word


class Links:
    """
    Analyzing data from links.csv
    """

    def __init__(self, path_to_the_file, debug=False):
        self.file = path_to_the_file
        self.map_movie_imdb = Counter()
        self.imdb_info = None
        self.debug = debug

    def read_links(self):
        mas = []
        with open(self.file) as f:
            line = f.readline().split(',')
            if len(line) != 3:
                raise ValueError("не тот формат файла")
            for line in f:
                line = line.strip().split(',')
                self.map_movie_imdb[line[0]] = line[1]
                if not line[0].isdigit() or not line[1].isdigit():
                    raise ValueError("не тот формат файла")
                mas.append(line)
        self.table_links = mas

    def from_movie_to_imdb(self, list_of_movie):
        if len(self.map_movie_imdb) == 0:
            raise ValueError('файл не прочтен, используй read_links')
        # return (self.map_movie_imdb[i] for i in list_of_movie)
        return (self.map_movie_imdb[str(i)] for i in list_of_movie)

    def get_imdb(self, list_of_fields) -> list:
        """
        Метод возвращает список списков для списка фильмов, заданных в качестве аргумента (movieId).
        Например, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        Значения должны быть взяты из веб-страниц фильмов IMDB.
        Отсортируйте его по идентификатору фильма по убыванию.
        """
        try:
            self.read_links()
            list_of_imdf = self.from_movie_to_imdb(list_of_fields)
            imdb_info = []
            imdb_url = None
        except:
            raise ValueError('что то не так с input')
        try:
            for id_imdf, movieId in zip(list_of_imdf, list_of_fields):
                imdb_url = f"http://www.imdb.com/title/tt{id_imdf}/"
                response = requests.get(imdb_url)
                soup = BeautifulSoup(response.text, "html.parser")

                table_fields = soup.find('a', attrs={'class': 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'})
                directors = table_fields.get_text()

                table_fields = soup.find('h1', attrs={'data-testid': 'hero-title-block__title'})
                title = table_fields.get_text()

                table_fields2 = soup.find('section', attrs={'data-testid': "BoxOffice"})
                if table_fields2 != None:
                    table_fields2 = table_fields2.find('span', attrs={'class': "ipc-metadata-list-item__list-content-item"})
                    budgets = table_fields2.get_text()
                else:
                    budgets = '0,0,0'

                table_fields3 = soup.find('section', attrs={'data-testid': "BoxOffice"})
                if table_fields3 != None:
                    table_fields3 = table_fields3.find_all('span', attrs={'class': "ipc-metadata-list-item__list-content-item"})
                    cwg = table_fields3[-1].get_text()
                else:
                    cwg = '0,0,0'

                table_fields4 = soup.find('section', attrs={'data-testid': "TechSpecs"})
                table_fields4 = table_fields4.find('div', attrs={'class': "ipc-metadata-list-item__content-container"})
                runtime = table_fields4.get_text()

                imdb_info.append([movieId, title, directors, budgets, cwg, runtime])
                if self.debug:
                    print(imdb_info[-1])
        except:
            raise ValueError(f"проблема с {imdb_url, id_imdf, movieId}")


        self.imdb_info = sorted(imdb_info, key=lambda x: int(x[0]))
        return self.imdb_info

    def top_directors(self, n) -> dict:
        """
        The method returns a dict with top-n directors where the keys are directors and
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        if self.imdb_info is None:
            raise ValueError('таблички нет, используй get_imdb')
        directors = Counter()
        for line in self.imdb_info:
            directors[line[2]] += 1
        return dict(directors.most_common(n))

    def most_expensive(self, n) -> dict:
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        if self.imdb_info is None:
            raise ValueError('таблички нет, используй get_imdb')
        budgets = Counter()
        for line in self.imdb_info:
            budgets[line[1]] = float(''.join([i for i in line[3] if i.isdigit()]))
        return dict(budgets.most_common(n))

    def most_profitable(self, n) -> dict:
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
     Sort it by the difference descendingly.
        """
        if self.imdb_info is None:
            raise ValueError('таблички нет, используй get_imdb')
        profits = Counter()
        for line in self.imdb_info:
            budget = float(''.join([i for i in line[3] if i.isdigit()]))
            cwg = float(''.join([i for i in line[4] if i.isdigit()]))
            profits[line[1]] = cwg - budget
        return dict(profits.most_common(n))

    def longest(self, n) -> dict:
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version â€“ choose any.
        Sort it by runtime descendingly.
        ?????????
        """
        if self.imdb_info is None:
            raise ValueError('таблички нет, используй get_imdb')
        runtimes = Counter()
        for line in self.imdb_info:
            lines = line[5].split()
            runtimes[line[1]] = time(int(lines[0]), int(lines[2]))
        return dict(runtimes.most_common(n))

    def top_cost_per_minute(self, n) -> dict:
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the budgets divided by their runtime. The budgets can be in different currencies â€“ do not pay attention to it.
         The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        if self.imdb_info is None:
            raise ValueError('таблички нет, используй get_imdb')
        costs = Counter()
        for line in self.imdb_info:
            budgets = float(''.join([i for i in line[3] if i.isdigit()]))
            lines = line[5].split()
            run_time = time(int(lines[0]), int(lines[2]))
            costs[line[1]] = round(budgets / (run_time.hour * 60 + run_time.minute), 2)
        return dict(costs.most_common(n))

class Test:
    """
    Create tests using PyTest for each and every method of the classes above.
    They should check:
    * if the methods return the correct data types
    * if the lists elements have the correct data types
    * if the returned data sorted correctly 

    start:
    > py.test --capture=no movielens_analysis.py 

    https://doc.pytest.org/en/latest/explanation/goodpractices.html#conventions-for-python-test-discovery
    collection starts from the initial command line arguments which may be directories, filenames or test ids.
    recurse into directories, unless they match norecursedirs
    test_*.py or *_test.py files, imported by their package name.
    Test prefixed test classes (without an __init__ method) [<-- notice this one here]
    test_ prefixed test functions or methods are test items
    https://stackoverflow.com/questions/21430900/py-test-skips-test-class-if-constructor-is-defined
    """

    def test_type_of_return(self):
        test_tags_obj = Tags('data/tags.csv')
        test_rating_obj = Ratings('data/ratings.csv')
        test_link_obj = Links('data/links.csv')
        test_movie_obj = Movies('data/movies.csv')
        assert type(test_tags_obj.most_words(10)) == dict
        assert type(test_tags_obj.longest(10)) == list
        assert type(test_tags_obj.most_words_and_longest(10)) == list
        assert type(test_tags_obj.tags_with('funny')) == list
        assert type(test_tags_obj.most_popular(10)) == dict
        assert type(test_rating_obj.movies.dist_by_year()) == dict
        assert type(test_rating_obj.movies.dist_by_rating()) == dict
        assert type(test_rating_obj.movies.top_by_num_of_ratings(10)) == dict
        assert type(test_rating_obj.movies.top_by_ratings(10)) == dict
        assert type(test_rating_obj.movies.top_controversial(10)) == dict
        assert type(test_rating_obj.users.dist_by_users()) == dict
        assert type(test_rating_obj.users.dist_by_metric()) == dict
        assert type(test_rating_obj.users.top_controversial(10)) == dict
        assert type(test_link_obj.get_imdb([1])) == list
        assert type(test_link_obj.top_directors(10)) == dict
        assert type(test_link_obj.most_expensive(10)) == dict
        assert type(test_link_obj.most_profitable(10)) == dict
        assert type(test_link_obj.longest(10)) == dict
        assert type(test_link_obj.top_cost_per_minute(10)) == dict
        assert type(test_movie_obj.dist_by_release()) == dict
        assert type(test_movie_obj.dist_by_genres()) == dict
        assert type(test_movie_obj.most_genres(10)) == dict

    def test_type_of_inner_data(self):
        test_tags_obj = Tags('data/tags.csv')
        # test_rating_obj = Ratings('data/ratings.csv')
        test_link_obj = Links('data/links.csv')
        # test_movie_obj = Movies('data/movies.csv')
        assert type(test_tags_obj.longest(10)[0]) == str
        assert type(test_tags_obj.most_words_and_longest(10)[0]) == str
        assert type(test_tags_obj.tags_with('funny')[0]) == str
        assert type(test_link_obj.get_imdb([1])[0]) == list

    def test_of_sorting(self):
        test_tags_obj = Tags('data/tags.csv')
        test_rating_obj = Ratings('data/ratings.csv')
        test_link_obj = Links('data/links.csv')
        test_movie_obj = Movies('data/movies.csv')
        prev = 0
        for num, value in enumerate(test_movie_obj.dist_by_release().values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_movie_obj.dist_by_genres().values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_movie_obj.most_genres(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_rating_obj.movies.dist_by_year().keys()):
            if num != 0:
                assert prev <= value
            prev = value
        for num, value in enumerate(test_rating_obj.movies.dist_by_rating().keys()):
            if num != 0:
                assert prev <= value
            prev = value
        for num, value in enumerate(test_rating_obj.movies.top_by_num_of_ratings(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_rating_obj.movies.top_by_ratings(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_rating_obj.movies.top_controversial(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_rating_obj.users.dist_by_users().values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_rating_obj.users.dist_by_metric().values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_rating_obj.users.top_controversial(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_tags_obj.most_words(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_tags_obj.most_popular(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        test_link_obj.get_imdb([356,318,296,593])
        for num, value in enumerate(test_link_obj.top_directors(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_link_obj.most_expensive(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_link_obj.most_profitable(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_link_obj.longest(10).values()):
            if num != 0:
                assert prev >= value
            prev = value
        for num, value in enumerate(test_link_obj.top_cost_per_minute(10).values()):
            if num != 0:
                assert prev >= value
            prev = value

if __name__ == '__main__':
    print("Please, use movielens_report.ipynb for results")