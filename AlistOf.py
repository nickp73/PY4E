from datetime import datetime

# This is my version roughly copied from the one I did in scratch
birds = []
now = datetime.now()

print("Please tell me what bird you have seen: ")
while len(birds) < 6:
    birds.append(input())

    if len(birds) < 6:
        print(f"Please add another bird: ")


print(f"You have seen the following birds: {birds} ")

#print(birds[4] + ':' + ' ' + now.strftime('%H:%M:%S %d-%m-%Y'))

#print(dir(birds))
#print(help(birds))
#####################################################################
#####################################################################
# This is what the LLM returned after I uploaded my example.
"""birds = []

print("Bird Spotter (Type 'exit' to see your list)")

# Start with an empty string so the loop can begin
user_input = ""

while user_input != "exit":
    user_input = input("Which bird did you see? ")

    if user_input != "exit":
        # Capture the time RIGHT NOW
        now = datetime.now()
        timestamp = now.strftime('%H:%M:%S')

        # Combine them into one string and add it to our list
        birds.append(user_input + " at " + timestamp)
        print(f"Logged {user_input}!")

print("\n--- Final List ---")
# This prints the whole list at the end
print(birds)"""