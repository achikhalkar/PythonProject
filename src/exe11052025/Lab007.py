#Find max between 3

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))
num3 = int(input("Enter the num3"))

if num1 > num2 and num1 > num3:
    print (num1)

elif num1 < num2 and num2 > num3:
    print (num2)

else:
    print (num3)


#Grade Calculator
score = int(input("Enter score"))
if score >= 90:
    #grade= "A"
    print("The letter grade is: {A}")

elif score >= 80:
    #grade = "B"
    print("The letter grade is: {B}")

elif score >= 70:
    #grade = "C"
    print("The letter grade is: {C}")

elif score >= 60:
   #grade = "D"
    print("The letter grade is: {D}")

else:
        grade='F'
        print("The letter grade is: {F}")



