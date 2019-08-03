import argparse
import json
import os
import urllib

from bs4 import BeautifulSoup
import requests

class Sister_Search():
	def __init__(self):
		self.GOOGLE_SEARCH_URL = "https://www.google.co.jp/search"
		self.session = requests.session()
		
	def search(self, keyword, maximum):
		print("searching {keyword}")
		query = self.query_gen(keyword)
		return self.image_search(query,maximum)

	def image_search(self,query_gen,maximum):


def main():

if __name__ == "__main__":
    main()