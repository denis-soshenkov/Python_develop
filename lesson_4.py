import random
from datetime import datetime, time

names = ['Денис', 'Карл', 'Аристарх', 'Федосий', 'Эрнест', 'Аскольд', 'Антип', 'Порфирий', 'Борис', 'Владилен',
         'Гавриил', 'Олег', 'Владлен', 'Вадим', 'Пахом', 'Владислав', 'Богдан', 'Никита', 'Наум', 'Семен', 'Никанор',
         'Ярослав', 'Соломон', 'Яков']
N = 200


# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random)
def F(names, N):
    tmp = []
    for n in range(N):
        tmp.append(names[random.randint(0, len(names) - 1)])
    return tmp


# Напишите функцию вывода самого частого имени из списка на выходе функции F.
def top_name(names):
    tmp = []
    unique_names = set(names)
    for name in unique_names:
        tmp.append((name, names.count(name)))
    tmp.sort(key=lambda i: i[1], reverse=True)
    return tmp[0]


top_1 = top_name(F(names, N))
print(f'Имя "{top_1[0]}" повторяется {top_1[1]} раз(а)')


# Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F
def letter_top1(names):
    tmp_list = [x[0] for x in names]
    tmp_set= {tmp_list}
    tmp = []
    for letter in tmp_set:
        tmp.append((letter, tmp_list.count(letter)))
    tmp.sort(key=lambda i: i[1])
    return tmp[0]


letter_1 = letter_top1(F(names, N))
print(f'Самая редкая заглавная буква "{letter_1[0]}" встречается {letter_1[1]} раз(а)')


# В файле с логами найти дату самого позднего лога (по метке времени)
def max_date(file):
    f = open(file, 'r').readlines()
    events = []
    for line in f:
        events.append(line.replace('\n', '').split(sep=' - '))
    for event in events:
        DT = datetime.strptime(event[0], '%Y-%m-%d %H:%M:%S,%f')
        event.insert(1, DT.time())
        event[0] = DT.date()
    events.sort(key=lambda i: i[1], reverse=True)
    return events


last_event = max_date(r'E:\log')[0]
print(f'Самая поздняя по времени запись в логе зафиксирована {last_event[0].strftime("%d.%m.%Y")} '
      f'в {last_event[1].strftime("%H:%M:%S")} для модуля {last_event[3]} приложения {last_event[2]} '
      f'c текстом "{last_event[4]}"')
