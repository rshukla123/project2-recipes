import sys
import requests
import nltk
import itertools
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
from string import punctuation


def get_recipe_data(url):
	sw = set(stopwords.words('english'))
	punc = [p for p in punctuation]
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	recipe_data = {
		'raw_ingredients': [],
		'directions': []
	}

	try:
		raw_directions = [span.text for span in soup.find('ul', {'class': 'instructions-section'}).find_all('p')]
	except AttributeError:
		raw_directions = [span.text for span in soup.find('ol', {'class': 'recipe-directions__list'}).find_all('span', {'class': 'recipe-directions__list--item'})]

	for d in raw_directions:
		i = len(d) - 1
		while i >= 0 and d[i] in [' ', '\\', 'n']:
			i -= 1

		recipe_data['directions'].append(d[:i])

	return recipe_data
