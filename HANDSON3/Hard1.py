def calculate_increment(salary, rating):

    if salary <= 0 or rating < 1 or rating > 10:
        return "Invalid Input"

    if 1 <= rating <= 4:
        salary = salary + (salary * 10 / 100)

    elif 4.1 <= rating <= 7:
        salary = salary + (salary * 25 / 100)

    elif 7.1 <= rating <= 10:
        salary = salary + (salary * 30 / 100)

    return int(salary)


salary = int(input("Enter the salary: "))
rating = float(input("Enter the appraisal rating: "))

print(calculate_increment(salary, rating))