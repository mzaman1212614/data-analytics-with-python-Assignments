# Qustion No 1:- Working with lists
        # first:Create a list called numbers  containing atleast 8 intergers.
        # Using for loop:
          # print all the numbers in the list
          # print the sum of all numbers
          # print only the  even numbers
numbers = [0,1,2,3,4,5,6,7]                      # creating a list 
for i in numbers:
    print(i)                                   # showing list

total = 0                      
for i in numbers:
    total = total + i
print(total)                                    # printing sum
for i in numbers:
    if i % 2 == 0:
        print(i)                                # showing even numbers

# Question No 2:- Dictinary Basics
              # Create a dictionary called student with the following keys
              # name
              # age 
              # course 
              # marks (must sotore a list of 3 marks)
              # Now using loops 
                # print all keys and their values
                # calculate the average of the marks
                # Display whether the student passed(average >=50) or failed
student = {"name":"Muhammad Zaman",
           "age":28,
           "course":"Data Anlytics with Python",
           "marks":[50,60,70]}  
for key,value in student.items():
    print(key,":",value)                                 # print all keys and their values
    
total  = 0
count = 0
for mark in student["marks"]:
    total = total + mark
    count = count + 1
average = total / count
print("Average marks:",average)                 # calculating average of marks
for mark in student["marks"]:
    if average >=50:
        print("Passed")                             # checkinng whether student passed or faliled
    else:
        print("Failed")

# Question No 3:
# Create a list called employees
# Each employee must be stored as a dictionary containing:
# name,department,salary
# using loops
#    print detail of all employees
#    find the employee with the highest salary
#    Calculate the total salary expense
employees = [{"name":"Muhammad Zaman","department":"Arts","salary":35000},
             {"name":"Habib","department":"Science","salary":40000},
             {"name":"Bilal","department":"Social Sciences","salary":25000}]    
for i in employees:                      # detail of all employees
    print(i)    
highest_salary = employees[0]["salary"]
for employee in employees:
    if employee["salary"] > highest_salary:                         # checking employee highest salarys
        highest_salary = employee["salary"]
print("Highest Salary:",highest_salary)        
total_expense = 0
for employee in employees:
    total_expense = total_expense + employee["salary"]                # claculating total expense
print("Total Expense:",total_expense)    

# Question No.4: While loop with user input
# Ask the user to enter numbers
# store the numbers in a list
# stops when the user enters -1
# After the loop ends:
                     # print the complete list
                     # print the largest number
                     # print the smallest number
numbers =[]
while True:
     number = int(input("Enter numbers:"))
     if number == -1:
          break 
     numbers.append(number)
print("Complete List:",numbers)
smallest = numbers[0]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number
print("Smallest Number:",smallest)            
print("Largest Number:",largest)
# Question No.5:Word frequency counter
#Ask the user to enter a sentence
#convert a sentence into a list of words
# use a dictionary to count how many times each word appears
# print the word frequency clearly
sentence = input("Enter a sentence:")
sentence = sentence.split()
count = {}
for word in sentence:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1
print(count)        
# Question No.6: Nested loops - Multiplication Table
# Use nested loops ,print a multiplication table from 1 to 5
for i in range(1, 11):

    for j in range(1, 11):
        print(i * j, end=" ")

    print()


  