#Loops
from bdb import Breakpoint

#1. For Loop
#for variable name in the range
x = list(range (1,10, 1))
print(x)

for i in range(10, 0, -2):
    print(i)

my_list = list(range(10, 0 , -2))
print(my_list)

for Atul in range(0,10 -2):
    print(Atul)


#2. While Loop
#Syntax
variable_name = 0

i = 0
while i < 10:
    print(i," ")
    i = i+1


#1. Break
for i in range(0,10):
    print(i)
    if i== 5:
        break

for i in range(0,10, 1):
    if i == 6:
        print(i)
    else:
        pass # pass is used to ignore false output
        #print("no output")
        #break

for i in range(0,100):
    if i % 2 == 0:
        print(i)
    else:
        pass # pass is used to ignore false output


#2. Continue
#Skip the iteration and move to next

for number in range(10):
    if number % 2 == 0:
        continue
    else:
        print(number)


#Match Statement
browser_name = input("Enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute the firefox code")
    case "firefox":
        print("Execute the firefox code")
    case "Chrome":
        print("Execute the Chrome code")
    case "Edge":
        print("Execute the Edge code")
    case "Safari":
        print("Execute the Safari code")
    case _:
        print("Browser not found")