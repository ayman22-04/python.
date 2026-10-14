# Bill Splitter Program

bill = float(input("Enter total bill amount: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people splitting the bill: "))

# Calculate Tip
tip = bill * tip_percent / 100

# Calculate Total Bill
total_bill = bill + tip

# Calculate Amount Per Person
if people > 0:
    per_person = total_bill / people

    print("\n----- BILL SUMMARY -----")
    print("Original Bill:", bill)
    print("Tip Amount:", tip)
    print("Total Bill with Tip:", total_bill)
    print("Number of People:", people)
    print("Each Person Pays:", round(per_person, 2))

else:
    print("Number of people must be greater than zero.")

print("Program Finished Successfully!")