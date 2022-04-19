from cupshelpers import parseDeviceID
import numpy as np
from pyrsistent import b

def predict(number:int=100) -> int:
    """Ассимптотически подбираемся к числу, начиная с середины

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    predict_number, predict_number_prv, tmp = 50, 0, 0
    
    while True:
        count += 1
        if number == predict_number:
            break
        
        elif predict_number == predict_number_prv == tmp:
        # Отрабатываем случаи 1, 98, 99 и 100 отдельно из-за округления
            if number < predict_number:
                predict_number = 1
            else:
                for i in range(1, 3):
                    predict_number += i
                    if number == predict_number:
                        break
                    
        elif number > predict_number:
            tmp = predict_number
            predict_number = (predict_number 
                            + abs(predict_number - predict_number_prv)//2)
            predict_number_prv = tmp
        elif number < predict_number:
            tmp = predict_number
            predict_number = (predict_number 
                            - abs(predict_number - predict_number_prv)//2)
            predict_number_prv = tmp
        
    print(f'Это число {predict_number}!')
    
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(predict)

print(f'Всего {predict()} попыток! Вы великолепны!')