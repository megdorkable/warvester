#!/usr/bin/python3
# warvester.py
import os
import requests
from typing import List
import bs4
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# -- LOAD ENVIRONMENT VARIABLES -- #

load_dotenv()
CHROMEDRIVER_BINARY_PATH = os.environ.get('CHROMEDRIVER_BINARY_PATH')
CHROME_BINARY_PATH = os.environ.get('CHROME_BINARY_PATH')


class Tag:
    pass


class Tag:
    def __init__(self, tag: bs4.element.Tag):
        self.tag: bs4.element.Tag = tag
        self.name: str = tag.name
        self.text: str = tag.text
        self.attrs: dict = tag.attrs

    def __repr__(self):
        return self.tag.prettify()

    def __str__(self):
        return self.tag.prettify()

    def __getitem__(self, item):
        return self.attrs[item]

    def get_text(self, *args, **kwargs) -> str:
        return self.tag.get_text(*args, **kwargs)

    def find(self, tag: str = None, attrs: dict = {}, *args, **kwargs) -> Tag:
        return Tag(self.tag.find(name=tag, attrs=attrs, *args, **kwargs))

    def find_all(self, tag: str = None, attrs: dict = {}, *args, **kwargs) -> List[Tag]:
        return [Tag(tag) for tag in self.tag.find_all(name=tag, attrs=attrs, *args, **kwargs)]


class Soup(Tag):
    def __init__(self, url: str, dynamic: bool = False):
        self.url: str = url
        self.soup: BeautifulSoup = self.__get_soup(url=url, dynamic=dynamic)
        super().__init__(tag=self.soup)

    @staticmethod
    def __get_webdriver() -> webdriver.chrome.webdriver.WebDriver:
        service = Service(CHROMEDRIVER_BINARY_PATH)

        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        # If running with a non-default chrome path
        if CHROME_BINARY_PATH != 'default':
            options.binary_location = CHROME_BINARY_PATH

        return webdriver.Chrome(service=service, options=options)

    @staticmethod
    def __get_soup(url: str, dynamic: bool = False) -> BeautifulSoup:
        if dynamic:
            driver = Soup.__get_webdriver()
            driver.get(url)

            driver.implicitly_wait(15)

            html = driver.page_source
            driver.close()
        else:
            request = requests.get(url)
            html = request.content
        return BeautifulSoup(html, 'html.parser')
