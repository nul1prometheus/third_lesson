# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей
x = 0
educational_grant, expenses = 10000, 12000
parental_money = expenses - educational_grant
while x <= 10:
    x = x + 1
    expenses = expenses * 1.03
    expenses = float('{:.2f}'.format(expenses))
    print(expenses)
    parental_money = parental_money + expenses - educational_grant

print('From parents to year', parental_money)
