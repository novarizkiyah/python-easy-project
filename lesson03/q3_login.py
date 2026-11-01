username = input("Please input your username: ")
password = input("Please input your password: ")


if username == 'admin' and password == 'python123':
    print("Access granted")
elif username != 'admin':
    print("Unknown user")
else:
    print("Wrong password")
