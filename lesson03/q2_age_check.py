name = input("What is your name? ")
age = int(input("How old are you? "))


if age >= 65:
    print(f"{name.title()} is a senior")
elif age >= 18 and age <= 64:
    print(f"{name.title()} is an adult")
elif age >= 13 and age <= 17:
    print(f"{name.title()} is a teenager") 
else:
    print(f"{name.title()} is a child")


