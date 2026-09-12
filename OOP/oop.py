class Employee:
    def __init__(self, name="", dpt="", scale=0):
        self.name = name
        self.dpt = dpt
        self.scale = scale

    def set_name(self, name):
        self.name = name

    def set_dpt(self, dpt):
        self.dpt = dpt

    def set_scale(self, scale):
        self.scale = scale

    def get_name(self):
        return self.name

    def get_dpt(self):
        return self.dpt

    def get_scale(self):
        return self.scale

    def take_home_income(self):
        raise NotImplementedError("Base employee does not have a take-home income calculation.")


class Officer(Employee):
    def __init__(self, name, dpt, scale, monthly_salary):
        super().__init__(name, dpt, scale)
        self.monthly_salary = monthly_salary

    def set_monthly_salary(self, ms):
        self.monthly_salary = ms

    def get_monthly_salary(self):
        return self.monthly_salary

    def take_home_income(self):
        return int(self.monthly_salary * 0.90)  # 10% tax


class DailyWager(Employee):
    def __init__(self, name, dpt, scale, daily_wage, absent_count):
        super().__init__(name, dpt, scale)
        self.daily_wage = daily_wage
        self.absent_count = absent_count

    def set_daily_wage(self, dw):
        self.daily_wage = dw

    def get_daily_wage(self):
        return self.daily_wage

    def set_absent(self, ab):
        self.absent_count = ab

    def get_absent(self):
        return self.absent_count

    def salary(self):
        present_days = 30 - self.absent_count
        return self.daily_wage * present_days

    def take_home_income(self):
        return self.salary()


# Main section
employees = [
    Employee("Ali", "DS", 17),
    Officer("Ahmad", "SE", 18, 50000),
    DailyWager("Kamran", "AI", 5, 1000, 2),
    Officer("Akmal", "IT", 21, 100000),
    Employee("Arshad", "CS", 22)
]

for emp in employees:
    print(f"Employee Name: {emp.get_name()}")
    print(f"Department: {emp.get_dpt()}")
    print(f"Scale: {emp.get_scale()}")

    try:
        income = emp.take_home_income()
        print(f"Take-home income: {income}")
    except NotImplementedError as e:
        print(str(e))

    print("-----------------------------")

