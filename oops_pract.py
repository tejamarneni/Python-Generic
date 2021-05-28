# oops practice this code is inspired from Corey Schafer's YouTube channel

class Employee():


    def __init__(self,first_name,last_name,Title,Salary,Designation):
        self.first_name = first_name
        self.last_name = last_name
        self.Title = Title
        self.Salary = Salary
        self.Designation = Designation

  
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def email(self):
        return self.first_name.lower() + '.' + self.last_name.lower() + '@company.com'

    def change_Title(self,title):
        self.Title = title  

    def salary_hike(self,hike):
        self.Salary = self.Salary + hike  


class Devloper(Employee):


    def __init__(self,first_name,last_name,Title,Salary,Designation,Prog_lang=None):
        super().__init__(first_name,last_name,Title,Salary,Designation)  
        if Prog_lang is None:
            self.Prog_language = []
        else:    
            self.Prog_lang = Prog_lang

    def add_lang(self,lang):
        if lang not in self.Prog_lang:
            self.Prog_lang.append(lang)   

    def remove_lang(self,lang):
        if lang in self.Prog_lang:
            self.Prog_lang.remove(lang)
        else:
            print(lang + ' is not in the list')         

class Manager(Employee):


    def __init__(self,first_name,last_name,Title,Salary,Designation,employees=None):
        super().__init__(first_name,last_name,Title,Salary,Designation)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees    

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print(emp + ' is not in the list')  

    def print_emp(self):
        for emp in self.employees:
            print(emp.full_name())                       


 #implementation   
dev_1 = Devloper('Teja','Marneni','Engineer',75000,'Associate',['Python','Java'])   
dev_2 = Devloper('Ravi','Marneni','Engineer',75000,'Associate',['C++','Java','C#'])   

print(dev_2.Prog_lang)
dev_2.remove_lang('C#')

print(dev_2.Prog_lang)

mgr_1 = Manager('Ravi','Marneni','Manager',75000,'Manager',[dev_1,dev_2]) 

mgr_1.print_emp()



