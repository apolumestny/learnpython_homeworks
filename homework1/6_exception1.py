"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def ask_user():
    """
    Замените pass на ваш код
    """
    menu = {'Что на обед?': 'Борщ', 'Что на завтрак': 'амлет', 'Что на ужин': 'ничего! Пора худеть'}
    qestion = input('Задай мне вопрос\n')
    while qestion != 'Пока':
        try:
            if qestion in menu:
                print(menu[qestion])
                qestion = input('Задай мне вопрос\n')
            if qestion not in menu:
                qestion = input('Что нибудь еще?\n')
        except KeyboardInterrupt:
            print('Пока')
            break
if __name__ == "__main__":
    ask_user()
