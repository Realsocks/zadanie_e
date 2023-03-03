import os # импорт библиотеки для работы с файлами


def Sorting(path): # функци сортировки
    list_files = [] # создание списка
    with os.scandir(path) as files:
        for i in files:
            list_files.append(i.name) # добавление файлов в список
    print('Выберите вид сортировки:')
    print('1. В алфавитном порядке;')
    print('2. В обратном алфавитном порядке.')
    a = int(input()) # ввод ответа
    if (a == 1): # если ответ - 1
        for file in sorted(list_files, reverse=False): # сортировка в алфавитном, reverse=False - не разворачивает список
            print(file)
    elif (a == 2):
        for file in sorted(list_files, reverse=True): # сортировка в обратном алфавитном, reverse=True - разворачивает список
            print(file)
    else:
        print('Неверный ввод.')


def CreateFile(path): # функция создания файла
    print('Введите название файла, который нужно создать:')
    file_name = input() # ввод названия
    new_path = path + "/" + file_name # склеивание старого пути и нового, для дальнейшей работы
    if (os.path.exists(new_path)):
        print('Данный файл уже существует')
    else:
        open(file_name, "w") # создание файла open(file_name, "w") - "w" перезапись или создание файла (если его не существует)
        print('Файл создан')

def CheckUnique(path):
    list_files = []
    with os.scandir(path) as files:
        for i in files:
            i = path + "/" + i.name # склеивание
            list_files.append(i) # добавление файлов в список
    files_hash = {}  # создание словаря
    for j in list_files:
        opened_file = open(j, 'r')  # открытие файла
        hash_cod = hash(opened_file.read())  # формирование хэш-кода текущего файла
        if hash_cod in files_hash.values():  # если совпадают
            print("Файл : " + j + " удалён.")
            opened_file.close()
            os.remove(j)  # удаление файла
        elif hash_cod not in files_hash.values():  # если не совпадают
            files_hash[j] = hash_cod # добавление хэш-кода файла в словарь

def WriteFile(path):
    print('Введите название файла:')
    file_name = input() # ввод
    new_path = path + "/" + file_name # склеивание
    print('Введите, что нужно записать:')
    text = input() # ввод текста
    with open(new_path, "a") as file: # запись в файл open(new_path, "a") - "a" пишет в конце файла, в отличие от "w"
        file.write("\n" + text)

def CheckFile(path): # чтение файла
    print('Введите название файла:')
    file_name = input() # ввод
    new_path = path + "/" + file_name # склеивание
    if (os.path.exists(new_path)): # если путь существует
        with open(new_path, "r") as file:
            line = file.readline() # чтение файла и запись в переменную line
            while line: # цикл
                print(line, end="") # вывод строки
                line = file.readline() # переход на следующую строку и её запись в переменную line
            print()
    else:
        print('Файла не существует')


def DeleteFile(path):
    print('Введите название файла:')
    file_name = input()
    new_path = path + "/" + file_name # склеивание
    if (os.path.exists(new_path)): # если файл существует
        os.remove(new_path) # удаление по пути
        print('Файл удален')
    else:
        print('Файл не существует')


print('Введите путь:')
path = input()
if (os.path.exists(path)):
        print("\nФайлы в папке:")
        with os.scandir(path) as files:
            for i in files:
                print(i.name) # вывод файлов
            print()
        print('Выберите желаемую опцию: ')
        print('1. Проверка на уникальность;')
        print('2. Сортировка файлов;')
        print('3. Добавить новый файл;')
        print('4. Дополнить текст в файле;')
        print('5. Просмотр содержимого файла;')
        print('6. Удалить файл;')
        a = int(input())
        if (a == 1):
            CheckUnique(path) # вызов функции проверки на уникальность
        elif (a == 2):
            Sorting(path) # вызов сортировки
        elif (a == 3):
            CreateFile(path) # вызов создания файла
        elif (a == 4):
            WriteFile(path) # вызов записи в файл
        elif (a == 5):
            CheckFile(path) # вызов просмотра содержимого
        elif (a == 6):
            DeleteFile(path) # вызов удаления файла
else:
    print('Путь не найден.')