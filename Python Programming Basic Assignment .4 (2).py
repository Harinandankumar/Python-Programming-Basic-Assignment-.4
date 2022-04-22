#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python Program to Find the Factorial of a Number?
# 
# 
# 
# 
# Ans:-

# In[3]:


def factorial(num):
    if (num < 1):
        return 1
    else:
        return num*factorial(num-1)
num = int(input('Enter a number: '))
value = factorial(num)
print(f'The Factorial of {num} is {value}')


# 2.	Write a Python Program to Display the multiplication Table?
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def generateTable(base,entries):
    for x in range(1,entries+1):
        print(f'{base} X {x} = {base*x}')

num = int(input('Enter a number: '))
values = int(input('Enter no of entries: '))
generateTable(num,values)


# 3.	Write a Python Program to Print the Fibonacci sequence?
# 
# 
# 
# 
# 
# Ans:-

# In[7]:


s_count = int(input('Enter the no of fibonacci sequences you want? '))
initial_list = [0,1]
if s_count < 0:
    print('Fibonacci Numbers are not available for Negative Numbers')
elif s_count <= 2 and s_count >= 0:
    print(initial_list)
else:
    for ins in range(s_count):
        if ins >= 2:
            initial_list.append(initial_list[ins-1]+initial_list[ins-2])
    print(f'The First {s_count} fibonacci series are: ',initial_list)


# 4.	Write a Python Program to Check Armstrong Number?
# 
# 
# 
# 
# Ans:-

# In[8]:


def checkArmstrongNumber():
    in_num = input('Enter a number: ')
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        print(f'{in_num} is a Armstrong Number')
    else:
        print(f'{in_num} is a Not Armstrong Number')

for x in range(2):
    checkArmstrongNumber()


# 5.	Write a Python Program to Find Armstrong Number in an Interval?
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def checkArmstrongNumber(in_num, storage):
    sum = 0
    for char in range(len(in_num)):
        sum = sum + pow(int(in_num[char]),3)
    if sum == int(in_num):
        storage.append(int(in_num))

start_interval = int(input('Enter the Start of the Interval: '))
end_interval = int(input('Enter the End of the Interval: '))
list_of_armstrong = []

if start_interval > end_interval:
    print("Start Interval Cannot be Greater than End Interval")
else:
    for number in range(start_interval,end_interval+1):
        checkArmstrongNumber(str(number),list_of_armstrong)
    print(f'The Armstrong numbers between {start_interval} and {end_interval} are {list_of_armstrong}')


# 6.	Write a Python Program to Find the Sum of Natural Numbers?
# 
# 
# 
# 
# Ans:-

# In[6]:


def sumOfNaturalNumbers(num):
    sum = num*((num+1)/2)
    print(f'Sum of {num} natural numbers is {sum}')
    
num = int(input('Enter a number: '))
sumOfNaturalNumbers(num)

