#Name:Jake Krezenbeck
#Class: 5th Hour
#Assignment: HW16
import random

#1. import the "random" library

#2. print "Hello World!"
print("Hello World")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
res = (a+b)/c
print(res)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
x = (round(res))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
print(x)
#6. Create a list of five different random integers between 1 and 10.
vars = [random.randint(1,10),random.randint(1,10),random.randint(1,10),
        random.randint(1,10),random.randint(1,10)]
print(vars)
#7. Print the 4th number in the list.
print(vars[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
vars.append(random.randint(1,10))
print(vars)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
vars.sort(reverse=True)
print(vars[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += i
#11. Create a list containing the names of five other students in the classroom.
name = ["Etan","Crud","Olicker","Sandi","Andtony"]
#12. Create a for loop that individually prints out the names of each student in the list.
for d in name:
    print(d)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for e in range(1, 100):
    if e % 10 == 0:
        break
    else:
        print(e)
#14. Free space. Do something creative. :)
m = str(input("Want to do something creative?"))
if m == "yes" or m == "Yes":
    print("Too Bad I Don't Want To!")
if m == "No" or m == "no":
    print("Good, I Didn't Want To Anyways.")