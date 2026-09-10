#Name: Jake Kreizenbeck
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
num_list = [67, 89, 910, 2, 5, 32, 31, 8, 1]
#2. Sort the list from highest to lowest.
num_list.sort()
print(num_list)
#3. Create an empty list.
empt_list = []
#4. Remove the median number from the first list and add it to the second list.
empt_list.insert(0,31)
num_list.pop(4)
#5. Remove the first number from the first list and add it to the second list.
empt_list.append(num_list[0])
num_list.pop(0)
#6. Print both lists.
print(num_list)
print(empt_list)
#7. Add the two numbers in the second list together and print the result.
empt_list_subsum = empt_list[0] + empt_list[1]
print(empt_list_subsum)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
num_list.append(empt_list[1])
empt_list.pop(0)
print(empt_list)
print(num_list)
#9. Sort the first list from lowest to highest and print it.
num_list.sort()
print(num_list)