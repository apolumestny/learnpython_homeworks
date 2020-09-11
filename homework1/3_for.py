
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код

    """
    marks = [ {'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4b', 'scores': [3,4,4,5,2,5,5,3]},{'school_class': '4c', 'scores': [5,5,5,5,5]}]

    total_people = 0
    total_scores = 0
    each_class = {}
    for class_count in range(len(marks)):
        class_scores = 0
        for people_count in range(len(marks[class_count]['scores'])):
            total_scores += marks[class_count]['scores'][people_count]
            class_scores += marks[class_count]['scores'][people_count]
            each_class[marks[class_count]['school_class']] = class_scores/len(marks[class_count]['scores'])
        total_people += len(marks[class_count]['scores'])
    avg_school =total_scores/total_people
    print(avg_school)
    print(each_class)
if __name__ == "__main__":
    main()
