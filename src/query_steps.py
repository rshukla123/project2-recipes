import json

def query_steps(ingredients, directions, tools, methods):
	print(methods)
	time_units = {'second', 'sec', 'minute', 'min', 'hour', 'hr'}

	with open('data/methods.json', 'r') as f:
		all_methods = json.load(f)

	steps = []

	for direc in directions:
		step = {}

		step['time'] = 0
		has_time = set(direc).intersection(time_units)
		if has_time:
			time_index = direc.index(has_time[0])
			if time_index > 0 and direc[time_index - 1].isnumeric():
				step['time'] = {
					'duration': direc[time_index - 1],
					'unit': direc[time_index]
				}

		step['tools'] = set(tools).intersection(set(direc))
		# step['ingredients'] = set([i['name'] for i in ingredients]).intersection(set(direc))
		step['methods'] = [
			m for m in all_methods
			if m in direc or
				any([syn in direc for syn in all_methods[m]['synonyms']])
		]

		steps.append(step)

	return steps