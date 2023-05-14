# Define a function to scrape a webpage for publicaly availabel data in python using beautiful soup
# This function is called by the main script to scrape the data from the webpage
# The data is then written to a csv file for further analysis

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.adelsvapen.com/genealogi/Abrahamsson_-_von_D%C3%B6beln"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')