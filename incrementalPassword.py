import random

print("This is a simple password generator")

print("Please enter the name of your first pet: ")
password = input()
print(password)
print("Please enter your favourite colour: ")
password += input()
print(password)
print("Please enter your favourite song: ")
password += input()
print(password)

random_number = random.randint(10, 1000)
password += str(random.randint(1000, 9999))

print(f"Your password is: {password}")

