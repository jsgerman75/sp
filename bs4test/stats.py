from bs4 import BeautifulSoup
import requests
import csv


with open('axiomatic.html') as source:
    soup = BeautifulSoup(source, 'lxml')

#<div class="card-heading">[1]
print(soup.find("div", class_"card-heading")[1])
