#Name:Jake Kreizenbeck
#Class: 5th Hour
#Assignment: SC3
print("Hello World!")
#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
Num = 0

while Num < 99:
    Num += 1
    if Num % 3 == 0:
        if Num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif Num % 5 == 0:
            print("Buzz")
    else:
        print(Num)