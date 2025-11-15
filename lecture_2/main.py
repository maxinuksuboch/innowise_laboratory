from datetime import datetime

def generate_profile(age : int) -> str:
    """
    Determines a user's life stage based on age.
    Returns one of: "Child", "Teenager", "Adult"
    """
    life_stage = ""
    if 0 <= age <= 12:
        life_stage = "Child"
    elif 13 <= age <= 19:
        life_stage = "Teenager"
    elif age >= 20:
        life_stage = "Adult"
    else:
        return "Wrong age"
    return life_stage


# Main part of the program

#Get the current year(used to calculate age)
current_year = datetime.now().year

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = current_year - birth_year

# Collect hobbies (loop continues until user types 'stop')
hobbies = []
hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

while hobby.lower() != 'stop':
    hobbies.append(hobby)
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

life_stage = generate_profile(current_age)

user_profile = {
    "name" : user_name,
     "age" : current_age,
     "stage" : life_stage,
     "hobbies" : hobbies
     }

# Output

print("---")
print("Profile Summary")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

# If user entered any hobbies, show them
if hobbies:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}): ")
    for hobby in user_profile["hobbies"]:
        print(f'- {hobby}')
else:
    print("You didn't mention any hobbies")
print("---")