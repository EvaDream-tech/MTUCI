# Задание 1: Защита данных пользователя
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        if len(new_password) >= 8:
            self.__password = new_password
            print("Пароль успешно изменен")
        else:
            print("Ошибка: пароль слишком короткий")
    def check_password(self, password):
            return password == self.__password
user = UserAccount("Anton", "Anton@yandex.ru", "qwerty123")
print(user.check_password("12345"))
print(user.check_password("qwerty123"))

user.set_password("new_password")
print(user.check_password("new_password"))

# Задание 2: Полиморфизм и наследование
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