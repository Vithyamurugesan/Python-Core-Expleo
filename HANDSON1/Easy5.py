from datetime import datetime
birthdate=input("Enter your birthdate(YYYY-MM-DD): ")
birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
today=datetime.today()
age=today.year-birth_date.year
if(today.month,today.day)<(birth_date.month,birth_date.day):
    age-=1
print("Your age is:",age,"years")

