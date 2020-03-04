import sys

from get_recipe_data import get_recipe_data

from src.parse_ingredients import parse_ingredients
from src.query_methods import query_methods
from src.query_tools import query_tools
from src.query_steps import query_steps

from src.change_health import change_health
from src.to_indian import to_indian

from src.helpers import *

def main():
	print('Welcome to the Recipe Transformer!\n')
	url = input('Please enter the url of a recipe:\n>> ')

	recipe_data = get_recipe_data(url)

	print('\n' + recipe_data['title'] + '\n')

	ingredients = parse_ingredients(recipe_data['ingredients'])
	methods = query_methods(recipe_data['directions'])
	tools = query_tools(ingredients, recipe_data['directions'])

	steps = query_steps(ingredients, recipe_data['directions'], tools, methods['methods'])
	print_recipe(steps)

	transform = input('\nPlease enter the number of your desired transformation:\n'
		'1: Healthier\n'
		'2: Unhealthier\n'
		'3: Vegetarian\n'
		'4: Non-Vegetarian\n'
		'5: Indian\n'
		'6: Mediterranean\n'
		'>> ')

	if transform == '1':
		new_recipe = change_health(True, steps)
	elif transform == '2':
		new_recipe = change_health(False, steps)
	elif transform == '5':
		new_recipe = to_indian(steps)

	print(new_recipe)

	print('\nBon Appetit!')

if __name__== '__main__':
	main()
