def to_mediterranean(ingredients):
    cheeses = [line.strip() for line in open('cheeses.txt')]
    dressings = [line.strip() for line in open('dressings.txt')]
    red_meats = [line.strip() for line in open('red_meats.txt')]
    meats = [line.strip() for line in open('meats.txt')]
    breads = [line.strip() for line in open('breads.txt')]
    sauces = [line.strip() for line in open('sauces.txt')]
    dressings = [line.strip() for line in open('dressings.txt')]
    spices = [line.strip() for line in open('spices.txt')]
    veggies = ['onion','red pepper','tomato','peppers','green pepper','roasted vegetables']
    ans_veggies = unibigrams(veggies)
    ans_spices = unibigrams(spices)
    ans_sauces = unibigrams(sauces)
    ans_cheese = unibigrams(cheeses)
    ans_meats = unibigrams(meats)
    ans_rm = unibigrams(red_meats)
    ans_breads = unibigrams(breads)
    ans_dressings = unibigrams(dressings)
    med = ["lamb", "chicken", "falafel"]
    med_sauces = ["Tahini sauce","Tzatziki sauce","Chermoula","Harissa","Toum"]
    c_f = ['chicken','falafel']
    med_spices = ['za\'atar','rosemary','sage','basil']
                  
    new_dict = {}

    for key, value in ingredients.items():
        new_value = [value[0], value[1], value[2], value[3]]
        name = word_tokenize(key)
        #print(name)
        if len(name) == 1:
           # print(name)
            if name[0] in cheeses:
                new_key = key.replace(key, 'feta cheese')
                new_dict[new_key] = new_value
                
            elif key == "butter":
                new_key = key.replace(key, 'olive oil')
                new_dict[new_key] = new_value
                
            elif name[0] in dressings:
                new_key = key.replace(key, 'Greek dressing')
                new_dict[new_key] = new_value
                
            elif name[0] in veggies:
                new_key = key.replace(key, 'olives')
                new_dict[new_key] = new_value
               
            elif name[0] in meats:
                #if not name[0] in red_meats:
                #    new_key = key.replace(name[0], random.choice(c_f))
                #    new_dict[new_key] = new_value
                new_key = key.replace(key,'lamb')
                new_dict[new_key] = new_value
            elif name[0] in breads:
                
                new_key = key.replace(key,'pita')
                new_dict[new_key] = new_value
                
            elif name[0] in spices:
                
                new_key = key.replace(key,random.choice(med_spices))
                new_dict[new_key] = new_value
                
                
            elif name[0] in sauces:
                new_key = key.replace(name[0], random.choice(med_sauces))
                new_dict[new_key] = new_value
            else:
                new_dict[key] = value
        elif len(name) == 2:
            if name in ans_cheese['bigrams']:
                new_key = key.replace(key, 'feta cheese')
                new_dict[new_key] = new_value
                
            elif name in ans_dressings['bigrams']:
                new_key = key.replace(key, 'Greek dressing')
                new_dict[new_key] = new_value
                
            elif name in ans_veggies['bigrams']:
                new_key = key.replace(key, 'olives')
                new_dict[new_key] = new_value
            elif name in ans_meats['bigrams']:
                if not name in ans_rm['bigrams']:
                    new_key = key.replace(key, random.choice(c_f))
                    new_dict[new_key] = new_value
                elif name in ans_rm['bigrams']:
                    new_key = key.replace(key, 'lamb')
                    new_dict[new_key] = new_value
            elif name in ans_sauces['bigrams']:
                new_key = key.replace(key, random.choice(med_sauces))
                new_dict[new_key] = new_value
            else:
                new_dict[key] = value
        elif len(name) == 3:
            if name in ans_cheese['trigrams']:
                new_key = key.replace(key, 'feta cheese')
                new_dict[new_key] = new_value
            elif name in ans_dressings['trigrams']:
                new_key = key.replace(key, 'Greek dressing')
                new_dict[new_key] = new_value
            elif name in ans_meats['trigrams']:
                if not name in ans_rm['trigrams']:
                    new_key = key.replace(key, random.choice(c_f))
                    new_dict[new_key] = new_value
                elif name in ans_rm['trigrams']:
                    new_key = key.replace(key, 'lamb')
                    new_dict[new_key] = new_value
            elif name in ans_sauces['trigrams']:
                new_key = key.replace(key, random.choice(med_sauces))
                new_dict[new_key] = new_value
            else:
                new_dict[key] = value
        else:
            new_dict[key] = value
    return new_dict