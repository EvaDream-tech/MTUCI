class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return "Имя сотрудника: {}, Идентификационный номер: {}".format(self.name, self.id)
class Manager(Employee):
    def __init__(self, name, id, department):
        # super().__init__(name, id)
        Employee.__init__(self, name, id)
        self.department = department
    def get_info(self):
        return "Имя сотрудника: {}, Идентификационный номер: {}".format(self.name, self.id)
    def manage_project(self):
        return "Управляет проектами: {}".format(self.department)
class Technician(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization
    def get_info(self):
        return "Техник: {}, Идентификационный номер: {}".format(self.name, self.id)
    def perform_maintenance(self):
        return "Выполняет техническое обслуживание: {}".format(self.specialization)
class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team = []
    def get_info(self):
        return "Технический менеджер: {}, Идентификационный номер: {}".format(self.name, self.id)
    def tech_lead(self):
        return "Управляет проектами: {}, Выполняет техническое обслуживание: {}".format(self.department, self.specialization)
    def add_employee(self, employee):
        self.team.append(employee)
        return "Сотрудник {} добавлен в список подчиненных".format(employee.name)
    def get_team_employee(self):
        if not self.team:
            return "Нет подчиненных сотрудников"
        team_info = "Команда сотрудников:\n"
        for employee in self.team:
            team_info += "- " + employee.get_info() + "\n"
        return team_info

emp1 = Employee("Иван Иванов", "У1")
manager = Manager("Петр Петров", "У2", "IT")
tech = Technician("Сидоров", "У3", "Сети")
tech_manager = TechManager("Маша", "У4", "Разработка", "Python")

print(emp1.get_info())
print(manager.get_info())
print(manager.manage_project())
print(tech.get_info())
print(tech.perform_maintenance())
print(tech_manager.get_info())
print(tech_manager.tech_lead())

print(tech_manager.add_employee(emp1))
print(tech_manager.add_employee(tech))
print(tech_manager.get_team_employee())