from bs4 import BeautifulSoup
import os
import time 
from requests_html import HTMLSession
import requests
import cloudscraper
from selenium import webdriver


os.environ['PATH'] += r"C:/Users/DELL/Downloads/webdriver"

session = HTMLSession()
browser = webdriver.Chrome()
scraper = cloudscraper.create_scraper()


# initializing some variable used 
episode_url_list = []
episode_download_list = []

anime_input = """What anime would you like to download?
>> """
anime_input = input(anime_input).lower()

anime_input = "https://www1.gogoanime.ee/category/" + anime_input

link = browser.get(anime_input)
browser.implicitly_wait(10)
link = browser.page_source
soup = BeautifulSoup(link, 'html.parser')
print(soup)

episode_link_list = soup.find_all("ul", id="episode_related")
episode_number_list = soup.find_all("div", class_="name")
print(episode_link_list)
browser.quit()
