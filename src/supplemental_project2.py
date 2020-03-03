import requests
from bs4 import BeautifulSoup
from nltk.tokenize import TweetTokenizer
import re
import nltk
import fractions

def make_veg(i_dict):
    new_dict = {}
    meat = ['beef', 'chicken', 'pork', 'salmon', 'tuna', 'sausage', 'veal', 'turkey', 'duck', 'goat', 'lamb', 'meatball', 
            'shrimp', 'crab', 'lobster', 'hot dog', 'bacon', 'ham', 'burger', 'patty', 'pork', 'meat']
     
    for key, value in i_dict.items():
        new_value = [value[0], value[1], [], []]
        start = len(new_dict)
        i = 0
        for m in meat:
            if m in key:
                i = 1
                new_key = key.replace(m, 'tofu')
                new_dict[new_key] = new_value
                
        if len(new_dict) == start:
            if i == 1:
                new_key = key.replace(m, 'seitan')
                new_dict[new_key] = new_value
            else:
                new_dict[key] = value
    return new_dict



def double_amount(i_dict):
    for key, value in i_dict.items():
        if '/' in value[0]:
            fraction_obj = sum(map(fractions.Fraction, value[0].split()))
            doubled = fraction_obj + fraction_obj
            n = doubled.numerator 
            d = doubled.denominator 
            if str(n) == str(d):
                amount = '1'
            else:
                amount = str(n) + str('/') + str(d)
            i_dict[key] = [amount, value[1], value [2], value[3]] 
        elif value[0].isnumeric():
            amount = int(value[0]) * 2
            i_dict[key] = [amount, value[1], value [2], value[3]]
        else:
            i_dict[key] = value
    return i_dict
        


def make_meat(i_dict):
    new_dict = {}
    subs = ['tofu', 'eggplant', 'seitan', 'jackfruit']
    i = 0
    for key, value in i_dict.items():
        new_value = [value[0], 'pound(s)', [], []]
        start = len(new_dict)
        
        for m in subs:
            if m in key:
                i = i + 1
                new_key = key.replace(m, 'chicken')
                new_dict[new_key] = new_value
                
        if len(new_dict) == start:
                new_dict[key] = value
    if i == 0:
        new_dict['chicken'] = [1, 'pound', [], []]
    
    return new_dict