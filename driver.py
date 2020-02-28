from get_recipe_data import get_recipe_data
from src.query_methods import query_methods

def main(url):
	recipe_data = get_recipe_data(url)

	methods = query_methods(recipe_data['directions'])

	print(methods)

if __name__== '__main__':
	url = 'https://www.allrecipes.com/recipe/276149/indian-chicken-saag/?internalSource=staff%20pick&referringId=201&referringContentType=Recipe%20Hub&clickId=cardslot%201'
	main(url)
