salary = int(input("Please enter your salry: "))
year = int(input("How many years heve you worked with us: "))
discount = salary * 0.05
if (year >= 5):
    print("your discount is ", discount)
    print("Your net salary is= ", salary + discount )
else:
    print("No discount")
