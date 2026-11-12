total = 0

number = int(input("Number? "))

while number != 0 :
    total = total + number
    number = int(input("Number? "))
print(f"Total: {total}")