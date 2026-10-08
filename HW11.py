#Name: Jake Kreizenbeck
#Class: 5th Hour
#Assignment: HW11
import random

#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
numb_list = [random.randint(1,100),random.randint(1,100),random.randint(1,100)]
#3. Print the list.
print(numb_list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if numb_list[0]>numb_list[1] and numb_list[0]>numb_list[2]:
    print(numb_list[0])
    num = numb_list[0]
elif numb_list[1]>numb_list[0] and numb_list[1]>numb_list[2]:
    print(numb_list[1])
    num = numb_list[1]
elif numb_list[2]>numb_list[0] and numb_list[2]>numb_list[1]:
    print(numb_list[2])
    num=numb_list[2]
else:
    print("Two or more numbers are equal to each other")
#5. Tie the result (the largest number) from #4 to a variable called "num".
# already tied in number 4
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    if num % 3 == 0:
        print("Number is divisible by both 2 and 3")
    else:
        print("Number is divisible by 2")
else:
    if num % 3 == 0:
        print("Number is divisible by 3")
    else:
        print("Number is divisible by neither")