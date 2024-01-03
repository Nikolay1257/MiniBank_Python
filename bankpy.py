bank = {
    0000: {
        'pin': 0000,
        'balance': 1500
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


def user(USER):
    if bank.get(USER):
        print("у данного пользователя " + str(bank[USER]['balance']) + "$")
    else:
        print("Данного пользователя нету в бд")


def shop(USER):
    if bank.get(USER):
        summa = int(input("введите сумму для пополнения\n"))
        if summa < 20001 and summa > 0:
            bank[USER]['balance'] += summa
            print("Ваш счет пополнен на: " + str(summa) + "$" + "\n")
        else:
            print(
                "сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n"
            )
    else:
        print("Данного пользователя нету в бд")


def takeoff(USER):
    if bank.get(USER):
        summa = int(input("введите сумму для снятия:\n"))
        if summa <= bank[USER]['balance'] and summa > 0 and bank[USER][
                'balance'] > 0:
            bank[USER]['balance'] = bank[USER]['balance'] - summa
            print("с вашего счета снято " + str(summa) + "$")
        else:
            print("на счету не достаточно средств для снятия\n")
    else:
        print("данного пользоваткля нету в бд")


def card(USER):
    if bank.get(USER):
        summa = int(input("введите сумму для перевода:\n"))
        if (summa < 20001) and (summa > 0) and bank[USER]['balance'] > 0:
            print("с вашего счета будет снято " + str(summa) + "$")
            recipient = int(
                input("введите пользователя котрому хотите перевести:\n"))
            if bank.get(recipient) and recipient != USER:
                bank[USER]['balance'] -= summa
                bank[recipient]['balance'] += summa
                print("переведено " + str(summa) + " пользователю " +
                      str(recipient) + "\n")
            elif recipient == USER:
                print("нельзя перевести деньги себе")
            else:
                print(
                    "сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n"
                )
    else:
        print("данного пользоваткля нету в бд")


if number == 0000:
    while True:
        print("1 - баланс пользователя")
        print("2 - пополнить баланс")
        print("3 - снять средства пользователя")
        print("4 - перевод средств между пользователями")
        print("5 - показатьвсех пользователей в системе и их баланс")
        print("6 - завершить работу")

        c = "выберите что хотите сделать:\n"
        enter = input(c)

        if enter == '1':
            o = int(input("введите счет:\n"))
            user(o)

        elif enter == '2':
            o = int(input("Выберите пользователя:\n"))
            result = shop(o)

        elif enter == '3':
            o = int(input("выберите пользователя:\n"))
            takeoff(o)

        elif enter == '4':
            o = int(
                input(
                    "введите пользователя у которого хотите пееревести деньги\n"
                ))
            card(o)

        elif enter == '5':
            for key in list(bank.keys()):
                print(
                    str(key) + " - у пользователя " +
                    str(bank[key]['balance']) + '$')

        elif enter == '6':
            break
        else:
            print("извините такого пункта нету в меню")

else:
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
            summa = int(input("введите сумму для пополнения:\n"))
            if (summa < 20001) and (summa > 0):
                bank[number]['balance'] += summa
                print("Ваш счет пополнен на: " + str(summa) + "$" + "\n")
            else:
                print(
                    "сумма превышает минимально допустимую 20000$\nПросьба обратиться в банк\n"
                )

        elif enter == '3':
            summa = int(input("введите сумму для снятия:\n"))
            if (summa <= (bank[number]['balance'])) and (summa > 0) and (
                    bank[number]['balance'] > 0):
                bank[number]['balance'] -= summa
                print("с вашего счета снято " + str(summa) + "$")
            else:
                print("недостаточно средств\n")

        elif enter == '4':
            break

        else:
            print("извините такого пункта нет в меню выберете другой\n")
