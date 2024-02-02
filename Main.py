## WEB SCRAPING HTML BASICS

from bs4 import BeautifulSoup ## knihovna pro web scraping

with open("home.html", "r") as html_file:   ## Nahrani dokumentu
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    course_cards = soup.find_all("div", class_= "card")

    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs  {course_price}')


from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.csfd.cz/zebricky/filmy/nejlepsi/").text


soup = BeautifulSoup(html_text, "lxml")
film = soup.find("article", class_="article article-poster-60")

