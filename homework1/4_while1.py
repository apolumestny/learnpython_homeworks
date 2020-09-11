"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    """
    Замените pass на ваш код
    """
    menu = {'Что на обед?' : 'Борщ', 'Что на завтрак' : 'амлет' ,'Что на ужин' : 'ничего! Пора худеть' }
    answer = input('Как дела?\n')
    while answer != 'Хорошо':
        answer = input('Как дела?\n')
    qestion = input('Задай мне вопрос\n')
    while qestion != 'Пока':
        if qestion in menu:
            print(menu[qestion])
            qestion = input('Задай мне вопрос\n')
        if qestion not in menu:
            qestion = input('Что нибудь еще?\n')
        if qestion == 'Пока':
            break

    
if __name__ == "__main__":
    ask_user()
