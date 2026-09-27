import random

name = input("Enter the name: ").title()
dob = input("Enter the DOB[DD-MM-YYYY]:")
special =['@','#','$','*','&','%','.',',']

password = name+random.choice(special)+dob[-4:]

print("Generated password:",password)