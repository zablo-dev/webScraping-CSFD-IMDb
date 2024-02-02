from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.imdb.com/chart/top/'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')


movies = soup.find_all('li', class_ = 'ipc-metadata-list-summary-item sc-1364e729-0 caNpAE cli-parent')

#print(len(movies))

csv_filename = 'movies_data.csv'

with open(csv_filename, mode = 'w', newline='', encoding='utf-8-sig') as file:
    writer=csv.writer(file)

    header = ['Rank', 'Name', 'Year', 'Rating']
    writer.writerow(header)

    for movie in movies:
        name = movie.find('div', class_ = 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title').a.text.split('.')[1]
        rank = movie.find('div', class_ = 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title').a.text.split('.')[0] 
        year = movie.find('div', class_ = 'sc-be6f1408-7 iUtHEN cli-title-metadata').span.text
        rating = movie.find('div', class_ = 'sc-e2dbc1a3-0 ajrIH sc-be6f1408-2 dAeZAQ cli-ratings-container').span.text.split()[0]
       
        writer.writerow([rank, name, year, rating])
       
#print("Data byla uložena do tohoto csv file:", csv_filename)       
        # print(rating)
        # break

##TODO Lze vytvorit funkci -> dat do ni main obsah -> a nastavit aby sbirani dat probihalo v intervalech (10-15min) neni potreba zde 