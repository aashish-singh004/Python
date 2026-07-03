if else statement statement like we studied in linux 
can use like this if:
else:    
we can write variable and operators too before colon


Comparison operators 
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== Equal to
!= not equal to

% - Modulo operator {tells us whats the remainder when we divide the no. like 10 % 3 will be 1 and 20 % 5 will be 0}
Can make a small project like , to let user choose a no. and then we can print if its a odd no. or a even no.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
  #indentation should be correct 


Nested if, elif, and else in Python

In python, we can write an if statement inside another if statement. This is called a nested if.
Python uses indentation spaces to show which code belongs to which block. 
if number % 2 == 0: print(f"{number} is even") 
    if number == 6: 
    print("Thala for a reason, suiiiiii") 
else: print(f"{number} is odd")

The nested if only runs if the first if is already True.

elif means "else if".
It is written between if and else when we want to check multiple conditions.


In short words, the outer if checks the main condition first.
If it is true. then the python enters the block and check another condition using if-elif-else. 
Memory trick - Outer if= Can i enter 
               Inner if-elif-else = Now what should i do?

I made a pizza outlet ordering thing- 

topping= input("To add pepperoni , Press Y or N ")
cheese= input("To add cheese , Press Y or N ")
print("Welcome to our Pizza Outlet")
bill = 0

# Pizza size
if user == "S":
    bill += 15
elif user == "M":
    bill += 20
elif user == "L":
    bill += 25
#we can either write billl = bill + 25 or straight bill +=3 , both are same.
# Pepperoni
if topping == "Y":
    if user == "S":
        bill += 2
    else:
        bill += 3

# Cheese
if cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
