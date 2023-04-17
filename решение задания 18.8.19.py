all_cost_ticket = 0  # заводим счетчик общей стоимости билетов
print("Сколько билетов вы хотите приобрести: ")
sum_ticket = int(input())

list_ticket = []  # создаем пустой список билетов по возрасту
print("Заполните графу возраст: ")
list_ticket = [int(input()) for i in range(sum_ticket)]
# каждое значение возраста вводим, записываем в список и прогоняем по количеству покупаемых билетов

for years in list_ticket:  # условия для стоимости билетов; прогоняем возраст по созданному списку
    if years < 18:
        all_cost_ticket += 0
    if 18 <= years < 25:
        all_cost_ticket += 990
    if years >= 25:
        all_cost_ticket += 1390
if sum_ticket > 3:  # условия скидки
    all_cost_ticket = float(all_cost_ticket*0.9)

print("Общая стоимость билетов =", all_cost_ticket, "руб.")
