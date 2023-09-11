
# -*- coding: utf-8 -*-
"""
Created on a cloudy day
@Student Name: Christopher O Grady
@Student id: R00067022
@Cohort: ???
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv("movie_metadata.csv", encoding="ISO-8859-1")


# average imdb score
# director is also the first, second, third actor then not an actor
def Task1():
    # required columns
    director = df['director_name']
    actor1 = df['actor_1_name']
    actor2 = df['actor_2_name']
    actor3 = df['actor_3_name']

    # mean of required data
    imdb_a = (df['imdb_score'][director == actor1]).mean()
    print("1st actor", imdb_a)
    imdb_b = (df['imdb_score'][director == actor2]).mean()
    print("2nd actor", imdb_b)
    imdb_c = (df['imdb_score'][director == actor3]).mean()
    print("3rd actor", imdb_c)
    imdb_d = (df['imdb_score'][director != actor3][director != actor2][director != actor1]).mean()
    print("Not acting", imdb_d)

    # implementation of bar chart
    appearance = ['1st actor', '2nd actor', '3rd actor', 'not acting']
    average_imdb = [imdb_a, imdb_b, imdb_c, imdb_d]

    plt.bar(appearance, average_imdb)
    plt.title('Imdb per director appearance')
    plt.xlabel('Appearance as')
    plt.ylabel('Average Imdb')
    plt.grid(True)
    plt.show()

    statement = \
        "While minimal, there is a difference in movie ratings where the director does act in, with the director " \
        "acting first the movie seems to be received better.\nThis may indicate a greater effort from the director " \
        "to make the movie better if they put their face first in it "
    print(statement)


# data clean Type, display number of 'Color' and ' Black and White'
def Task2():
    # cleaning mis-entered data, may not be efficient or scalable
    # print(df['Type'].value_counts()) to find what data was stored
    df['Type'][df['Type'] == 'Black White'] = ' Black and White'
    df['Type'][df['Type'] == ' Black and white'] = ' Black and White'
    df['Type'][df['Type'] == ' Black andWhite'] = ' Black and White'
    df['Type'][df['Type'] == ' Black and Wite'] = ' Black and White'
    df['Type'][df['Type'] == ' Black And White'] = ' Black and White'
    df['Type'][df['Type'] == ' Black and Whit'] = ' Black and White'
    df['Type'][df['Type'] == 'Black Wite'] = ' Black and White'
    df['Type'][df['Type'] == ' Blackand White'] = ' Black and White'
    df['Type'][df['Type'] == ' Black And white'] = ' Black and White'
    color = (df['Type'][df['Type'] == 'Color'])
    black_and_white = (df['Type'][df['Type'] == ' Black and White'])

    # pie chart was chosen to represent findings and the difference to be easily visible
    # Color movies are by far the most popular
    palette = [len(color), len(black_and_white)]
    color_label = "Color " + str(len(color))
    black_white_label = "Black and white " + str(len(black_and_white))
    labels = [color_label, black_white_label]
    f = plt.figure()
    f.set_size_inches(10, 5)

    plt.pie(palette, shadow=True, startangle=90, autopct='%0.1f%%', pctdistance=1.1,
            labeldistance=1.3, labels=labels)
    plt.annotate('Majority of movies are color', xy=(1, 0.5), xytext=(1, 1),
                 arrowprops=dict(arrowstyle="->"))
    plt.show()


# Get every unique genre, may be more than one '|'
# Find the top 5 most popular
# Apply visualization to depict the population of each genre
def Task3():
    # dropping null
    cf = df.dropna(subset=['genres'])
    # getting all uniques
    genres = pd.unique(cf['genres'])
    # making an array to split at | to hold ALL values
    values = []
    for g in genres:
        f = g.split("|")
        for i in f:
            values.append(i)
    # converting back to DF with index of same length
    index1 = list(range(0, len(values)))
    temp = pd.Series(values, index=[index1])
    genre_series = pd.DataFrame({'genre': temp})

    # getting all unique genres
    genre_list = [genre_series['genre'].unique()]
    genre_counts = genre_series['genre'].value_counts()
    print("Unique Genres:\n", genre_list)
    print("\nMost popular:\n", genre_series['genre'].value_counts().head(5))

    # attempted, not implemented correctly
    plt.hist(genre_series)
    plt.show()


def Task4():
    #bf = df.dropna(subset=['duration'])
    # drop null
    dur = df['duration'].dropna()
    # make boxplot
    vis = plt.boxplot(dur)
    plt.xlabel("Duration")
    print("Min: ", vis['whiskers'][0].get_xydata()[1][1])
    print("Max: ", vis['whiskers'][1].get_xydata()[1][1])
    print("Median: ", vis['medians'][0].get_xydata()[0][1])
    print("First Quartile: ", vis['whiskers'][0].get_xydata()[0][1])
    plt.show()

    # did not get graph working as intended
    sorted1 = dur.sort_values(ascending=[True])
    plt.plot(sorted1)
    plt.show()


def Task5():
    # dropping null
    cf = df.dropna(subset=['budget'])
    # getting required medians and ranges
    c = (cf['budget']).median()
    sub1 = cf[cf['budget'] < c]
    sub2 = cf[cf['budget'] > c]
    a = (sub1['budget']).median()
    b = (sub2['budget']).median()
    # defining our target set
    targetSet = cf[(cf['budget'] > a) & (cf['budget'] < b)]
    #print(targetSet)
    plt.hist(targetSet['budget'], bins=40)
    plt.show()


def main():
    #Task1()
    #Task2()
    #Task3()
    #Task4()
    Task5()


main()

