#!/usr/bin/env python3
from urllib.request
import urlopen
from bs4 import BeautifulSoup
import ssl
import csv

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup.find("section")
column_name  = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})

price = []
rating = []
title = []

for child in column_name:
	for child_div in child.find_all("div"):
		for price_color in child_div.find_all("p",{"class" :"price_color"}):
			text = price_color.get_text()
			price.append(text)

	for child_h3 in child.find_all("h3"):
		title_text = child_h3.get_text()
		title.append(title_text)

	for child_article in child.find_all("article",{"class":"product_pod"}):
		attr = child_article.findChildren("p")[0]
		rate = attr.get("class")[1]
		rating.append(rate)

lst = list(zip(title,price,rating))
file = open("scrape_html_file.csv","w")
file.write("'title' , 'price' , 'rate'")
file.write("\n")

for item in lst:
	row_string = '"{}","{}","{}"'.format(item[0], item[1], item[2])
	file.write(row_string)
	file.write("\n")

file.close()
