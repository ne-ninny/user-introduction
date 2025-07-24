def main():
    user_name = input("What is your name?: ")
    home_planet = input("What planet are you from?: ")
    user_generation = input("What generation are you?: ")
    
    user_title = royal_title(user_name, home_planet, user_generation)

    print(type(user_title))

def royal_title(name, home, generation):
    title = f"All hail, {name} of {home}!"
    what_generation = f"He's from the {generation} generation!"
    return title, what_generation

main()