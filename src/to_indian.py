import random
from src.helpers import *


def to_indian(ingreds):
    spices = [line.strip() for line in open('spices.txt')]
    sauces = [line.strip() for line in open('sauces.txt')]
    indian_spices = [line.strip() for line in open('indian_spices.txt')]
    indian_sauces = [line.strip() for line in open('indian_sauces.txt')]
    breads = [line.strip() for line in open('breads.txt')]
    cheeses = [line.strip() for line in open('cheeses.txt')]
    red_meats = [line.strip() for line in open('red_meats.txt')]
    ans_spices = unibigrams(spices)
    ans_sauces = unibigrams(sauces)
    ans_cheese = unibigrams(cheeses)
    ans_rm = unibigrams(red_meats)
    ans_breads = unibigrams(breads)

    new_dict = {}
    for key, value in ingreds.items():
        new_value = [value[0], value[1], value[2], value[3]]
        start = len(new_dict)
        i = 0
        name = word_tokenize(key)
        if len(name) == 1:
                #print(name)
            if name[0] in ans_spices['unigrams']:
                i = 1
                new_key = key.replace(key, random.choice(indian_spices))
                new_dict[new_key] = new_value
            elif x in ans_sauces['unigrams']:
                i = 1
                new_key = key.replace(key, random.choice(indian_sauces))
                new_dict[new_key] = new_value
            elif x == 'rice':
                i = 1
                new_key = key.replace(key, 'basmati rice')
                new_dict[new_key] = new_value
            elif name in breads:
                i = 1
                new_key = key.replace(key, 'naan')
                new_dict[new_key] = new_value
            elif name in red_meats:
                i = 1
                new_key = key.replace(key, 'chicken')
                new_dict[new_key] = new_value
            elif name in cheeses:
                i = 1
                new_key = key.replace(key, 'paneer')
                new_dict[new_key] = new_value
            else:
                new_dict[key] = value

        if len(name) == 2:
            if name in ans_spices['bigrams']:
                i = 1
                new_key = key.replace(key, random.choice(indian_spices))
                new_dict[new_key] = new_value
            elif name in ans_sauces['bigrams']:
                i = 1
                new_key = key.replace(key, random.choice(indian_sauces))
                new_dict[new_key] = new_value
            elif name in ans_breads['bigrams']:
                i = 1
                new_key = key.replace(key, 'naan')
                new_dict[new_key] = new_value
            elif name in ans_rm['bigrams']:
                i = 1
                new_key = key.replace(key, 'chicken')
                new_dict[new_key] = new_value
            elif name in ans_cheese['bigrams']:
                i = 1
                new_key = key.replace(key, 'paneer')
                new_dict[new_key] = new_value
            else:
                new_dict[key] = value
        if len(name) == 3:
            if name in ans_spices['trigrams']:
                i = 1
                new_key = key.replace(key, random.choice(indian_spices))
                new_dict[new_key] = new_value
            elif name in ans_sauces['trigrams']:
                i = 1
                new_key = key.replace(key, random.choice(indian_sauces))
                new_dict[new_key] = new_value
            elif name in ans_breads['trigrams']:
                i = 1
                new_key = key.replace(key, 'naan')
                new_dict[new_key] = new_value
            elif name in ans_rm['trigrams']:
                i = 1
                new_key = key.replace(key, 'chicken')
                new_dict[new_key] = new_value
            elif name in ans_cheese['trigrams']:
                i = 1
                new_key = key.replace(key, 'paneer')
                new_dict[new_key] = new_value
            else:
                new_dict[key] = value
    return new_dict

