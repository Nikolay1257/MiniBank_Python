import sqlite3

con = sqlite3.connect("data.sqlite3")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS user_data(cart_number integer PRIMARY KEY, pin text, balance REAL)""")
cur.execute("INSERT INTO user_data(cart_number, pin, balance) VALUES(?, ?, ?)", (12345678, "0000", 10023))
cur.execute("INSERT INTO user_data(cart_number, pin, balance) VALUES(?, ?, ?)", (87654321, "9993", 0))

print("Добро пожаловать в банк\n")


def check_number(cart_number):
    cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (cart_number,))
    card_data = cur.fetchall()

    if len(card_data) == 0:
        return False

    return True


def check_pin(pin_string, cart_number):
    cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (cart_number,))
    card_data = cur.fetchall()[0]
    return card_data[1] == pin_string


number = input("Введите свой номер карты: ")

while not check_number(number):
    print("Неверный номер или такой карты нет. Попробуйте ещё раз\n")
    number = input("Введите свой номер карты: ")

pin = input("Введите свой PIN: ")

while not check_pin(pin, number):
    print("Неверный PIN. Попробуйте ещё раз")
    pin = input("Введите свой PIN: ")

print("\nДобро пожаловать в личный кабинет!\n")


def user(user_data: tuple):
    cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (user_data[0],))
    data_user = cur.fetchall()
    if len(data_user) != 0:
        print(f"\nУ данного пользователя {data_user[0][2]} $\n")
    else:
        print("\nДанного пользователя нету в бд\n")


def shop(user_data: tuple):
    cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (user_data[0],))
    data_user = cur.fetchall()
    if len(data_user) != 0:
        a = int(input("Введите сумму для пополнения: "))
        if (a < 20001) and (a > 0):
            cur.execute('UPDATE user_data SET balance = ? where cart_number = ?', (data_user[0][2] + a, user_data[0]) )
            print(f"\nВаш счет пополнен на: {a}$\n")
        else:
            print("\nСумма превышает минимально допустимую 20000$\nПожалуйста, обратитесь в поддержку\n")
    else:
        print("\nДанный пользователь не существует.\n")


def takeoff(user_data: tuple):
    cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (user_data[0],))
    data_user = cur.fetchall()
    if len(data_user) != 0:
        c = int(input("\nВведите сумму для снятия:\n"))
        if 0 < c <= data_user[0][2]:
            cur.execute('UPDATE user_data SET balance = ? where card_number = ?',
                        (data_user[0][2] - int(c), user_data[0]))
            print(f"\nС вашего счета снято {c} $\n")
        else:
            print("\nНа счету не достаточно средств для снятия\n")
    else:
        print("\nДанный пользователь не существует\n")


def card(user_data: tuple):
    cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (user_data[0], ))

    data_user = cur.fetchall()

    if len(data_user) != 0:

        k = input("\nВведите пользователя которому хотите перевести: ")

        if k == str(user_data[0]):
            print("\nВы не можете сами себе перевести.\n")
            return

        cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (k,))
        to_send_user = cur.fetchall()

        if len(to_send_user) == 0:
            print("\nДанный пользователь не существует.\n")
            return

        v = int(input("\nВведите сумму для перевода:\n"))

        if 0 < v < 20001 and v <= data_user[0][2]:
            cur.execute('UPDATE user_data SET balance = ? where cart_number = ?',
                        (data_user[0][2] - int(v), user_data[0]))
            cur.execute('UPDATE user_data SET balance = ? where cart_number = ?',
                        (to_send_user[0][2] + int(v), k))
            print(f"\nС вашего счета снято: {v} $ и отправленно: {k}")

    else:
        print("\nДанного пользователя нету в бд\n")


number = int(number)
user_data = (number, pin)

while True:
    print("1 - мой счет")
    print("2 - пополнить счет")
    print("3 - снять со счета")
    print("4 - перевести другому пользователю")
    print("5 - завершить работу")

    v = "\nВвыберите что хотите сделать: "
    enter = input(v)

    if enter == "1":
        cur.execute("SELECT * FROM user_data WHERE cart_number = (?)", (user_data[0], ))
        data_user = cur.fetchall()
        print(f"\nНа вашем счету  {data_user[0][2]} $")

    elif enter == "2":
        shop(user_data)

    elif enter == "3":
        takeoff(user_data)

    elif enter == "4":
        card(user_data)

    elif enter == "5":
        break

    else:
        print("Извините, но такого пункта нет в меню, выберете другой\n")
