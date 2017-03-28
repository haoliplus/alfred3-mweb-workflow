#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys,os
from bs4 import BeautifulSoup

class Articles:

    def __init__(self, path):
        self.archives_path = os.path.join(path, "archives.html")
        if os.path.isfile(self.archives_path):
            self.archives_content = open(self.archives_path).read()
        else:
            self.archives_content = ""
        soup = BeautifulSoup(self.archives_content,"html.parser")
        self.articles = []
        for item in soup.find_all('div','article'):
            article = {}
            article['title']= item.find('h1').get_text()
            article['link'] = item.find('a','clearlink').get('href')
            article['date']= item.find('span','date').get_text()
            article['category'] = ' '.join([x.get_text() for x in item.find_all('span','posted-in')])
            self.articles.append(article)

if __name__ == "__main__":
    a = Articles("/Users/hao/blog/MWeb-Blog/Blog")
    for i in a.articles:
        print i['title']

