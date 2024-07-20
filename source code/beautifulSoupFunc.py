from bs4 import BeautifulSoup
import requests


class scrapperBot:
    def __init__(self, URL):
        self.URL = URL
        self.areaList = None
        self.amountList = None
        self.ownerList = None

    def startScrapping(self):
        response = requests.get(self.URL)
        website_html = response.text

        soup = BeautifulSoup(website_html,"html.parser")

        self.areaList = soup.find_all(name='h2', class_='mb-srp__card--title')
        self.amountList = soup.find_all(name='div', class_='mb-srp__card__price--amount')
        self.ownerList =soup.find_all(name='div',class_='mb-srp__card__ads--name')
