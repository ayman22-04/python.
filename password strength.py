password = input("Enter your password: ")

if (len(password) >= 8
        and password.isupper() == False
        and password.islower() == False
        and any(char.isdigit() for char in password)):
    print("Strong Password")
elif len(password) >= 6:
    print("Moderate Password")
else:
    print("Weak Password")