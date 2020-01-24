from setup import *

def change_scene(scene_arg):
    switch = {
        0: "Main Menu"
        1: "New Game"
    }

def greet():
    narrator = character("Mysterious Voice", "GOD", 999999, 100, ({}), ({}), "GREET")

    narrator.say('Welcome to the world of Valoda. This is an adventure game to help you learn a language.')
    character_name = narrator.ask("Who are you? (Enter chraracter name) > ")
    narrator.say("which language would you like to learn?")
    print('1: Spanish')
    print('2: Chinese (Mandarin)')
    print('3: Arabic')
    language_choice = languages[str(narrator.ask("Please enter the number corresponding to your choice > "))]

    player = character(character_name, "Unknown", 10, 1, ({}), ({}), "NEW")
    instance = game_instance(language_choice, "GREET")


    narrator.say("So, " + player.name + "...You want to learn " + instance.language + "?")
    confirmation = input("Y/N > ")

    while confirmation.upper() != "Y" or confirmation.upper() != "N":
        if confirmation.upper() == "Y":
            print("Let's begin...")
            retval = [player, instance]
            save_game(player.name, player.character_class, player.hp, player.level, instance.language, "GREET")
            return retval
        elif confirmation.upper() == "N":
            print("Well, that's alright. Maybe another time.")
            return 0
        else:
            confirmation = input("Try again, Y/N")

def main_menu():
    print("Valoda - Created by Jack Duval")
    response = input("New Game (N) or Load Game (L) > ")

    while response.upper() != "N" or response.upper() != "L":
        if response.upper() == "N":
            print("Starting new game...")


