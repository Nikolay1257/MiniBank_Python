bank = {
    'balance': 0,
}

while True:
    print("1 - мой счет")
    print("2 - пополнить счет")
    print("3 - снять со счета")
    print("4 - завершить работу")

    v = ("\nвыберите что хотите сделать: ")
    enter = input(v)

    if enter == '1':
    
        print("на вашем счету " + str(bank['balance']) + "$")
    
    elif enter == '2':
        o = int(input("введите сумму для пополнения: "))
        if (o < 20001) and (o > 0):
            bank['balance'] = bank['balance'] + int(o)
            print("Ваш счет пополнен на: " + str(o) + "$")
        else:
            print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк")

    elif enter == '3':
        c = int(input("введите сумму для снятия: "))
        if (c < 20001) and (c > 0) and (bank['balance'] > 0):
            bank['balance'] = bank['balance'] - int(c)
            print("с вашего счета снято " + str(c) + "$")
        else:
            print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк")
    
    elif enter == '4':
        break

    else:
        print("извините такого пункта нет в меню выберете другой")