import requests
from bs4 import BeautifulSoup

def main(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	raw_directions = [span.text for span in soup.find('ol', {'class': 'recipe-directions__list'}).find_all('span', 'recipe-directions__list--item')]
	directions = []

	for d in raw_directions:
		i = len(d) - 1
		while i >= 0 and d[i] in [' ', '\\', 'n']:
			i -= 1
		directions.append(d[:i])

	return directions

main('https://www.allrecipes.com/recipe/218068/smoky-grilled-pork-chops/')