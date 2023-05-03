print ("This is my first python code")

print (1080)

firstName = "John"
secondName = "Doe"

salary = "USD 2000"

name = firstName + " " + secondName

print (name)
print (salary)

form = 3

if (form < 3): 
    print ("You are not eligible for a captain position")

elif (form == 3):
    print ("You're not eligible for the deputy captain position")

else:
    print ("You're eligible for the captain position")

listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print (listNum[0])

for i in listNum:
    if i % 2 == 1:
        print(i)

for i in listNum:
    print(i**2)