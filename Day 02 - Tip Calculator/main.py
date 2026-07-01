print("Welcome to the Tip Calculator")
currency = input("Enter your currency name/symbol : ")
bill=float(input("Enter your bill amount: "))
tip=float(input("Enter the tip (%) you want to give: "))
people=float(input("How many people to split the bill: "))
total_bill= bill+ (bill * tip /100)
print(f" Total bill amount including tip :{currency}{total_bill}")
print(f"Each person should pay {currency}{total_bill/people:.2f}")
print("Thank you for shopping with us :-) ")

#In line 8 : starts the formatting instruction and .2 shows 2digit after decimal point and f formats the no. as floating point
#Its better to use this :whatever rounded no. u wanna show then f in line 8 rather then using round command.
#added line 2 and line 9 to make it look more haha.
