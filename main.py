def greet():
    print('welcome to the world of Valoda. This is an adventure game to help you learn a language.')
    character_name = input("What would you like to name your character?")
    print("which language would you like to learn?")
    print('1: Spanish')
    print('2: Chinese (Mandarin)')
    print('3: Arabic')
    language_choice = languages[str(input("Please enter the number corresponding to your choice > "))]

    player = character(character_name, "Unknown", 10, 1, ({}), ({}))
    instance = game_instance(language_choice)


    print("So, " + player.name + "...You want to learn " + instance.language + "?")
    confirmation = input("Y/N")

    while confirmation.upper() != "Y" or confirmation.upper() != "N":
        if confirmation.upper() == "Y":
            print("Let's begin...")
            retval = [player, instance]
            return retval
        elif confirmation.upper() == "N":
            print("Well, that's alright. Maybe another time.")
            return 0
        else:
            confirmation = input("Try again, Y/N")

languages = ({
    "1" : "Spanish",
    "2" : "Chinese (Mandarin)",
    "3" : "Arabic"
})

class character:
    def __init__(self, name, character_class, hp, level, inventory, equipped):
        self.name = name
        self.character_class = character_class
        self.hp = hp
        self.level = level
        self.inventory = inventory
        self.equipped = equipped

class game_instance:
    def __init__(self, language):
        self.language = language

if __name__ == "__main__":
    greet_return = greet()

    player = greet_return[0]
    instance = greet_return[1]