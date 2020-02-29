from get_recipe_data import get_recipe_data
from src.query_methods import query_methods
from src.change_health import change_health

def main():
	print('Welcome to the Recipe Transformer!')
	url = input('Please enter the url of a recipe:\n>> ')

	recipe_data = get_recipe_data(url)

	methods = query_methods(recipe_data['directions'])
	print(methods)

	transform = input('Please enter the number of your desired transformation:\n'
		'1: Healthier\n'
		'2: Unhealthier\n'
		'3: Vegetarian\n'
		'4: Non-Vegetarian\n'
		'>> ')

	if transform == '1':
		healthier = change_health(True, recipe_data['raw_ingredients'], recipe_data['directions'])
		print(healthier)
	elif transform == '2':
		unhealthier = change_health(False, recipe_data['raw_ingredients'], recipe_data['directions'])
		print(unhealthier)

	print('\nBon Appetit!')

if __name__== '__main__':
	main()
