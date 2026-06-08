from datetime import datetime

birds = []

print("--- Bird Logger ---")

# 1. Collect 3 sightings from the user
while len(birds) < 3:
    bird_name = input("What bird did you see? ").strip()

    # Capture the exact time right now
    now = datetime.now()
    spotted_time = now.strftime('%H:%M:%S')

    # Store them as a mini-list: [name, time]
    birds.append([bird_name, spotted_time])
    print(f"Logged {bird_name} at {spotted_time}\n")

print("--- Log Complete ---\n")

# 2. Querying the list
search_bird = input("Which bird do you want to check the time for? ").strip()

# We set a flag to check if we actually find the bird
found = False

for entry in birds:
    # entry[0] is the Bird Name, entry[1] is the Time
    if entry[0].lower() == search_bird.lower():
        print(f"You saw the {entry[0]} at {entry[1]}")
        found = True
        break

# If the loop finishes and 'found' is still False, the bird wasn't there
if not found:
    print(f"Sorry, I couldn't find a sighting for '{search_bird}'.")