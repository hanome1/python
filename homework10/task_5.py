"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
targets = [['ping', 'yandex.ru'],['ping', 'youtube.com']]
for item in targets:
    process = subprocess.Popen(item, stdout=subprocess.PIPE)
    for line in process.stdout:
        print(line)
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))