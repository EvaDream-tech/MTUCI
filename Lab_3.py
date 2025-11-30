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