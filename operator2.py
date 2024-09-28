#Take height and weight from user
#BMI formula:Weight/(height/100)**2
#if bmi<18.4 print("underweight")
#if bmi<=24.9 print("You are healthy")
#if bmi<=29.9 print ("You ARE OVERWEIGHT")
#IF bmi<= 34.9 print you are severly overweight
#if bmi<=39.9 print You are  obese
#else you are severly obese

height = float(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))
bmi = weight/(height/100)**2
if  bmi <18.4:
    print("You are Underweight")
elif bmi<=24.9 and bmi>=18.4:
    print("You are healthy")
elif bmi<=29.9 and bmi>=24.9:
    print ("You ARE OVERWEIGHT")
elif bmi<= 34.9 and bmi>=29.9:
     print("you are severly overweight")
elif  bmi<=39.9 and bmi>=34.9:
    print(" You are obese")
else:
    print("You are severly obese")