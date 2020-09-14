def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код

    """
    marks = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
             {'school_class': '4b', 'scores': [3, 4, 4, 5, 2, 5, 5, 3]},
             {'school_class': '4c', 'scores': [5, 5, 5, 5, 5]}]

    total_people = 0
    total_scores = 0

    for school_class in marks:
        each_class = 0
        for scores in school_class['scores']:
            each_class += scores
        total_scores += each_class
        total_people += len(school_class['scores'])
        print('{}: {}'.format(school_class['school_class'],each_class/len(school_class['scores'])))
    print(total_scores/total_people)

if __name__ == "__main__":
    main()
