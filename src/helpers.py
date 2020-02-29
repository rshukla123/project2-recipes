from nltk import TweetTokenizer as tokenizer

def get_ngrams(n, s):
	return [' '.join(s[i:i+n]) for i in range(len(s) - n + 1)]

def clean_string(s, sw):
	return [tkn.lower() for tkn in s if tkn not in sw]

def tokenize_string(s):
	return tokenizer().tokenize(s)
