emp_dict = {
    'Employee' : {
        'Alice' : {'name': 'Ferry', 'age':25, 'salary': 65000},
        'Bob' : {'name': 'Merry', 'age':22, 'salary': 70000},
        'Rob' : {'name': 'Stark', 'age':32, 'salary': 80000}

     }  
}  

total_salary = sum(emp['salary'] for emp in emp_dict['Employee'].values())

# Add the percentage column
for emp in emp_dict['Employee'].values():
    emp['percentage'] = round((emp['salary'] / total_salary) * 100,2)

print(emp_dict)

#Another Example
student_grades = {"Alice":{"Math": 90, "Science": 80},
                  "Bob": {"Math": 70, "Science": 60},
                  "Charlie": {"Math": 60, "Science": 70}}

for key,val in student_grades.items():
    total = sum(val.values())
    student_grades[key]["Total"] = total

    
print(student_grades)





