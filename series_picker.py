from bs4 import BeautifulSoup
from random import randrange
import requests
import time

url = 'https://www.imdb.com/chart/toptv'

def movie_picker():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html,"html.parser")
    series_tag = soup.select('td.titleColumn')
    series_innertag = soup.select('td.titleColumn a')
    ratings_tag = soup.select('td.posterColumn span[name = ir]')

    def all_years(series_year):
        series_split = series_year.text.split()
        year = series_split[-1]
        return year

    years = [all_years(year) for year in series_tag]
    actors_list = [tag["title"] for tag in series_innertag]
    title_list = [tag.text for tag in series_innertag]
    ratings_list = [float(tag['data-value']) for tag in ratings_tag]

    t_len = len(title_list)
    
    while True:
        inx = randrange(0,t_len)

        print(f"Python Suggestion: {title_list[inx]}, cast includes {actors_list[inx]}.It is released in the year {years[inx][1:5]}.It has an IMDB rating of {ratings_list[inx]:.1f}")

        user_input = input("Already watched? Do you want another suggestion? ['y'/[n]]\n")

        if user_input != "y":
            print("Enjoy the series")
            time.sleep(5)
            break

if __name__ == '__main__':
    movie_picker()