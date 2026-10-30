name = input("Your name? ")
birth_year = input("Birth year? ")

birth_year1 = int(birth_year)

current_year = 2026
age = current_year - birth_year1

print(f"Hi {name.title()}, you are about {age} years old in 2026")