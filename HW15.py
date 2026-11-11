#Name:
#Class: 5th Hour
#Assignment: HW15
import random, time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5, 0, -1):
    time.sleep(0.3)
    print(i)
else:
    print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for a in range(0, 31, 2):
    print(a)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for b in range(0, 30):
    if b % 3 == 0:
        continue
    else:
        print(b)
#4. Create a for loop that prints 5 different animals from a list.
anim = ["Dog","Cat","Bird","Cow","Parastratiosphecomyia stratiosphecomyioides"]
for c in anim:
    time.sleep(0.4)
    print(c)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
word = str(input("Enter a word: ")[::-1])
for c in word:
    print(c)
#6. Create a list containing 10 integers of your choice and print the list.
lis1 = [1,3,8,23,7,400,6,86,2,4]
print(lis1)
#7. Create two empty variables named evenNumbers and oddNumbers.
odd_numb = 0
even_numb = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for num in lis1:
    if num % 2 == 0:
        even_numb +=1
    else:
        odd_numb +=1

print(odd_numb)
print(even_numb)
#9. Create a variable that asks the user for an integer and an empty integer variable.
number = int(input("Enter a number: "))
list_numb = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for x in range(1,number+1):
    list_numb *= x
print(list_numb)