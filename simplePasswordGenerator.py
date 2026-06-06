import random
print("This is a simple password generator")

print("Please enter the name of your first pet: ")
user_pet_name = input()
print(f"Your first pet's name is: {user_pet_name}")

print("Please enter the name of your favorite colour: ")
user_favorite_colour = input()
print(f"Your favorite colour is: {user_favorite_colour}")

print("Please enter the name of your favorite song: ")
user_favorite_song = input()
print(f"Your favorite song is: {user_favorite_song}")

random_number = random.randint(10, 1000)

generated_password = f"{user_pet_name[:4]}{user_favorite_colour[:3]}{user_favorite_song[:4]}{random_number:04d}"
print(f"Generated password: {generated_password}")
