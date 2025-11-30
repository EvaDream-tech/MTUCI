# my_list = [1,2,3,4,5,6,7,8,9,10]
# print(my_list[1], type(1))
# my_list [1] = 100
# import example
#for i in range (1, 11):
    #    print (i, type(i))


#i=10
#while i >=1:
#    print(i)
#    i -=1

#num =int(input("Введите число: "))
#if num % 2==0:
#    print("Число четное")
#else:
#    print("Число нечетное")

# a=5
# print(a, "относится к типу", type(a))
#
# a=2.0
# print(a, "относится к типу", type(a))
#
# a=1+2j
# print(a, "Комплексное число?", isinstance(1+2j,complex))
#
# a=[1, 2.2, 'python']
#
# s= "Это строка"
# print(s)
#
# s= '''Многострочная строка'''
# print(s)

# number=1
# number=1.1
# print(number)

# a={5,2,3,1,4}
# print("a =",a)
# print(type(a))

# t=(5, 'Программа', 1+3j)
# print("t[1] =", t[1])
# print("t[0:3] =", t[0:3])
# t[0]=10

# num=int(input("Введите число: "))
# if num > 0:
#     print("Число положительное")
# elif num < 0:
#     print("Число отрицательно")
# else:
#     print("Число равное нулю")

# a=([1,2,3,4,5], "Введите число: ")
# print(a)


# a=int(input("Введите число: "))
# if a > 5:
#     print("Неправильно число, нужно от 0 до 5")
# elif a <= 5:
#     while a <
#     print(a, 1,2,3,4,5)


# num=int(input("Введите число: "))
# for i in range(num + 1):
#     print(i)


# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a > b:
#     print("Большее число:", a)
# elif a < b:
#     print("Большее число:", b)
# else:
#     print("Числа равны")

# Напиши программу, которая запрашивает два числа и выводит их сумму

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print("Сумма двух чисел: ", a+b)

# Пользователь вводит число. Выведи "Чётное" или "Нечётное"

# a = int(input("Введите число: "))
# if a % 2==0:
#     print("Чётное")
# else:
#     print("Нечётное")

# Запроси год рождения и вычисли возраст пользователя

# a = int(input("Год рождения: "))
# b = 2025
# print("Вам", b-a, "лет")

# Запроси три числа и найди наибольшее

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите треть число: "))
# if a > b and a > c:
#     print("Наибольшее число: ", a)
# elif b > a and b > c:
#     print("Наибольшее число: ", b)
# else:
#     print("Наибольшее число: ", c)

# Пользователь вводит N. Выведи сумму всех чисел от 1 до N

# a = int(input("Введите любое число: "))
# total = 1
# for i in range(1, a + 1):
#     total = total * i
# print("Факториал числа от 1 до", a, "равна:", total)


# a = int(input("Введите любое число: "))
# for i in range(1, 11):
#     sum = a * i
#     print(a, "*", i, "=", sum)


# a = int(input("Введите любое число: "))
# for i in range(1, 11):  # исправил диапазон
#     sum = a * i
#     print(a, "*", i, "=", sum)  # исправил - вывод внутри цикла

# a = int(input("Введите любое число: "))
# while a >=1:
#     print(a)
#     a -=1


# 4. Домашнее задание
# Задача 1
# a = int(input("Введите любое число: "))
# for i in range(0, a+1):
#     print(i)

# Задача 2
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
# if a > b:
#     print("Большее число: ", a)
# elif a < b:
#     print("Большее число: ", b)
# else:
#     print("Оба числа одинаковые")

# def anton(name):
# #def - ключевое слово, "имя функции"(идентификатор функции соответствует правилами идентификаторов функции), в скобках (аргумент)
#     print(f"Привет, {name}!")
# anton ("Антон")

# Задание 1. Написать простые функции


# def greet(name, mgs):
#     print("Привет,", name + '. ' + mgs)
# greet("Маша", "Доброе утро!")

