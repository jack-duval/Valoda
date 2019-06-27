import pandas as pd

class character:
    def __init__(self, name, character_class, hp, level, inventory, equipped, story_location):
        self.name = name
        self.character_class = character_class
        self.hp = hp
        self.level = level
        self.story_lcation = story_location

    def say(self, message):
        print(self.name + ": " + message)

    def ask(self, message):
        val = input(self.name + ": " + message)
        return val

class game_instance:
    def __init__(self, language, story_location):
        self.language = language
        self.story_location = story_location

    def set_location(self, new_location):
        self.story_location = new_location

languages = ({
    "1": "Spanish",
    "2": "Chinese (Mandarin)",
    "3": "Arabic"
})

game_state = []

story_location = ({
    "NEW",
    "GREET"
})
def save_game(player_name,
              player_class,
              player_hp,
              player_level,
              instance_language,
              instance_location):
    game_state.append({
        "PLAYER_NAME" : player_name,
        "PLAYER_CLASS" : player_class,
        "PLAYER_HP" : player_hp,
        "PLAYER_LEVEL" : player_level,
        "INSTANCE_LANGUAGE" : instance_language,
        "STORY_LOCATION" : instance_location
    })

    pd.DataFrame(game_state).to_csv(r'./savefile.csv')
