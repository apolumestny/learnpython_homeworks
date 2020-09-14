"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def compareStr(str1,str2):
        if isinstance(str1,str) and isinstance(str2,str):
            if str1 == str2:
                return 1
            elif len(str1) > len(str2):
                return 2
            elif str2 == 'learn':
                return 3

        return 0

    print(compareStr(3,4))
    print(compareStr('aaa',4))
    print(compareStr(3,'bbbb'))
    print(compareStr('aaaa','aaaa'))
    print(compareStr('1111','111112222'))
    print(compareStr('111111','11111'))
    print(compareStr('learn','11111222'))
    print(compareStr('learn','learn'))
    print(compareStr('1','learn'))




if __name__ == "__main__":
    main()
