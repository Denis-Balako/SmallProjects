"""Бейглз, (с) Денис Балако denisarius2000s@gmail.com
Дедуктивная логическая игра на угадывание числа по подсказкам.

Теги: короткая, игра, головоломка
"""

import random

NUM_DIIGITS = 3 # (!) Попробуй задать эту константу равной 1 ли 10
MAX_GUESSES = 10 # (!) Попробуй задать эту константу равной 1 ли 100

def main():
    print('''Бейглз, дедуктивная логическая игра.
by Denis Balako denisarius2000s@gmail.com

Я придумал {} значное число, без повторяющихся чисел.
Попробуй его угадать! Вот несколько подсказок:
Когда я говорю:    Это означает:
    Pico           Одно число правильное, но находится не в том месте
    Fermi          Одно число правильное и находится в том месте
    Bagels         Никакое из чисел не подходит

К примеру, если секретное число 248 и твой ответ 843, то ответ будет Fermi Pico.'''.format(NUM_DIIGITS))

    while True: # Основной цикл игры
        secretNum = getSecretNum() # Переменная, в которой хранится секретное число, которое должен угадать игрок
        print('Я придумал число.')
        print('У тебя есть {} попыток, чтобы его угадать.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Продолжаем итерации до получения правильной догадки
            while len(guess) != NUM_DIIGITS or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # Правильно выходим из цикла
            if numGuesses > MAX_GUESSES:
                print('Ты использовал все свои подсказки.')
                print('Ответ был {}'.format(secretNum))

        # Спрашиваем игрока, хочет ли сыграть ещё раз
        print('Хочешь сыграть ещё раз? (да/нет)')
        if not input('> ').lower().startswith('д'):
            break
    print('Спасибо за игру!')

def getSecretNum():
    """Возвращает строку из NUM_DIIGITS уникальных случайных цифр."""
    numbers = list('0123456789') # Создает список от 0 до 9
    random.shuffle(numbers)

    # Берем первые NUM_DIIGITS цифр из нашего списка
    secretNum = ''
    for i in range(NUM_DIIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Возвращает строку с подсказками pico, fermi и bagels
    для полученной на входе пары из догадки и секретного числа"""
    if guess == secretNum:
        return 'Ты угадал!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Правильная цифра на правильном месте
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # Правильная цифра в неправильном месте
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # Правильных цифр нет вообще
    else:
        # Сортируем подсказки в алфавитном порядке, чтобы их исходный порядок ничего не выдавал
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()
