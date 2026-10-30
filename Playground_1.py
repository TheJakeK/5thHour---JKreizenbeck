#Black Jack

import random as r
J = 10
Q = 10
K = 10
A = 11
deck = ["A","A","A","A",2,2,2,2,3,3,3,3,
        4,4,4,4,5,5,5,5,6,6,6,6,
        7,7,7,7,8,8,8,8,9,9,9,9,
        "J","J","J","J","Q","Q","Q","Q",
        "K","K","K","K",]

Chip = 500
print("Current Chip Ammount:",Chip)
Bid = int(input("How many chips would you like to bid"))
if Bid > Chip:
    print("Not enough chips!")
elif Bid < 1:
    print("Enter a numer 1 -",Chip)
else:
    Chip = Chip - Bid
    print("Chip Amount:", Chip)

phand = []
dhand = []

phand.insert(random.choice(deck))
if phand[0] == "A":
Ace1 = int(input("Should Ace be an 1 or 11?"))
elif phand[0]  "A":
phand.insert(random.choice(deck))

print("Cards:" phand)
