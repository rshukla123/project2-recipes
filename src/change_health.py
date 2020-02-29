import sys
import json

from src.helpers import *

def change_health(make_healthier, ingredients, directions):
	with open('data/healthy.json', 'r') as f:
		health_json = json.load(f)
	f.close()

	health_data = {}
	if make_healthier:
		for pair in health_json:
			health_data[pair[0]] = pair[1]
	else:
		for pair in health_json:
			health_data[pair[1]] = pair[0]

	new_directions = []

	for direction in directions:
		new_direction = direction
		for n in reversed(range(1, 5)):
			for ngram in get_ngrams(n, tokenize_string(direction)):
				if ngram.lower() in health_data.keys():
					new_direction = new_direction.replace(ngram, health_data[ngram])
		new_directions.append(new_direction)

	return new_directions
