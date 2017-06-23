# Create a class that contains information about employees of a company
# and define methods to get employee name, job title, and start date.

class Company():

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.employees = set()

    def get_name(self):
        return self.name

    def add_employee(self, employee):
        self.employees.add(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def list_employees(self):
        for each in self.employees:
            print("{} started working as a {} {} at {}".format(each.name, each.title, each.start_date, my_company.get_name()))


class Employee():

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date


    def get_name(self):
        return self.name

    def get_title(self):
        return self.title

    def get_start_date(self):
        return self.start_date

    def get_info(self):
        print("{}, a {} at {} started working {}".format(self.name, self.title, my_company.get_name(),  self.start_date))



my_company = Company('Big Money', 'Big Prizes', '1992')
james = Employee("James", "dev", "today")
joel = Employee("Joel", "real job", "july 24")


my_company.add_employee(james)
my_company.add_employee(joel)

my_company.list_employees()

for each in my_company.employees:
    each.get_info()

