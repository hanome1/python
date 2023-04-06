"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
items_strings = ['разработка', 'администрирование', 'protocol', 'standard']
items_bytes = []
for el in items_strings:
    el = str.encode(el, encoding='utf-8')
    print (el, type(el))
    items_bytes.append(el)
print()
for el in items_bytes:
    el = bytes.decode(el, encoding='utf-8')
    print (el, type(el))
#print(items_bytes) не понимаю, почему в списке данные по прежнему формата bytes, когда я в цикле их перезаписываю