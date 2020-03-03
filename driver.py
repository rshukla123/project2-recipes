from get_recipe_data import get_recipe_data

from src.query_methods import query_methods
from src.query_tools import query_tools
from src.query_steps import query_steps

from src.change_health import change_health
from src.to_indian import to_indian

def main():
	print('Welcome to the Recipe Transformer!\n')
	url = input('Please enter the url of a recipe:\n>> ')

	recipe_data = get_recipe_data(url)

	methods = query_methods(recipe_data['directions'])
	tools = query_tools(recipe_data['raw_ingredients'], recipe_data['directions'])

	steps = query_steps([], recipe_data['directions'], tools, methods['methods'])
	for s in steps:
		print(s)

	transform = input('Please enter the number of your desired transformation:\n'
		'1: Healthier\n'
		'2: Unhealthier\n'
		'3: Vegetarian\n'
		'4: Non-Vegetarian\n'
		'5: Indian\n'
		'>> ')

	if transform == '1':
		healthier = change_health(True, recipe_data['raw_ingredients'], recipe_data['directions'])
		print(healthier)
	elif transform == '2':
		unhealthier = change_health(False, recipe_data['raw_ingredients'], recipe_data['directions'])
		print(unhealthier)
	elif transform == '5':
		indian = to_indian()

	print('\nBon Appetit!')

if __name__== '__main__':
	main()