# a=str(input("Введите имя пользователя: "))
# def greet(name):
#     print("Привет,", name)
# greet(a)

# a=int(input("Введите число: "))
# def square(number):
#     if a % 2==0 and a!=0:
#         print("Квадрат числа равен: ", a**2)
#     elif a % 2==1:
#         print("Квадрат числа равен: ", a**2)
#     else:
#         print("Ноль возвести в квадрат нельзя")
# square(number)

# x=int(input("Введите первое число: "))
# y=int(input("Введите второе число: "))
# def max_of_two(x, y):
#     if x>y:
#         print("Большее число: ", x)
#     elif x<y:
#         print("Большее число: ", y)
#     else:
#         print("Оба числа равны")
# max_of_two(x, y)

# name=str(input("Введите имя: "))
# def describe_person(name, age=30):
#     print("Вас зовут", name, "и Ваш возраст", age)
# describe_person(name)


# number=int(input("Введите число: "))
# def is_prime(number):
#     if number % 2==0:
#         print("False")
#     else:
#         print("True")
# is_prime(number)

# Чтение всего файла

# with open('example.txt', 'r') as file:
#     content = file.read()
# print(content)

# with open('example.txt', 'r') as file:
#     for line in file:
#         content = file.read()
# print(content)

# with open('user_input.txt', 'w') as file:
#     text = input("Введите текст: ")
#     file.write(text)
# print("Текущий текст сохранён в файле user_input.txt:", text)
# with open('user_input.txt', 'a') as file:
#     text = input("Введите текст: ")
#     file.write(text)
# print("Текущий текст сохранён в файле user_input.txt:", text)


# def error():
#     text = input("Введите название документа: ")
#     ok_files=('example.txt')
#     if text in ok_files:
#         try:
#            with open('example.txt', 'r') as file:
#                 context = file.read()
#                 print(context)
#         except FileNotFoundError:
#                 print("Неправильно введено названия файла")
#     else:
#         print("Неправильно введено названия файла")
# error()


# import example
# print(example.add(4, 5.5))

# def eva():
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     c = a + b
#     print("Сумма равна: ", c)
# eva()

# import example
# print(example.сложить(100, 100))

# def какая_то_функция():
#     a=input("Введите первое число: ")
#     b=input("Введите второе число: ")
#     if a>b:
#         import example
#         print(example.сложить(400, 100))
#         from datetime import datetime
#         print("Текущее время", datetime.now())
#
#     else:
#         print("Не угадал")
# какая_то_функция()

# from math import sqrt
# print("Квадратный корень: ", sqrt(16))


# import my_module
# print(my_module.сложить(1, 1))


# from example.qwerty import t
# name, number = t()
# print(name, number)
# t()

# 1. Запрашивает у пользователя ввод числа и выводит на экран все числа от 1 до введенного числа включительно.
#   a=int(input("Введите число: "))
#   for i in range(1, a + 1):
#     print(i)

# 2. Запрашивает у пользователя ввод 2 чисел и выводит на экран большее из них.
#     a=int(input("Введите первое число: "))
#     b=int(input("Введите второе число: "))
#     if a>b:
#         print("Большее число: ",a)
#     elif a<b:
#         print("Большее число: ",b)
#     else:
#         print("Оба числа равны")

    # 3. Напишите функцию greet, которая принимает имя пользователя в качестве аргумента и выводит приветствие с этим именем.
    # def greet():
    #     name=input("Введите имя пользователя: ")
    #     print("Здравствуйте,",name)
    # greet()

# 4. Создайте функцию square, которая возвращает квадрат переданного ей числа.
# a=int(input("Введите число: "))
# def square():
#     if a % 2==0 and a!=0:
#         print("Квадрат числа равен: ", a**2)
#     elif a % 2==1:
#         print("Квадрат числа равен: ", a**2)
#     else:
#         print("Ноль возвести в квадрат нельзя")
# square()

