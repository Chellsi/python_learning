import random

MESSAGE_CHOOSE_ITEM = "Please, choose your item - insert '1' for Rock, '2' for Scissors, '3' for Paper.\n" \
                        "Or insert '0' if you want your item to be chosen randomly: "
MESSAGE_CHOOSING_ERROR = "\033[1;31;31mYou have inserted wrong value!\033[0m"
MESSAGE_CONTINUE_GAME = "Want to continue game? Type 'Y' to continue or 'N' to finish and view score: "
MESSAGE_CONTINUE_ERROR = "\033[1;31;31mPlease, type 'Y' or 'N'!\033[0m"


score = {
    "player": 0,
    'bot': 0,
    'draws': 0
}


def choose_random():
    """
    Function to choose random number from 1 to 3
    Returns:
        (int): pseudo-randomly chosen integer from range 1-3

    """
    return random.randrange(1, 4, 1)


def convert_item(item):
    """
    Function which converts number from 1 to 3 to corresponding item
    Args:
        item (int): number in range 1-3

    Returns:
        (str): text containing item of game

    """
    if item == 1:
        return 'Rock'
    elif item == 2:
        return 'Scissors'
    elif item == 3:
        return 'Paper'


def calc_result(player_item, bot_item):
    """
    Function which calculates winner of exact party depending on user`s and bot`s game items
    Args:
        player_item (int): pseudo-randomly chosen or inserted by user integer from range 1-3
        bot_item (int): pseudo-randomly chosen integer from range 1-3

    Returns:
        (str): party tesult - user victory, bot victory or draw

    """
    if player_item == bot_item:
        return 'draw'
    elif player_item == 1 and bot_item == 2:
        return 'player_victory'
    elif player_item == 2 and bot_item == 1:
        return 'bot_victory'
    elif player_item == 2 and bot_item == 3:
        return 'player_victory'
    elif player_item == 3 and bot_item == 2:
        return 'bot_victory'
    elif player_item == 3 and bot_item == 1:
        return 'player_victory'
    elif player_item == 1 and bot_item == 3:
        return 'bot_victory'


def receive_user_item():
    """
    Function which checks user input when he is choosing game item
    Returns:
        (int): pseudo-randomly chosen or inserted by user integer from range 1-3

    """
    while True:
        inserted_item = input(MESSAGE_CHOOSE_ITEM)
        if inserted_item.isdigit() and 0 < int(inserted_item) <= 3:
            return int(inserted_item)
        elif inserted_item == '0':
            return choose_random()
        else:
            print(MESSAGE_CHOOSING_ERROR)


def validate_answer():
    """
    Function which checks user input when he is deciding to continue game or not
    Returns:
        (str): user`s decision to continue game or not

    """
    while True:
        inserted_data = input(MESSAGE_CONTINUE_GAME).upper()
        if inserted_data in ('Y', 'N', 'YES', 'NO'):
            return inserted_data
        else:
            print(MESSAGE_CONTINUE_ERROR)


def detect_party_winner():
    """
    Function which drives exact game party and detects it`s result.
    Prints result to user and updates score{} to track highscores.

    """
    user = receive_user_item()
    bot = choose_random()
    result = calc_result(user, bot)
    user_string = convert_item(user)
    bot_string = convert_item(bot)
    if result == 'player_victory':
        print(f"{user_string} beats {bot_string}. You won!")
        score["player"] += 1
    elif result == 'bot_victory':
        print(f"{bot_string} beats {user_string}. You lost!")
        score["bot"] += 1
    else:
        print(f"{bot_string} = {user_string}. Draw!")
        score["draws"] += 1


def init_game_loop():
    """
    Function which allows game to be run in a loop.
    It calls new party or ends the game and shows highscores depending on user`s decision.

    """
    user_answer = 'Y'
    while True:
        if user_answer in ('Y', 'YES'):
            detect_party_winner()
            user_answer = validate_answer()
        else:
            print(f'Final score:\n-User: {score["player"]}\n-Bot: {score["bot"]}\n{score["draws"]} times draw happened')
            break


init_game_loop()
