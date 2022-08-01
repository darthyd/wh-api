import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def getData():
    my_list = []

    url_base = 'https://sports.williamhill.com/betting/en-gb/football/matches/competition/today/match-betting'

    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
    option = Options()
    option.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
    option.add_argument('--headless')
    option.add_argument('window-size=1920x1080')
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    nav = webdriver.Chrome(executable_path=str(
        os.environ.get('CHROMEDRIVER_PATH'), option=option))

    nav.get(url_base)

    sleep(5)

    html = nav.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)

    sleep(2)

    html.send_keys(Keys.END)

    sleep(2)

    games = nav.find_elements(
        By.CSS_SELECTOR, '.sp-o-market__title > a')

    for item in games:
        item = item.get_attribute('outerHTML')

        soup = BeautifulSoup(item, 'html.parser')
        link = soup.find('a')['href']
        game = soup.find('a').get('title')
        home = game.split(' v ')[0]
        away = game.split(' v ')[1]
        id = link.split('OB_EV')[1].split('/')[0]

        my_list.append({'game': game, 'home': home,
                       'away': away, 'id': id, 'link': link})

    nav.quit()

    return my_list
