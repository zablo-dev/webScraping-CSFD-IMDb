from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.csfd.cz/zebricky/filmy/nejlepsi/'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

movies = soup.find_all('article', class_ = 'article article-poster-60')

#print(len(movies))


csv_filename = 'filmy_data.csv'

with open(csv_filename, mode = 'w', newline='', encoding='utf-8-sig') as file:
    writer=csv.writer(file)

    header = ['rank', 'name', 'year', 'director', 'rating']
    writer.writerow(header)

    for movie in movies:
        name = movie.find('div', class_ = 'article-content article-content-toplist').a.text
        rank = movie.find('div', class_ = 'article-content article-content-toplist').span.text
        year = movie.find('span', class_ = 'info').text.strip('()')
        director = movie.find('p', class_ = 'film-creators').text.split(':')[1]
        rating = movie.find('div', class_ = 'rating-average red').text
        # print(rating)
        # break

        writer.writerow([rank, name, year, director, rating])

print("Data byla uložena do tohoto csv file:", csv_filename)

##TODO Lze definovat funkci -> dat do ni main obsah -> a nastavit aby sbirani dat probihalo v intervalech (10-15min) ,neni potreba zde 