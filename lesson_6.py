"""
Skypro. Профессия "Python-разработчик" ПОТОК
Курс 2
*******************************
Урок  6. Локальный Python и фaйлы. Домашнее задание 
Родительский Дмитрий Вячеславович
"""
from random import shuffle, sample
import os

# Влючение-выключение отладочных сообщений (True/False)
IS_DEBUG_MSG = bool(0)

# Файлы для работы программы
# для хранения списка слов для тестирования
WORDS_FILE = 'words.txt'
# для записи историй игр
HISTORY_FILE = 'history.txt'


TRUE_ANSWER_MSG = "Верно! Вы получаете 10 очков."
BONUS = 10

# количество вопросов для тестирования пользователя из общего списка слов
TASK_COUNT = 25

def get_list_for_user_from_file(fname : str):
    """
    Функция получает список слов из файла fname, 
    обрезает сисмволы перевода строки, получает список 
    случайных TASK_COUNT значений и возращает список 
    слов для тестирования пользователя, при этом порядок слов по отношению
    к исходному файлу перемешивается.
    Обязательно отсекается строки в исходной файле 
    (в противном случае программа виснет)!
    *********************************************
    return [<str>, <str>, ... <str>]
    *********************************************
    """
    f = open(file=fname, mode="rt")
    try:
        return sample([str(item).replace("\n", "") for item in f.readlines() if len(str(item).strip()) > 0], TASK_COUNT)
    finally: f.close()


def get_shuffle_word(src_word : str):
    """
    Функция перемешивает буквы в слове случайным порядком
    возврашает слово типа str
    В процессе отладки несколько раз перемешиваемое слово
    совпадало с исходным, поэтому добавлен цикл while
    *********************************************
    return <None>
    *********************************************
    """
    shuffle_word = src_word 
    while shuffle_word == src_word:
        lst = [letter for letter in src_word]
        shuffle(lst)
        shuffle_word = "".join(lst)
    return shuffle_word


def add_history_to_file(user_name : str, score : int, fname : str):
    """
    Добавляем статистику (имя пользователя, количество очков) 
    в файл fname по текущей игре
    *********************************************
    return <None>
    *********************************************
    """
    f = open(file=fname, mode="at")
    try: f.write(f"{user_name} {score}\n")
    finally: f.close()


def read_user_history_from_file(user_name : str, fname : str):
    """
    Получаем статистику игр конкретного пользователся 
    Фукция возвращает список вида 
    retyrn [<Всего игр> : int,  <Лучший результат> : int]
    """
    # Читаем файл с историей игр в набор строк
    f = open(file=fname, mode="rt")
    try:
        lst = [str(item).replace("\n", "") for item in f.readlines()]
    finally: f.close()
    # Парсим набор строк и ищем данные по пользователю user_name
    # CЧетчик
    # Игр и максимального количества очков
    max_score = total_play = 0
    
    for item in lst:
        # !!! Прием из вебинара !!!!!
        user, score = item.split(" ")
        # Прочитали данные по нашему пользователю - 
        # учитываем в статистике
        if user == user_name:
            total_play += 1
            if int(score) >= max_score: max_score = int(score)
    
    return [total_play, max_score]


def main():
    """
    Основная функция программы с реализацией бизнес-логики
    *********************************************
    return <None>
    *********************************************
    """
    # Очищаем консоль
    os.system('cls')
    # Считываем из файла список слов для тестирования
    # и перемешиваем его, если не можем загрузить
    # список слов сообщаем пользователю и завершаем программу
    user_tasks_list = get_list_for_user_from_file(fname=WORDS_FILE)
    # shufle_userword(user_tasks)
    if len(user_tasks_list) == 0:
        print("Что-то не так со списком заданий")
        print("Пока, пока ....")
        quit()
    print("[+] Начинаем тестирование ...")
    
    # Ввод имени пользователя (и сделаем первую букву имени заглавной)
    while True:
        user_name = input("Ведите имя пользователя (из одного слова): ").strip().capitalize()
        if user_name != "": break
    # Начинаем наш цикл
    # счетчик набранных баллов
    total = 0
    # счетчик слов
    i = 1
    for word in user_tasks_list:
        if IS_DEBUG_MSG: print(f"Исходное слово >>>> {word} <<<<")
        # Выводим слово с перемешанными буквами и ждем ответа пользователя
        answer = input(f"Угадай слово № {i} >>>> {get_shuffle_word(word)}: ").lower().strip()
        i += 1
        # Пользователь угадал слово, увеличиваем счетчик бонусов
        if answer == word:
            print(f"{TRUE_ANSWER_MSG}")
            total += BONUS
        # Пользователь не угадал слово ...
        else: print(f"Неверно! Верный ответ – {word}.")

    # Добавляем статистику игры пользователя в файл с историей
    add_history_to_file(user_name=user_name, score=total, fname=HISTORY_FILE)

    # Получаем статистику пользователя за предыдущие игры из файла с историей
    # в виде списка целочисленных чисел [количество игр, максимальный результат]
    user_stat_list = read_user_history_from_file(user_name=user_name, fname=HISTORY_FILE)

    # И выводим ее на печать
    print("*" * 20)
    print(f"Всего игр сыграно: {user_stat_list[0]}")
    print(f"Максимальный рекорд: {user_stat_list[1]}")

    # Прощаемся с пользователем
    input(f"{user_name}, cпасибо за игру!!!. Нажмите Enter для завершения ....")
    # И очищаем консоль
    os.system('cls')

    
# Основной каркас нашей программы
if __name__ == "__main__":
    main()


################




 

