bank = {
    0000: {
        'pin': 0000,
        'balance': 1500,
    },
    1111: {
        'pin': 1111,
        'balance': 20,
    },
    2222: {
        'pin': 2222,
        'balance': 50,
    }
}

print("Добро пожаловать в банк\n")

number = int(input("введите свой номер карты:\n"))
while (not bank.get(number)):
    print('нету такой карты. Попробуйте ещё раз')
    number = int(input("введите свой номер карты:\n"))

pin = int(input("введите свий PIN:\n"))
while bank[number]["pin"] != pin:
    print("неверный PIN. Попробуйте ещё раз")
    pin = int(input("введите свий PIN:\n"))

print("\nДобро пожаловать в админ панель" + "\n")

def user1():
    print("у пользователя " + str(bank[1111]['balance']) + "$")

def user2():
    print("у данного пользователя " + str(bank[2222]['balance']) + "$")


def shop():
    o = int(input("введите сумму для пополнения\n"))
    if (o < 20001) and (o > 0):
            bank[0000]['balance'] = bank[0000]['balance'] + int(o)
            print("Ваш счет пополнен на: " + str(o) + "$" + "\n")
    else:
        print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

def shop1():
    a = int(input("введите сумму для пполнения\n"))
    if (a < 20001) and (a > 0):          
            bank[1111]['balance'] = bank[1111]['balance'] + int(a)
            print("Ваш счет пополнен на: " + str(a) + "$" + "\n")
    else:
        print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

def shop3():
    a = int(input("введите сумму для пполнения\n"))
    if (a < 20001) and (a > 0):          
            bank[2222]['balance'] = bank[2222]['balance'] + int(a)
            print("Ваш счет пополнен на: " + str(a) + "$" + "\n")
    else:
        print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")


def takeoff():
    c = int(input("введите сумму для снятия:\n"))
    if (c < 20001) and (c > 0) and (bank[0000]['balance'] > 0):
            bank[0000]['balance'] = bank[0000]['balance'] - int(c)
            print("с вашего счета снято " + str(c) + "$")
    else:
        print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

def takeoff1():
    c = int(input("введите сумму для снятия:\n"))
    if (c < 20001) and (c > 0) and (bank[1111]['balance'] > 0):
            bank[1111]['balance'] = bank[1111]['balance'] - int(c)
            print("с вашего счета снято " + str(c) + "$")
    else:
        print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

def takeoff2():
    c = int(input("введите сумму для снятия:\n"))
    if (c < 20001) and (c > 0) and (bank[2222]['balance'] > 0):
            bank[2222]['balance'] = bank[2222]['balance'] - int(c)
            print("с вашего счета снято " + str(c) + "$")
    else:
        print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

def card():
     v = int(input("введите сумму для перевода:\n"))
     if (v < 20001) and (v > 0) and (bank[0000]['balance'] > 0):
            bank[0000]['balance'] = bank[0000]['balance'] - int(v)
            print("с вашего счета снято " + str(v) + "$")
            k = int(input("введите пользователя котрому хотите перевести:\n"))
            if k == 1111:
                 bank[1111]['balance'] = bank[1111]['balance'] + (v)
                 print("переведено " + str(v) + " пользователю " + "1111" + "\n")
            elif k == 2222:
                 bank[2222]['balance'] = bank[2222]['balance'] + (v)
                 print("переведено " + str(v) + "пользователю " + "2222" + "\n")
            elif k == 0000:
                 bank[0000]['balance'] = bank[0000]['balance'] + int(v)
                 print("деньги возврвщены на счет пользователю " + "0000 " + "\n")
            else:
                 print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

def card1():
     v = int(input("введите сумму для перевода:\n"))
     if (v < 20001) and (v > 0) and (bank[1111]['balance'] > 0):
            bank[1111]['balance'] = bank[1111]['balance'] - int(v)
            print("с вашего счета снято " + str(v) + "$")
            k = int(input("введите пользователя котрому хотите перевести:\n"))
            if k == 0000:
                 bank[0000]['balance'] = bank[0000]['balance'] + (v)
                 print("переведено " + str(v) + "пользователю " + "0000" + "\n")
            elif k == 1111:
                 bank[1111]['balance'] = bank[1111]['balance'] + int(v)
                 print("деньги возврвщены на счет пользователю " + "1111" + "\n")
            elif k == 2222:
                 bank[2222]['balance'] = bank[2222]['balance'] + (v)
            else:
                 print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

def card3():
     v = int(input("введите сумму для перевода:\n"))
     if (v < 20001) and (v > 0) and (bank[2222]['balance'] > 0):
            bank[2222]['balance'] = bank[2222]['balance'] - int(v)
            print("с вашего счета снято " + str(v) + "$")
            k = int(input("введите пользователя котрому хотите перевести:\n"))
            if k == 0000:
                 bank[0000]['balance'] = bank[0000]['balance'] + (v)
                 print("переведено " + str(v) + "пользователю " + "0000" + "\n")
            elif k == 1111:
                 bank[1111]['balance'] = bank[1111]['balance'] + (v)
            elif k == 2222:
                 bank[2222]['balance'] = bank[2222]['balance'] + int(v)
                 print("деньги возврвщены на счет пользователю " + "1111" + "\n")
            else:
                 print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")


if number == 0000:
    while True:
        print("1 - баланс пользователя")
        print("2 - пополнить баланс")
        print("3 - снять средства пользователя")
        print("4 - перевод средств между пользователями")
        print("5 - показатьвсех пользователей в системе и их баланс")

        c = ("выберите что хотите сделать:\n")
        enter = input(c)

        if enter == '1':
            o = int(input("введите счет:\n"))
            if o == 0000:
                print("у данного пользователя " + str(bank[number]['balance']) + "$")
            elif o == 1111:
                user1()
            elif o == 2222:
                user2()
            else:
                print("данного пользователя нету в бд")

        elif enter == '2':
            o = int(input("Выберите пользователя:\n"))
            if o == 0000:
                shop()
            elif o == 1111:
                shop1()
            elif o == 2222:
                shop3()
            else:
                print("Данного пользователя нету в бд")

        elif enter == '3':
            o = int(input("выберите пользователя:\n"))
            if o == 0000:
                takeoff()
            elif o == 1111:
                takeoff1()
            elif o == 2222:
                 takeoff2()
            else:
                 print("данного пользоваткля нету в бд")

        elif enter == '4':
             o = int(input("введите пользователя у которого хотите пееревести деньги\n"))
             if o == 0000:
                  card()
             elif o == 1111:
                  card1()
             elif o == 2222:
                  card3()   

        elif enter == '5':
             for x in int(bank[0000]['balance']):
                  print(x)         
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
        o = int(input("введите сумму для пополнения:\n"))
        if (o < 20001) and (o > 0):
            bank[number]['balance'] = bank[number]['balance'] + int(o)
            print("Ваш счет пополнен на: " + str(o) + "$" + "\n")
        else:
            print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")

    elif enter == '3':
        c = int(input("введите сумму для снятия:\n"))
        if (c < 20001) and (c > 0) and (bank[number]['balance'] > 0):
            bank[number]['balance'] = bank[number]['balance'] - int(c)
            print("с вашего счета снято " + str(c) + "$")
        else:
            print("сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n")
    
    elif enter == '4':
        break

    else:
        print("извините такого пункта нет в меню выберете другой\n")