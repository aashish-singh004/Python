3rd of July Day 04  , lets learn about random , and to import random like to use its functions, we have to run a command first

import random
{then we can use random module functions which is -}

1- random.randint(a,b) - returns a random integer a and b (both included)

import random

num= random.randint(1, 10)

print (num) #the output will be random no. b/w 1 and 10 everytime i run this small code 

2- random.random() - returns a random decimal number b/w 0.0 <= 1.0 , Example

import python

 print(random.random())

output will be anything like 0.54321 or 0.998 but it never will be 1 and if we want the decimal digits to be big, we can do like this

import random

print(random.random() *10) or we can do anything + - etc too instead of multiply

3- random.uniform(a,b) - gives us random decimal b/w two numbers with range 1.0-5.0

import random

print(random.uniform(1,5))    #output will be anything like 3.48 etc

4- random.choice() - randomly picks one item like

import random

fruits = ["apple" , "banana" , "mango"] #this [ bracket is used because it is a list and for list we use this

print(random.choice(fruits))  #output will be anything like apple or banana or mango everytime different 

5- random.suffle() - mixes a list, like if we choose [1,2,3,4,5] and run our code, everytime output will be shuffled.

6- random.sample() -returns random items

import random

names = ["a", "b" , "c" , "d"]

print(random.sample(names,2) #output will be c and a and everytime we run it will be a random 2 or 3 if we type in our code 3 

Lets talk bout list- A list stores multiple values in a single variable.- like for example,

hehe = [ "1" , "2" , "3"] 
print(hehe)

I can add one more word in the variable like hehe[1] = 1.1 and then if i print(hehe), output will be 1, 1.1 , 2 ,3 
Can also add last word like hehe.append(4) output will be 1 1.1 2 3 4

to add multiple item in last use .extent like hehe.extend([ "5" , "6"]) so the output will be 1 1.1 2 3 4 5 6

list_name[outer_index][inner_index]

Outer Index → Select the list

Inner Index → Select the item






