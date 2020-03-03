import nltk
from src.helpers import unibigrams
from nltk.tokenize import word_tokenize

def query_tools(ingredients, directions):
    tokenized = []
    pos = []
    nouns = []
    tools = []
    ings = []
    final_tools = []
    bi = []
    arr_bi = []
    arr_tri = []

    # tokenize directions
    for x in directions:
        tokenized.append(word_tokenize(x))
    # get pos tag and bigrams
    for x in tokenized:
        pos.append(nltk.pos_tag(x))
        bi.append(list(nltk.bigrams(x)))
    # only look at nouns
    for x in pos:
        for y in x:
            if y[1] == 'NN':
                nouns.append(y[0])
    # put bigrams and trigrams in arrays instead of lists
    for x in bi:
        for y in x:
           # print(y)
            i = []
            for j in y:
                i.append(j.lower())
            arr_bi.append(i)
    for x in trigrams:
        for y in x:
            i = []
            for j in y:
                i.append(j)
            arr_tri.append(i)
    
    #get ingredient names - don't consider words that are in ingredients
    for x in thisdict.keys():
        ings.append(x)
    for x in nouns:
        if not x in ings:
            tools.append(x)

    gen_tools = set([line.strip() for line in open('general_tools.txt')])
    ans_tools = unibigrams(gen_tools)

    for x in tools:
        if x in ans_tools['unigrams']:
            if not x in final_tools:
                final_tools.append(x)
    for x in arr_bi:
        if x in ans_tools['bigrams']:
            if not x in final_tools:
                final_tools.append(x)
    for x in arr_tri:
        if x in ans_tools['trigrams']:
            if not x in final_tools:
                final_tools.append(x)
            
    return final_tools
