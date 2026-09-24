#Name: Jake Kreizenbeck
#Class: 5th Hour
#Assignment: HW8

import random

#1. Import the "random" library

#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
intvar1 = random.randint(1,10)
intvar2 = random.randint(1,10)
intvar3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(intvar1,intvar2,intvar3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
intvar1_sum = intvar1 + 2
intvar2_sum = intvar2 - 4
intvar3_sum = intvar3 * 1.5
#6. Print each result from #5 on the same line.
print(intvar1_sum,intvar2_sum,intvar3_sum)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
intlist = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
intlist.sort()
print(intlist)
#9. Add together the highest three numbers in the list from #7 and print the result.
intlist_sum = intlist[1] + intlist[2] + intlist[3]
print(intlist_sum)
#10. Create a list with 5 names of other students in this class and print the list.
namelist = ["Ethan", "Santiago", "Oliver","Anthony", "Wyatt"]
print(namelist)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(namelist)
print(namelist)
#12. Print a random choice from the list of names from #10.
namelistrand = random.choice(namelist)
print(namelistrand)