# 5. Реализуйте функцию max_of_two, которая принимает два числа в качестве аргументов и возвращает большее из них.
# x=int(input("Введите первое число: "))
# y=int(input("Введите второе число: "))
# def max_of_two(x, y):
#     if x>y:
#         print("Большее число: ", x)
#     elif x<y:
#         print("Большее число: ", y)
#     else:
#         print("Оба числа равны")
# max_of_two(x, y)

# 6. Напишите функцию describe_person, принимающую имя и возраст человека, и печатающую эту информацию в читаемом виде. Сделайте возраст опциональным аргументом со значением по умолчанию 30.
# name=str(input("Введите имя: "))
# def describe_person(name, age=30):
#     print("Вас зовут", name, "и Ваш возраст", age)
# describe_person(name)


# 7. Напишите функцию is_prime, которая определяет, является ли число простым, и возвращает True или False соответственно.
# number=int(input("Введите число: "))
# def is_prime(number):
#     if number % 2==0:
#         print("False")
#     else:
#         print("True")
# is_prime(number)

# 10. Используйте разные методы чтения файла: чтение всего файла сразу, построчное чтение, реализуйте выбор типа чтения в принимаемых аргументах функции.
# def read_or_read():
#     a=str(input("Вы хотите прочитать файл полностью? (да/нет): "))
#     if a == "да":
#         with open('example.txt', 'r') as file:
#             content = file.read()
#         print(content)
#     elif a == "нет":
#         a = str(input("Вы хотите прочитать построчно? (да/нет): "))
#         with open('example.txt', 'r') as file:
#             for line in file:
#                 content = file.read()
#         print(content)
#         ответ=str(input("Вывести следующую строку? (да/нет): "))
#         if ответ == "нет":
#             print("Чтение прекращено.")
#
#         else:
#             print("Файл полностью прочитан.")
# read_or_read()

# 10. Используйте разные методы чтения файла: чтение всего файла сразу, построчное чтение, реализуйте выбор типа чтения в принимаемых аргументах функции.
# def read_or_read():
#     a = input("Вы хотите прочитать файл полностью? (да/нет): ").lower()
#     if a == "да":
#         with open('example.txt', 'r') as file:
#             content = file.read()
#         print(content)
#     elif a == "нет":
#         a = input("Вы хотите прочитать построчно? (да/нет): ").lower()
#         if a == "да":
#             with open('example.txt', 'r') as file:
#                 for line in file:
#                     print(line.strip())
#                     ответ = input("Вывести следующую строку? (да/нет): ").lower()
#             if ответ == "нет":
#                 print("Чтение прекращено.")
#             else:
#                 print("Файл полностью прочитан.")
# read_or_read()






# with open('example.txt', 'r') as file:
#      for line in file:
#          content = file.read()
#  print(content)

# 11. Напишите программу, которая запрашивает у пользователя текст и записывает его в новый файл user_input.txt.
# with open('user_input.txt', 'w') as file:
#     text = input("Введите текст: ")
#     file.write(text)
# print("Текущий текст сохранён в файле user_input.txt:", text)
# with open('user_input.txt', 'a') as file:
#     text = input("Введите текст: ")
#     file.write(text)
# print("Текущий текст сохранён в файле user_input.txt:", text)

# with open('user_input.txt', 'a') as file:
#     text = input("Введите текст: ")
#     file.write(text)
# print("Текущий текст сохранён в файле user_input.txt:", text)

# 11. Напишите программу, которая запрашивает у пользователя текст и записывает его в новый файл user_input.txt.
# with open('user_input.txt', 'w') as file:
#     text = input("Введите текст: ")
#     file.write(text)
# print("Текущий текст сохранён в файле user_input.txt:", text)

