#Пользователь делает вклад в размере a рублей сроком на years лет под m% годовых (каждый год размер его вклада
# увеличивается на m%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
#Написать функцию count_money, принимающая аргументы initial_money_amount,
# percent и years, и возвращающую сумму, которая будет на счету пользователя к концу переиода

initial_money_amount = int(input())
percent = int(input())
years = int(input())
def count_money(initial_money_amount, percent, years):
    for i in range(years):
        initial_money_amount = initial_money_amount + initial_money_amount / 100 * percent
    return initial_money_amount
print(count_money(initial_money_amount, percent, years))