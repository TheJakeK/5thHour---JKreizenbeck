#Name: Jake Kreizenbeck
#Class: 5th Hour
#Assignment: SC2
print("Hello World")

#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be told their BMI as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

ht = int(input("Please enter your height in (Inches)"))
wt = int(input("Please enter your weight in (Pounds)"))

bmi = (wt/(ht ** 2))*703
print(bmi)

if bmi<18.5:
    print("You are Underweight")
elif bmi>18.4 and bmi<25:
    print("You are Normal")
elif bmi>25 and bmi<30:
    print("You are Overweight")
else:
    print("You are Obese")

print("Thank You!")