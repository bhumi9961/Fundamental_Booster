print("Welcome to the Interactive Personal Data Collector")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meter: "))
number = int(input("Please enter your favourite number: "))

print("Thank you!! Here is the information we collected:")

print("Name:",name,"(type:",type(name), ", Memory Address:",id(name),")")
print("Age:",age,"(type:",type(age), ", Memory Address:",id(age),")")
print("Height:",height,"(type:",type(height), ", Memory Address:",id(height),")")
print("Favourite Number:",number,"(type:",type(number), ", Memory Address:",id(number),")")

birth_year = 2026 - age
print("Your birth year is approximately: " +str(birth_year) + " (based on your age of " +str(age) +")") 

print("Thank you for using Data collector. Goodbye!")