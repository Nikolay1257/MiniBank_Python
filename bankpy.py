bank = {
    1111: {
        'pin': 1111,
        'balance': 0,
    },
    2222: {
        'pin': 2222,
        'balance': 0,
    }
}

print("Добро пожаловать в банк!\n")

number = int(input("введите свой номер карты:\n"))
while (not bank.get(number)):
    print('нету такой карты. Попробуйте ещё раз')
    number = int(input("введите свой номер карты:\n"))

pin = int(input("введите свий PIN:\n"))
while bank[number]["pin"] != pin:
    print("неверный PIN. Попробуйте ещё раз")
    pin = int(input("введите свий PIN:\n"))

while True:
    print("1 - мой счет")
    print("2 - пополнить счет")
    print("3 - снять со счета")
    print("4 - завершить работу")

    v = ("\nвыберите что хотите сделать:\n")
    enter = input(v)

    if enter == '1':
    
        print("на вашем счету " + str(bank[number]['balance']) + "$")
    
    elif enter == '2':
        o = int(input("введите сумму для пополнения: "))
        if (o < 20001) and (o > 0):
            bank[number]['balance'] = bank[number]['balance'] + int(o)
            print("Ваш счет пополнен на: " + str(o) + "$")
        else:
            print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк")

    elif enter == '3':
        c = int(input("введите сумму для снятия: "))
        if (c < 20001) and (c > 0) and (bank[number]['balance'] > 0):
            bank[number]['balance'] = bank[number]['balance'] - int(c)
            print("с вашего счета снято " + str(c) + "$")
        else:
            print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк")
    
    elif enter == '4':
        break

    else:
        print("извините такого пункта нет в меню выберете другой\n")