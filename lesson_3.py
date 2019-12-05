import pymorphy2
morph = pymorphy2.MorphAnalyzer()

# Считать текст из файла
f = open(r'U:\text.txt').read()

# методами строк очистить от знаков препинания
znaki = ['.', ',', '?', '!', ':', ';', '—', '«', '»', '-']
for z in znaki:
    f = f.replace(z, '')

# сформировать List со словами
list_words = f.split()

# привести все слова к нижнему регистру
list_words_lower = list(map(lambda x: x.lower(), list_words))

# получить из list dict, ключами которого являются слова, а значения - их количество появлений в тексте
dict_words = {}
for word in list_words_lower:
    if word not in dict_words.keys():
        dict_words.update({word: 1})
    else:
        dict_words[word] += 1

# вывести 5 наиболее часто встречающихся слов, вывести количество разных слов в тексте
list_for_sort = list(dict_words.items())
list_for_sort.sort(key=lambda i: i[1], reverse=True)
print(list_for_sort[:5])

unique_words = set(list_words_lower)
print(unique_words)



# PRO
# дополнительно к приведению к нижнему регистру выполнить лемматизацию
list_words_lower_lemma = list(map(lambda x: morph.parse(x.lower())[0].normal_form, list_words))

# получить из list dict, ключами которого являются слова, а значения - их количество появлений в тексте
dict_words_lemma = {}
for word in list_words_lower_lemma:
    if word not in dict_words_lemma.keys():
        dict_words_lemma.update({word: 1})
    else:
        dict_words_lemma[word] += 1

# вывести 5 наиболее часто встречающихся слов, вывести количество разных слов в тексте
list_for_sort_lemma = list(dict_words_lemma.items())
list_for_sort_lemma.sort(key=lambda i: i[1], reverse=True)
print(list_for_sort_lemma[:5])

unique_words_lemma = set(list_words_lower_lemma)
print(unique_words_lemma)
