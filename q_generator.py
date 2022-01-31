from asyncio.windows_events import NULL
from string import printable
from turtle import title
from webbrowser import get
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dateutil.parser import parse
from selenium.webdriver.chrome.options import Options
from random import random, uniform, randint
from time import sleep

data = []
clubs =[]


if __name__ == '__main__':
    t = open("data.txt","w",encoding='utf8')

    for i in range(1,100):
        x = "call nations_trophies ( " + str(i) + ");"
        print (x, file=t)
    t.close()