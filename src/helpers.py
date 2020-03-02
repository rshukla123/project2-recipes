from nltk import TweetTokenizer as tokenizer
from nltk.tokenize import word_tokenize

def get_ngrams(n, s):
	return [' '.join(s[i:i+n]) for i in range(len(s) - n + 1)]

def clean_string(s, sw):
	return [tkn.lower() for tkn in s if tkn not in sw]

def tokenize_string(s):
	return tokenizer().tokenize(s)


def unibigrams(input_list):
	
	tokenized = []
	uni = []
	bi = []
     	tri = []
	results = {}
	for x in input_list:
		tokenized.append(word_tokenize(x))
	for x in tokenized:
		if len(x) == 1:
			for i in x:
				uni.append(i)
		if len(x) == 2:
			bi.append(x)
          	if len(x) == 3:
               		tri.append(x)
	results['unigrams'] = uni
     	results['bigrams'] = bi
     	results['trigrams'] = tri
	return results
