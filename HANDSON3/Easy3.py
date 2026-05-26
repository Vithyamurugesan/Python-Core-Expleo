def salary_hike(old_salary, hike):
    new_salary = old_salary + (old_salary * hike / 100)
    return new_salary
salary = float(input("Enter old salary per month: "))
hike = float(input("Enter hike percentage: "))
new_salary = salary_hike(salary, hike)
print("New Salary:", new_salary)