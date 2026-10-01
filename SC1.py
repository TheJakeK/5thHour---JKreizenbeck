#Name:
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemies = {
    "Zombie": {
        "Health": 20,
        "Damage": 5,
        "Amount": 1,
    },
    "Skeleton": {
        "Health": 25,
        "Damage": 3,
        "Amount": 1,
    },
    "Zombie Hoard": {
        "Health": 10,
        "Damage": 2,
        "Amount": 5,
    },
    "Spider": {
        "Health": 10,
        "Damage": 5,
        "Amount": 1,
    },
    "Juggernaut": {
        "Health": 50,
        "Damage": 15,
        "Amount": 1,
    },
}
qstn1 = (int(input("Enter Zombie Damage")))
enemies["Zombie"].update({"Damage" : qstn1})
print(enemies["Zombie"]["Damage"])

qstn2 = (int(input("Enter Skeleton Damage")))
enemies["Skeleton"].update({"Damage" : qstn2})
print(enemies["Skeleton"]["Damage"])

qstn3 = (int(input("Enter Zombie Hoard Damage")))
enemies["Zombie Hoard"].update({"Damage" : qstn3})
print(enemies["Zombie Hoard"]["Damage"])

qstn4 = (int(input("Enter Spider Damage")))
enemies["Spider"].update({"Damage" : qstn4})
print(enemies["Spider"]["Damage"])

qstn5 = (int(input("Enter Juggernaut Damage")))
enemies["Juggernaut"].update({"Damage" : qstn5})
print(enemies["Juggernaut"]["Damage"])


