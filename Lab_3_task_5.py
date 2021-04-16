"""
Создать класс Customer: id, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки, баланс.
Функции- члены реализуют запись и считывание полей (проверка корректности), зачисление и списание сумм на счет.
Создать список объектов. Вывести:
a)	список покупателей в алфавитном порядке;
b)	список покупателей, у которых номер кредитной карточки находится в заданном интервале
"""


class Customer:
    __id = 0
    __Surname = ""
    __Name = ""
    __MiddleName = ""
    __Address = ""
    __CreditCard = 0
    __Balance = 0

    def __init__(self, id0, surname, name, middlemame, address, creditcard, balance):
        self.__id = id0
        self.__Surname = surname
        self.__Name = name
        self.__MiddleName = middlemame
        self.__Address = address
        self.__CreditCard = creditcard
        self.__Balance = balance

    def getId(self):
        return self.__id

    def setId(self, id0):
        self.__id = id0

    def getSurname(self):
        return self.__Surname

    def setSurname(self, surname):
        self.__Surname = surname

    def getName(self):
        return self.__Name

    def setName(self, name):
        self.__Name = name

    def getMiddleName(self):
        return self.__MiddleName

    def setMiddleName(self, middlename):
        self.__MiddleName = middlename

    def getAddress(self):
        return self.__Address

    def setAddress(self, address):
        self.__Address = address

    def getCreditCard(self):
        return self.__CreditCard

    def setCreditCard(self, creditcard):
        self.__CreditCard = creditcard

    def getBalance(self):
        return self.__Balance

    def setBalance(self, balance):
        self.__Balance = balance

    def __str__(self):
        return "ID - " + str(self.__id) + " Фамилия: " + str(self.__Surname) + " Имя: " + str(
            self.__Name) + \
               " Отчество: " + str(self.__MiddleName) + " Адрес: " + str(self.__Address) + \
               " Номер карты: " + str(self.__CreditCard) + " Баланс: " + str(self.__Balance)

    def addBalance(self, balance):
        self.__Balance = self.getBalance() + balance

    def reduceBalance(self, balance):
        self.__Balance = self.getBalance() - balance

def sort():
    fio = []
    for i in range(len(BankClient)):
        fio.append(BankClient[i].getSurname()+" "+BankClient[i].getName()+" "+BankClient[i].getMiddleName())
    for i in range(len(fio)):
        for j in range(len(fio)-1-i):
            if fio[j] > fio[j+1]:
                fio[j], fio[j+1] = fio[j+1], fio[j]
    for i in range(len(fio)):
        print(fio[i])

def card(n, m):
    for i in range(len(BankClient)):
        if n <= BankClient[i].getCreditCard() and BankClient[i].getCreditCard() <= m:
            print(BankClient[i].getSurname()+" "+BankClient[i].getName()+" "+BankClient[i].getMiddleName()+" "
                  + str(BankClient[i].getCreditCard()))

# Заведение клиентов
BankClient = []
BankClient.append(Customer(1, "Гуревич", "Андрей", "Владимирович", "Гомель", 55441, 100))
BankClient.append(Customer(2, "Гуревич", "Павел", "Андреевич", "Минск", 45688, 200))
BankClient.append(Customer(3, "Василенко", "Валерий", "Петрович", "Москва", 45641, 500))
BankClient.append(Customer(4, "Абдурахман", "Ибн", "Хатаб", "Москва", 34561, 234))

# Функция сортировки по алфавиту (включая фамилия, имя, отчество)
sort()

# Увеличение баланса
BankClient[0].addBalance(45)
print(BankClient[0])

# Уменьшение баланса
BankClient[1].reduceBalance(25)
print(BankClient[1])

# Вывод карт из заданного диапазона
card(30000, 45000)
