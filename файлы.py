# file = open('file_1.txt')
# print(file.read())




# IO - In Out
# f = open(file='file_1.txt', mode='r')
# print(type(f)) #<class '_io.TextIOWrapper'>

f = open(file='file_1.txt', mode='r', encoding='UTF-8')
print(f.read()) #-> считывает весь файл целиком и возвращает строку
print(f.readline()) #-> считывает строку и возвращает строку
print(f.readlines()) #-> считывает все строки и возвращает список
for string in f:
    print(string, end='')

# mode='r' - Открывает файл для чтения
# Ставит каретку в начале файла
# Чтение возможно, запись невозможна
# Если файл не найден, вызывает ошибку

# mode='w' - Открывает файл для записи
# Ставит каретку в начале файла
# Если в файле записаны данные, он их все стирает
# Чтение невозможно, запись возможна
# Если файл не найден, создаёт его

# mode='a' - Открывает файл для записи
# Ставит каретку в конец файла
# Чтение невозможно, дозапись возможна
# Если файл не найден, создаёт его

# f = open(file='file_1.txt', mode='a', encoding='UTF-8')
# print(f.readable())
# print(f.writable())

# import sys
# sys.stdout - поток для вывода данных в консоль
# sys.stdin - поток для считывания данных из консоли
# sys.stderr - поток для вывода ошибок

with open(file='file_1.txt', mode='w+', encoding='UTF-8') as f:
    f.write('Hello World\nПривет Мир')
    f.write('Hello World\nПривет Мир')
    print(f.read())

# Открытие файла в двоичном режиме и запись текста
with open(file='1.txt', mode='wb') as f:
    print(f.write(bytes('Hello', encoding='UTF-8')))

with open(file='file_1.txt', mode='r', encoding='UTF-8') as f:
    count = 0
    for i in f:
        count += len(i) - 1
    count += 1
    print(count)


with open(file='file_1.txt', mode='r') as f:
    words = f.read().split()
    print(words)
    with open(file='output.txt', mode='w') as out:
        out.write(str([s for s in words if len(s) >= 6]))


with open(file='file_1.txt', mode='r') as f:
    words = f.read()
    with open(file='output.txt', mode='w') as out:
        out.write(words)


with open(file='file_1.txt', mode='r') as f:
    words = f.readline()
    with open(file='output.txt', mode='w') as out:
        while words != '':
            out.write(words)
            words = f.readline()


with open(file='file_1.txt', mode='r') as f:
    strings = f.readlines()
    strings[-1] += '\n'
    strings[0] = strings[0][:-1]

    with open(file='output.txt', mode='w') as out:
        for string in strings[::-1]:
            out.write(string)

a = input('Введите символ: ')
count = 0
with open(file='file_1.txt', mode='r') as f:
    for i in f.read().split():
        if a == i[0]:
            count += 1
print(count)

