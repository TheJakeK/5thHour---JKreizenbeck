#Name: Jake Kreizenbeck
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
jake_car_dictionary = {
    "brand" : "Dodge",
    "model" : "Charger",
    "year" : [2019, 2020, 2021]
}
#3. Print the keys of the dictionary from #2.
print(jake_car_dictionary.keys())
#4. Print the values of the dictionary from #2
print(jake_car_dictionary.values())
#5. Print one of the three numbers from the list by itself
print(jake_car_dictionary["year"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
jake_car_dictionary.update({
    "Trim" : "SXT"
})
#7. Print the entire dictionary from #2 with the updated key and value.
print(jake_car_dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
class_list = {
    "student_1": {
        "Name": "Wyatt",
        "Grade": 9,
        "Age": 14,
    },
    "student_2": {
        "Name": "Ethan",
        "Grade": 10,
        "Age": 15,
    },
    "student_3": {
        "Name": "Oliver",
        "Grade": 9,
        "Age": 14,
    },
}
#9. Print the names of all three classmates on the same line.
print(class_list["student_1"]["Name"], class_list["student_2"]["Name"], class_list["student_3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
class_list.pop("student_3")
print(class_list)
