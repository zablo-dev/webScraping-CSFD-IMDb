from bs4 import BeautifulSoup
import requests
import csv

url = 'https://twitchtracker.com/channels/ranking'

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')


streamers = soup.find_all('tr')

#print(len(streamer))

csv_filename = 'streamers_data.csv'

with open(csv_filename, mode = 'w', newline='', encoding='utf-8-sig') as file:
    writer=csv.writer(file)

    header = []
    writer.writerow(header)

    for streamer in streamers:
        avg_viewers = streamer.find('span', class_ = 'color-viewers')
        print(avg_viewers)
        break



 