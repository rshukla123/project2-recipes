import sys
import nltk
import json
import itertools

def get_verb_vars(v):
	return [
		v + 'ing',
		v[:-1] + 'ing',
		v + 'ed',
		v + 'd',
		v + 's'
	]

def get_noun_vars(n):
	return [
		n + 'er',
		n + 'r'
	]

def method_check(word, method, method_info):
	return (
		word == method or
		word in get_verb_vars(method) or
		any([
			word == syn or
			word in get_verb_vars(syn)
			for syn in method_info['synonyms']
		]) or
		any([
			word == tool or
			word in get_noun_vars(tool)
			for tool in method_info['tools']
		])
	)

def query_methods(directions):
	with open('data/methods.json', 'r') as f:
		method_data = json.load(f)
	f.close()

	raw_jumble = list(itertools.chain.from_iterable(directions))
	jumble = [j for j in raw_jumble if j.isalpha() and len(j) > 1]

	counter = {}
	for word in jumble:
		for method in method_data:
			if method_check(word, method, method_data[method]):
				counter[method] = 1 if method not in counter else counter[method] + 1

	sorted_methods = [d for d in sorted(counter, key=counter.get, reverse=True)]

	return {
		'main': sorted_methods[0],
		'methods': sorted_methods
	}
