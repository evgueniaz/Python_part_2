# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или
# из документации к языку.

with open("wikitext.txt", encoding="utf-8") as txt:
    TEXT = txt.read()
    words = TEXT.split()
    # print(words)

    dict_of_words = {}
    for word in words:
        word = word.lower().strip('"').strip("(").strip(")").strip("!").strip("«").strip("...»").strip(",").strip("»")
        if word not in dict_of_words:
            dict_of_words[word] = 1
        else:
            dict_of_words[word] += 1

    list_of_words = sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)
    short_list = list_of_words[0 : 9]
    sorted_short_dict = dict(short_list)
    print(f'The list of the most frequent words with their frequency is: \n{sorted_short_dict}')