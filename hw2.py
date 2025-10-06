from re import *

menu = {
    "coffee": 120,
    "tea": 80,
    "sandwich": 200,
    "cake": 150,
    "juice": 100,
    'crake': 1000
}

# Task 1
def showMenu(data, choice):
    if choice == '1':
        print(sorted(data.items(), key= lambda dish: dish[1]))
    elif choice=='2':
        print(sorted(data.items(), key= lambda dish: dish[0]))
    else: print('You havent chosen the way to sort menu. Try again')

# Task 2
def avgPriceInMenu():
    print(sum(menu[x] for x in menu)/len(menu))

# Task 3
def addNewDish():
    dish = input('Введи блюдо, которое хочешь добавить/заменить цену: ')
    price = int(input('Введите цену: '))
    menu.update({dish: price})

# Task 4
def delDish(data, dish):
    if dish in data.keys():
        data.pop(dish)
    else:
        print('Этого блюда итак нет в меню')

# Task 5
def showBP():
    inp = int(input('Покажи блюда дешевле чем: '))
    print(list(x[0] for x in menu.items() if x[1]<=inp))

# Task 7
def sortDrinks():
    drinks = ['coffee', 'tea', 'juice']
    drinks = sorted([x for x in menu.items() if x[0] in drinks], key= lambda y: y[1])

# Task 8
def orderBill(order, data):
    orderDict = {}
    for thing in order:
        if thing not in data: return False
        else: orderDict.update({thing: data[thing]})
    order = orderDict
    return order
# def makeOrder():
    


def showOrderBeatifully(order):
    summa = sum(x for x in order.values())
    orderBeautyList = []
    for dish in order.items():
        dish = f'{dish[0]} - {dish[1]} руб.'
        orderBeautyList.append(dish)
    print('Ваш заказ:')
    for index, dish in enumerate(orderBeautyList, start=1):
        print(index, dish)
    print('Итого: ', summa, 'руб.')
    if summa > 500: print("Поздравляем, у вас скидка 10%!")
    elif order == []: print('Вы ничего не выбрали')


while True:
    try:
        inp = input('''Введите номер действия которое хотите сделать:
1. Вывести меню отсортированное:
    1. По алфавиту
    2. По цене
2. Посчитать среднюю цену блюда в меню
3. Добавить новые блюда в меню
4. Удалить блюдо из меню
5. Показать все блюда ниже цены N
6. Сделать заказ 
''')
        if inp=='1': showMenu(menu, input('Выбрать вариант сортировки меню: '))
        elif inp == '2': avgPriceInMenu()
        elif inp == '3': addNewDish()
        elif inp == '4': delDish(menu, input('Введите блюдо, которое хотите удалить: '))
        elif inp == '5': showBP()
        elif inp == '6': 
            order = split(r'[., ]+', input('Введите заказ: '))
            order = orderBill(order, menu)
            showOrderBeatifully(order)
            break
        else: print('Вы ничего не выбрали')
    except: print('Попрробуйте еще раз')