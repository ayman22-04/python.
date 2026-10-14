full_name = input("Enter your full name: ")

names = full_name.split()

if len(names) >= 2:
    first_name = names[0]
    last_name = names[-1]

    print("First Name:", first_name)
    print("Last Name:", last_name)
    print("Initials:", first_name[0].upper() + ". " + last_name[0].upper() + ".")
    print("Uppercase Name:", full_name.upper())
    print("Reversed Name:", full_name[::-1])
else:
    print("Please enter your first and last name.")