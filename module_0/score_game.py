import numpy as np

from_number = 1  # от какого числа загадывать
to_number = 100  # до какого числа загадывать


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []

    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(from_number, to_number, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


def game_core(number):
    """Устанавливаем минимальную и максимальную границы для бинарного поиска, значения берем из граничных чисел. Затем
    запускаем цикл, в котором находим половину от текущего диапазона и сравниваем с загаданным числом. Если число
    меньше / больше, то смещаем левую либо правую границу на следующее / предыдущее число от текущего значения
    переменной mid. Условием окончания цикла является совпадение середины и загаданного числа. Функция принимает
    загаданное число, возвращает количество попыток, затраченных на поиск числа"""

    count = 1
    mid = 0
    low_predicted_number = from_number
    high_predicted_number = to_number

    while mid != number:
        count += 1
        mid = (low_predicted_number + high_predicted_number) // 2

        if mid < number:
            low_predicted_number = mid + 1
        elif mid > number:
            high_predicted_number = mid - 1

    return count  # выход из цикла, если угадали


score_game(game_core)


