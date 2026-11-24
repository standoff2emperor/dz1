def average_grade(a, b, c):
    res=(a + b + c) / 3
    return res
def grade_message(average):
    if average >=4.5:
        return "Отлично"
    elif average >=3.5:
        return "Хорошо"
    else:
        return "Нужно повторить материал"
srednee=average_grade(5, 4, 5)
srball1=grade_message(srednee)
print(round(srednee, 2), srball1)
srednee1=average_grade(3, 4, 3)
srball2=grade_message(srednee1)
print(round(srednee1, 2), srball2)
