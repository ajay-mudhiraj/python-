# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:31:46 2024

@author: Ajay
"""

x_y_z = input("enter three numbers:").split(sep= '_')

print(x)
print(_y)
print(_z)
s=2
print(type(s))

print(25)
type(25)
print('Hello"  "World', 123 end ='\n')

import time
print("Loading", end="", flush=True)
time.sleep(1)
print(".", end="", flush=True)
time.sleep(1)
print(".")

4+5/5*2

{1,2} =={1,2}

{'one':1} =={'one':2}

[1,2]==[1,2]

5.5%2

'5.0' == 5

5.0 == 5
n= 6-5j
n=4+j

'ABC'=='ABC'
'abC'<'aBc'

'9'>'9.6'
9!='9'
x = 0778

# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String:")
print(text.title())

# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())

# original string never changes
print("\nOriginal String")
print(text)



nm = 'ajay'


nm.center(15,'#')



'######ajay#####'






You have a list of words: ["Learning", "Python", "is", "awesome"].
Write a Python script to join them with " -> " as a delimiter.

l = ["Learning", "Python", "is", "awesome"]

l_join = '->'.join(l)

l_join


l =['learning']


l_join ='_'.join(for i in l:)

l_join

l =["Learning", "Python", "is", "awesome"]

for i in l:
    if len(i)%2 ==0:
        print(i)
else:
    print('task acomplished')


l ='learning'



a = 4
a<<2
a>>3

dic={'a'':4,''h':2,'w':0,5:4.3}
del dic
dic

line = "I'll come by then."

eline = "" 
for i in line: 
	eline += chr(ord(i)+3) 
print(eline)



my_string = 'geeksforgeeks'
new = ''
for i in range(len(my_string)): 
	new+=my_string[i].upper() 
print(new)
print (my_string)



my_string = 'geeksforgeeks'
for i in range(len(my_string)): 
	print (my_string, end=" ") 
	my_string = 'a'


len(my_string)


set1 = {1, 2, 3} 
set2 = set1.copy() 
set2.add(4) 
print(set1)
set2



int(2e-04)

ane = 'ajay'
int(ane)


txt = "We are the so-called \"Vikings\" from the north."

txt


h = [(6,7),8,7]

l = h.Deecopy()
l[0] = 1
l

h

l =[]
l.append([1,2,3,4,5])
l
l[0][2]

l.remove(l[0][2])

numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

numbers = [5, 10, 15, 2, 25]
largest = max(numbers)
smallest = min(numbers)

print("Largest number:", largest)
print("Smallest number:", smallest)



l = [1,2,3,4]

del l[0]
l
m =  ','.join(l)





marks = int(input("enter a number"))
if marks>=90:
    print("Grade A")
elif marks>=75 and marks<90:
    print("Grade B")

elif marks>=50 and marks<75:
    print("Grade c")

else:
    print("Grade F")

year = int(input("enter a year:"))

'''
year%4==0 and year%100!=0 and year%400==0 is leap year

year!==0 and year%100==0 and year%400!==0 non leap year

'''
if (year%4!=0 and year%400!=0) or (year%100==0):
    print("non leap")

else:
    print("leap")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Non-leap year")




year = int(input("Enter a year: "))
if (year%4==0) or (year%400==0 and year%100!=0):
    print("leap")

else:
    print("non leap")

# Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    print(f"The result is: {num1 + num2}")
elif operator == '-':
    print(f"The result is: {num1 - num2}")
elif operator == '*':
    print(f"The result is: {num1 * num2}")
elif operator == '/':
    if num2 != 0:  # Check for division by zero
        print(f"The result is: {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")

n1 = 2
n2 = 3
n3 = 4

if (n1>n2) and (n1>n3):
    print("n1")

elif (n2>n1) and (n2>n3):
    print("n2")

elif (n3>n1) and (n3>n1):
    print("n3")



x = int(input("enter a number:"))

    
if x in range(10,50):
    
   print("inside")

else:
   print("outside")


number_of_units = int(input("enter the units:"))
if number_of_units <=100:
    print(f'{number_of_units*5} rupees is your electricity bill')

elif number_of_units>100 and number_of_units<200:
    print(f'{number_of_units*7} rupees is your electricity bill')

elif number_of_units>200:
    print(f'{number_of_units*10} rupees is your electricity bill')

num = int(input("enter a number:"))
if num%5==0 and num%7==0:
    print("divsible by 5 and 7")

elif num %5==0:
    print("divisble by 5")

elif num%7==0:
    print("divisble by 7")



# Input the price of the product
price = float(input("Enter the price of the product: ₹"))

# Calculate the discount based on conditions
if price < 500:
    discount = 0
    print("No discount applicable.")
elif 500 <= price <= 1000:
    discount = price * 0.10
    print("10% discount applied.")
else:
    discount = price * 0.20
    print("20% discount applied.")

# Calculate the final price
final_price = price - discount

# Display the discount and final price
print(f"Discount: ₹{discount:.2f}")
print(f"Final Price after discount: ₹{final_price:.2f}")


number = int(input("enter a number:"))
fact =1

if number<0:
    print("enter positive number")
elif number==0:
    print(fact)
elif number>0:
    print(fact)

# Factorial program using if-else statements
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Input from the user
number = int(input("Enter a number: "))

# Output the result
print(f"The factorial of {number} is: {factorial(number)}")


n = int(input("enter n number:"))
sum=0
for i in range(n+1):
    sum+=i
    print(sum)





for i in range(1,51):
    if i%2==0:
        print(i,"even")

    
for i  in range(10,0,-1):
    print(i)



num = int(input("enter a number:"))


for i in range(1,11):
    print(f'{num}*{i}={num*i}')


vowels ="AEIOUaeiou"

count = 0

string = input("enter a number:")



for i in string :
     if i in vowels:
         count+=1
 
  
print(count)




number = int(input("enter a number:"))

if number < 0:
    print("enter positive number")
elif number ==0 or number==1:
    print("number factorial is 1")

elif number >0:
    fact = 1
    for i in range(1,number+1):
        fact*=i
print(fact)


number = int(input("enter a number:"))
sum = 0
for num in range(number+1):
   sum+=num

print(sum)



for i in range(5):
    for j in range(5-i):
        print('*', end = '')
    print()






#zip and unzip function sin python

'''
 combines the two iterable and form a single iterable pair up the elemnets of each element with the first iterable along with first
 elemnet of second iterable and resultant iterble return tuples . it returns tuple due to immmutability nature and memory efficient
'''
'''
 unzip function is used for separated the combined iterables using the * as the unpack the zipped iterables 
'''
 
students = ['John', 'Emma', 'Sophia']
scores = [85, 90, 88]

combined_iterables = zip(students,scores)

for pair in combined_iterables:
    print(pair)


new = set(combined_iterables)
new





students = ['John', 'Emma', 'Sophia']

for i in students:
    print(i)

tup = tuple(students)

tup

data = [(1, 'b'), (3, 'a'), (2, 'c')]
# Using sort()
data.sort(key=lambda x: x[1])
print(data)  # Output: [(3, 'a'), (1, 'b'), (2, 'c')]

# Using sorted()
sorted_data = sorted(data, key=lambda x: x[0], reverse=True)
print(sorted_data)  # Output: [(3, 'a'), (2, 'c'), (1, 'b')]

'''
Sort a list of dictionaries by a specific key.
Use sorted() to sort a string in descending alphabetical order.
Write a program to sort a list of tuples based on the length of their second element
'''

l = [{'name':'ajay', 'name':'vinnu', 'name':"dathu"}]
l.sort(key = lambda x:x['name'])
l

def greet(name):
    return name

name = greet('Hello rockstar Ajay')
greet(name)


def add_numbers(*a):
    return sum(a)


add_numbers(2,3,4,5)


number = int(input("enter a number:"))
def is_even(number):
    if number%2==0:
        return True
    else:
        return False


is_even(number)


def find_largest(a, b, c):
    if (a>b)and (a>c):
        print('a is larger')

    elif (b>a) and (b>c):
         print("b is larger")
         
    else:
         print("c is larger")
         
         
find_largest(1,2,3)
         
         
         
number = int(input("enter a  number:"))

def find_fact(number):
  if number<0:
    print("number doesnot exist factorial")
  elif number==0 or number==1:
    print("factorial of given number is 1")
  elif number>0:
      fact = 1
      for i in range(1,number+1):
          fact*=i
      print(fact)
find_fact(number)



# Input from the user
number = int(input("Enter a number: "))

# Function to calculate factorial
def find_fact(number):
    if number < 0:
        print("Factorial does not exist for negative numbers.")
    elif number == 0 or number == 1:
        print("Factorial of the given number is 1.")
    else:
        fact = 1  # Initialize factorial variable
        for i in range(1, number + 1):
            fact *= i  # Multiply fact by each number in the range
        print(f"The factorial of {number} is {fact}")

# Call the function
find_fact(number)


string = input("enter a string:")

def reverse_string(string):
    return string[::-1]
reverse_string(string)


string = input("enter a string:")
vowels = 'AEIOUaeiou'
def count_vowels(string):
    count =0
    for i in string:
        if i in vowels:
            count+=1
    print(count)


count_vowels(string)


def square_numbers(*numbers):
  l = {x:x**2 for x in numbers}
  return l

square_numbers(1,2,3,4,5)


def is_palindrom(string):
    if string[::]==string[::-1]:
          return True
    else:
        return False



is_palindrom('radar')

def count_uppercase(string):
    count = 0
    for i in string:
        if i is i.upper():
            count+=1
    print(count)

count_uppercase("AJAY")

a = [1, 2, 3]
b = [1, 2, 3]  # Two separate objects with the same value

print(a is b)  # False
print(a == b)  # True

id(a)
id(b)

a = "hello"
b = "hello"

print(a is b)  # True
print(a == b)  # True

a = 100
b = 100

print(a is b)  # True
print(a == b)  # True


def fact(number):
  fact=1
  if number>=0:
   for i in range(1,number+1):
      fact*=i

   print(fact)
  else:
      print("fact doesn't exist for negative numbers")

fact(-8)


'''
n = 5
0,1,2,3
fib(3) = 0,1,1

fib(5) = 0,1,1,2,3,
'''










def fibonnice(n):
    
    for i in range(0,n): #(0,1,2,3,4)
        if i 

fibonnice(3)

def fact(number):
   fact=1
  if number>0:
   for i in range(1,number+1):
      fact*=i

   print(fact)


def fibonacci(n):
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print([0])
    elif n == 2:
        print([0, 1])
    else:
        fib = [0, 1]  # Initialize the first two numbers
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])  # Add the last two numbers
        print(fib)

fibonacci(3)

def greet(name):
    print(f'Hello {name} Welcome!')


greet('Ajay')


def calculate(a,b,operation):
    if operation == 'add':
        return a+b
    elif operation == 'mul':
        return a*b
    elif operation =='divide':
        return a/b
    elif operation == 'sub':
        return a-b
    else:
        print('enter valid operation')

calculate(1,2,'mod')
 

def area(r):
    return 3.14*r*r

area(2)


def fib(n):
    fib = [0, 1]
    if n <= 0:
        return[0] 
    elif n==1:
        return [0]
    elif n == 2:
        return fib
        
    for i in range(2,n):
        fib.append(fib[-1]+fib[-2])
    return fib
fib(5)


def is_prime(n):
    if n <=1:
        return  False
    elif n <=3:
        return True
    elif n%2==0:
        return False
    for i in range(2,int(n**0.5)+1,2):
            if n%2==0:
         
              return False
    return True

is_prime(5)





def sum_of_squares(n):
  sum = 0
  for i in range(n):
      sum+=i**2 
  return sum
  


sum_of_squares(5)



def find_div(n):
    div = []
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
    return div

find_div(8)


def reverse_string(string):
    return string[::-1]

reverse_string('python')



def merge_dicts(dict1,dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

merge_dicts({'a':1}, {'b':2})



def print_pattern(n):
    for i in range(1, n):
        for j in range(i+1):
            print(j*'*', end ='')
        print()

print_pattern(4)


def print_pattern(n):
    # Loop through rows
    for i in range(1, n + 1):
        # Print '*' i times on each row
        print('*' * i)

# Test the function
print_pattern(4)

def is_prime(n):
    if n < 2:
        return False
    elif n > 2:
        for i in range(2,int(n**0.5)+1):
            if n%2 ==0:
                return False
        return True

is_prime(29)


my_dict = {"Ajay":8247411869,"daddy":8326198553,"maa":8008540567}

def fizzbuzz(n):
    for i in range(1,n+1):
        if (i%3==0) and (i%5==0):
            print('FIZZBUZZ')
        elif (i%3==0) and (i%5!=0):
            print('FIZZ')
        elif (i%5==0) and (i%3!=0):
            print("BUZZ")
    else:
        print(i)

fizzbuzz(8)


def fizzbuzz(n):
    for i in range(1, n + 1):  # Start from 1 to n
        if (i % 3 == 0) and (i % 5 == 0):
            print('FIZZBUZZ')
        elif (i % 3 == 0) and (i % 5 != 0):
            print('FIZZ')
        elif (i % 5 == 0) and (i % 3 != 0):
            print("BUZZ")
        else:
            print(i)

fizzbuzz(8)






