# 12. Реализуйте функционал добавления текста в существующий файл, не удаляя его предыдущее содержимое.
# with open('user_input.txt', 'a') as file:
#     text = input("Введите текст: ")
#     file.write(text)
# print("Текущий текст сохранён в файле user_input.txt:", text)

# 13. Модифицируйте программу из Задания 1 так, чтобы она корректно обрабатывала исключение, возникающее при попытке открыть несуществующий файл. Вместо вывода ошибки программа должна выводить пользователю понятное сообщение.
# Используйте в блоке try except следующий класс исключений: FileNotFoundError.
# def error():
#     text = input("Введите название документа: ")
#     ok_files=('example.txt')
#     if text in ok_files:
#         try:
#            with open('example.txt', 'r') as file:
#                 context = file.read()
#                 print(context)
#         except FileNotFoundError:
#                 print("Неправильно введено названия файла")
#     else:
#         print("Неправильно введено названия файла")
# error()

# 14. Импортируйте модуль math и используйте функцию sqrt() для вычисления квадратного корня.
# from math import sqrt
# print("Квадратный корень: ", sqrt(16))

# 15. Используйте модуль datetime для отображения текущей даты и времени.
# from datetime import datetime
# print("Текущее время", datetime.now())

# 17. Импортируйте my_module в другой файл Python и вызовите функцию, определённую в модуле.
# import my_module
# print(my_module.сложить(1, 1))
#
# def имя_фамилия():
#     a=str(input("Введите имя: "))
#     b=str(input("Введите Фамилию: "))
#     print("Здравствуйте,",a,b)
#     return a, b
# имя_фамилия()

# with open('example.txt', 'r') as file:
#     # for line in file:
#     #     print(line)
#     content=file.read(

# 19 Продемонстрируйте, как импортировать различные модули из вашего пакета в другой файл Python. 19 Продемонстрируйте, как импортировать различные модули из вашего пакета в другой файл Python.
# from example import Имя_фамилия
# from example import Сложение
# from example import Приветствие

# import example.Имя_фамилия
# example.Имя_фамилия.имя_фамилия()
# import example.Сложение
# example.Сложение.сложить()
# import example.Приветствие
# example.Приветствие.приветствие()


# Задание 1: Базовый класс и методы
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def get_info(self):
#         return "Название книги:",self.title, "Автор:",self.author, "Год издания:",self.year
# Azbuka = Book("Вишневый сад", "А.П.Чехов", 1903)
# print(Azbuka.get_info())

# Задание 2: Работа с конструктором
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def get_radius(self):
#         return self.radius
#     def set_radius(self, new_radius):
#         self.radius = new_radius
# circle = Circle(10)
# print("Начальный радиус:", circle.get_radius())
# circle.set_radius(5)
# print("Новый радиус:", circle.get_radius())

# Задание 1: Защита данных пользователя
# class UserAccount:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.__password = password
#     def set_password(self, new_password):
#         if len(new_password) >= 8:
#             self.__password = new_password
#             print("Пароль успешно изменен")
#         else:
#             print("Ошибка: пароль слишком короткий")
#     def check_password(self, password):
#             return password == self.__password
# user = UserAccount("Anton", "Anton@yandex.ru", "qwerty123")
# print(user.check_password("12345"))
# print(user.check_password("qwerty123"))
#
# user.set_password("new_password")
# print(user.check_password("new_password"))

# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#     def get_info(self):
#         return "Марка машины: {}, Модель машины, {}".format(self.make, self.model)
# class Car(Vehicle):
#     def __init__(self, make, model, fuel_type):
#         super().__init__(make, model)
#         self.fuel_type = fuel_type
#     def get_info(self):
#         return "Марка машины: {}, Модель машины, {}, Тип топлива {}".format(self.make, self.model, self.fuel_type)
# vehicle = Vehicle("Land_Rover","Discovery")
# car = Car("Mercedes_benz", "E500", 95)
#
# print(vehicle.get_info())
# print(car.get_info())




