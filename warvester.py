#!/usr/bin/python3
# warvester.py
import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# -- LOAD ENVIRONMENT VARIABLES -- #

load_dotenv()
CHROMEDRIVER_BINARY_PATH = os.environ.get('CHROMEDRIVER_BINARY_PATH')
CHROME_BINARY_PATH = os.environ.get('CHROME_BINARY_PATH')


def get_webdriver() -> webdriver.chrome.webdriver.WebDriver:
    service = Service(CHROMEDRIVER_BINARY_PATH)

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    # If running with a non-default chrome path
    if CHROME_BINARY_PATH:
        options.binary_location = CHROME_BINARY_PATH

    return webdriver.Chrome(service=service, options=options)


def get_soup(url: str, dynamic: bool = False) -> BeautifulSoup:
    if dynamic:
        driver = get_webdriver()
        driver.get(url)

        driver.implicitly_wait(15)

        html = driver.page_source
        driver.close()
    else:
        request = requests.get(url)
        html = request.content
    return BeautifulSoup(html, 'html.parser')
