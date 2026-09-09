#Name: Jake Kreizenbeck
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
name_list = ["Jim, Bob, Joe, Jake, Tim"]
#2. Append a new name onto the Name List.
name_list.append(input("Insert Person to List: "))
#3. Print out the 4th name on the list.
print(name_list)
#4. Create a list with 4 different integers in it.
num_list1 = [5, 3, 6, 8]
#5. Insert a new integer into the 2nd spot and print the new list.
num_list1.insert(1, 24)
print(num_list1)
#6. Sort the list from lowest to highest and print the sorted list.
num_list1.sort()
print(num_list1)
#7. Add the 1st three numbers on the sorted list together and print the sum.
num_list_sum = num_list1[0] + num_list1[1] + num_list1[2]
print(num_list_sum)
#8. Create a list with two strings, two variables, and too boolean values.
rand_list = ["Ball", "Mouse", 8, 4, True, False ]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(rand_list[int(input("Enter Index Location"))])