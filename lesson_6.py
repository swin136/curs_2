"""
Skypro. Профессия "Python-разработчик" ПОТОК
Курс 2
*******************************
Урок  6. Локальный Python и фaйлы. Домашнее задание 
Родительский Дмитрий Вячеславович
"""
import random
import os

# Влючение-выключение отладочных сообщений (True/False)
DEBUG = bool(0)

# Файлы для работы программы
# для хранения списка слов для тестирования
WORDS_FILE = 'words.txt'
# для записи историй игр
HISTORY_FILE = 'history.txt'


TRUE_ANSWER = "Верно! Вы получаете 10 очков."
BONUS = 10

def get_list_for_user():
    """
    Функция получает список слов из файла
    обрезает сисмволы перевода строки
    возращает список слов для тестирования пользователя 
    в формате [<str>, <str>, ... <str>]
    """
    f = open(file=WORDS_FILE, mode="rt")
    try:
        return [str(item).replace("\n", "") for item in f.readlines()]
    finally: f.close()


def shuffle_word(src_word : str):
    """
    Функция перемешивает буквы в слове случайным порядком
    возврашает слово типа str
    В процессе отладки несколько раз перемешиваемое слово
    совпадало с исходным, поэтому добавил цикл while
    <void>
    """
    shuffle_word = src_word 
    while shuffle_word == src_word:
        lst = [letter for letter in src_word]
        random.shuffle(lst)
        shuffle_word = "".join(lst)
    return shuffle_word


def add_history_to_file(user_name : str, score : int):
    """
    Добавляем статистику в файл по текущей игре
     <void>
    """
    f = open(file=HISTORY_FILE, mode="at")
    try: f.write(f"{user_name} {score}\n")
    finally: f.close()


def read_user_history(user_name : str):
    """
    Получаем статистику игр пользователся
    по имени
    Фукция возвращает список вида 
    [<Всего игр> : int,  <Лучший результат> : int]
    """
    # Читаем файл с историей игр в набор строк
    f = open(file=HISTORY_FILE, mode="rt")
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
    Основная функция программы
    """
    # Очищаем консоль
    os.system('cls')
    # Считываем из файла список слов для тестирования
    # и перемешиваем его
    user_tasks = get_list_for_user()
    random.shuffle(user_tasks)
    if len(user_tasks) == 0:
        print("Что-то не так со списком заданий")
        print("Пока, пока ....")
        quit()
    print("[+] Начинаем тестирование ...")
    
    # Ввод имени пользователя (и сделаем первую букву имени заглавной)
    while True:
        user_name = input("Ведите имя пользователя (из одного слова): ").strip().capitalize()
        if user_name != "": break
    # Начинаем наш цикл
    total = 0
    for word in user_tasks:
        if DEBUG: print(f"Исходное слово >>>> {word} <<<<")
        
        # Выводим слово с перемешанными буквами и ждем ответа пользователя
        answer = input(f"Угадай слово {shuffle_word(word)}: ").lower().strip()
        # Пользователь угадал слово
        if answer == word:
            print(f"{TRUE_ANSWER}")
            total += BONUS
        # Пользователь не угадал слово ...
        else: print(f"Неверно! Верный ответ – {word}.")

    # Добавлляем статистику игры пользователя в файл с историей
    add_history_to_file(user_name=user_name, score=total)

    # Получаем статистику пользователя за предыдущие игры
    user_stat = read_user_history(user_name=user_name)

    # И выводим ее на печать
    print("*" * 20)
    print(f"Всего игр сыграно: {user_stat[0]}")
    print(f"Максимальный рекорд: {user_stat[1]}")

    # Прощаемся с юзерем
    input(f"{user_name}, cпасибо за игру!!!. Нажмите Enter для завершения ....")
    # И очищаем консоль
    os.system('cls')

    
# Каркас нашей программы
if __name__ == "__main__":
    main()

################




 

