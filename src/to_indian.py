import random
from src.helpers import *

def to_indian(ingredients):
	subs = []
	ing_spices = []
	spices = [line.strip() for line in open('spices.txt')]
	sauces = [line.strip() for line in open('sauces.txt')]
	indian_spices = [line.strip() for line in open('indian_spices.txt')]
	indian_sauces = [line.strip() for line in open('indian_sauces.txt')]
	breads = [line.strip() for line in open('recipes/breads.txt')]
	cheeses = [line.strip() for line in open('recipes/cheeses.txt')]
	red_meats = [line.strip() for line in open('recipes/red_meats.txt')]
	ans_spices = unibigrams(spices)
	ans_sauces = unibigrams(sauces)

	for x in ingredients.keys():
		name = word_tokenize(x)
		if len(name) == 1:
			if x in ans_spices['unigrams']:
				subs.append([x, random.choice(indian_spices)])
			if x in ans_sauces['unigrams']:
				subs.append([x, random.choice(indian_sauces)])
		if len(name) == 2:
			if name in ans_spices['bigrams']:
				subs.append([name, random.choice(indian_spices)])
			if name in ans_sauces['bigrams']:
				subs.append([name, random.choice(indian_sauces)])
			if len(name) == 3:
				if name in ans_spices['trigrams']:
					subs.append([name, random.choice(indian_spices)])
				if name in ans_sauces['trigrams']:
					subs.append([name, random.choice(indian_sauces)])
		if x == 'rice':
			subs.append([x,'basmati rice'])
		if x in breads:
			subs.append([x, 'naan'])
		if x in red_meats:
			subs.append([x, 'chicken'])
		if x in cheeses:
			subs.append([x, 'paneer'])
	return subs

def printSubs(subs):
	for x in subs:
		print("Substitute " + x[0] + " with " + x[1])
