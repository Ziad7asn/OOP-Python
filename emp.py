import csv


class Employee:
    company = "Codezilla"
    

    def __init__(self, name , age, job, id,phone, bank_account,hours_worked=160,hour_rate=15 ,from_file = False):
        self.name = name
        self.age= age
        self.job = job
        self.__hours_worked = hours_worked
        self.__hour_rate = hour_rate
        self.__id = id
        self.__phone = phone
        self.__bank_account = bank_account
        if not from_file:
            AllEmployee.add_employee(self)
        

    @property
    def hours_worked(self):
        return self.__hours_worked
    
    @hours_worked.setter
    def hours_rate(self,new_hours):
        if isinstance(new_hours,int) and new_hours > 0:
            self.__hours_worked = new_hours
        else:
            raise ValueError("Hours Worked Must be a positive number")
        
    
    def calculate_gross_salary(self):
        return(self.__hours_worked * self.__hour_rate)

    def calculate_gross_salary(self):
        gross_salary = self.calculate_gross_salary()
        return Finance.calculation_net_salary(gross_salary)

    @staticmethod
    def is_valid_phone(phone):
        return phone.startswith("+20") and len(phone)==12
    
    @staticmethod
    def calculate_tax(salary):
        if salary < 30000:
            return salary * 0.1
        else: 
            return salary * 0.3

    def __str__(self):
        return f"{self.name} is {self.age} years old, and works as {self.job}."

    def __dir__(self):
        return f"Employee name = {self.name}, age = {self.age}, job = {self.job}"

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def set_phone(self,new_phone):
        if Employee.is_valid_phone(new_phone):
            self.__phone = new_phone
        else:
            return "not valid number"


    def get_phone(self):
            return self.__phone 

    def get_bank_account(self,id):
        if self.__id == id:
            return self.__bank_account[-3:]
        else:
            return "you are not allowed to view the bank account"
        

    @property
    def id(self):
        return self.__id   

    @id.setter
    def id(self,value):
            self.__id = value

    def calculate_gross_salary(self):
        return self.__hour_rate * self.__hours_worked
    

    


    @classmethod
    def read_csv_data(cls,file_name):
        with open(file_name,'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row["name"]
                age = row["age"]
                job = row["job_title"]
                id = row["id"]
                phone = row["phone"]
                bank_account = row["bank_account"]
                hours_worked = int(row['hours_worked'])
                hour_rate = int(row['hour_rate'])
                cls(name,age,job,id,phone,bank_account,hours_worked,hour_rate)

    
class EmployeeFileHandler:
    @staticmethod
    def read_csv_data(file_name):
        employees = []
        with open(file_name,'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row["name"]
                age = row["age"]
                job = row["job_title"]
                id = row["id"]
                phone = row["phone"]
                bank_account = row["bank_account"]
                hours_worked = int(row['hours_worked'])
                hour_rate = int(row['hour_rate'])
                employee=Employee(name,age,job,id,phone,bank_account,hours_worked,hour_rate,from_file=True)
                employees.append(employee)
        return employees
    
    @staticmethod
    def read_and_add_to_AllEmployess(file_name):
        employees_list = EmployeeFileHandler.read_csv_data(file_name)
        for emp in employees_list:
            AllEmployee.add_employee(emp)

class AllEmployee:
    __employees= []

    @classmethod
    def add_employee(cls,employee):
        if employee not in AllEmployee.__employees:
            cls.__employees.append(employee)

    @classmethod
    def list_all_employees(cls):
        return cls.__employees
    
    @classmethod
    def get_employee_by_id(cls,emp_id):
        for emp in cls.__employees:
            if emp.id == emp_id:
                return emp  
        return None  
    
    @classmethod
    def remove_employee_by_id(cls,employee_id):
        cls.__employees=[emp for emp in cls.__employees if emp.id != employee_id]

    def __str__(self):
        return "{self.name}"

class Finance:
    

    TAX_THRESHOLD = 5000
    TAX_LOW = 0.1
    TAX_HIGH = 0.3
    HEALTH_INSURANCE_COST = 100
    RETIRMENT_CONTRIBUTION_RATE = 0.5

    @staticmethod
    def calculate_tax(salary):
        if salary < 30000:
            return salary * 0.1
        else: 
            return salary * 0.3
            
    @staticmethod
    def calculation_net_salary(gross_salary):
        tax = Finance.calculate_tax(gross_salary)
        retirment_contribution = Finance.RETIRMENT_CONTRIBUTION_RATE * gross_salary
        total_deductions = tax + Finance.HEALTH_INSURANCE_COST + retirment_contribution
        net_salary = gross_salary-total_deductions
        return net_salary
    

    
mohamed = Employee("Mohamed","30","Developer","1234","+20123654","wfgf54g5")
zahra = Employee("Zahra","32","Developer","15","+20123654","wfgf54g5")
print(AllEmployee.list_all_employees())
EmployeeFileHandler.read_and_add_to_AllEmployess('employees_data_enhanced.csv')
print(len(AllEmployee.list_all_employees()))