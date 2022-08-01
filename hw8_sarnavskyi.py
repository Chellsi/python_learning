import random

MESSAGE_CHOOSE_FIGURE = "Please, choose your figure - insert '1' for Rock, '2' for Scissors, '3' for Paper.\n" \
                        "Or insert '0' if you want your figure to be chosen randomly: "
MESSAGE_CHOOSING_ERROR = "You have inserted wrong value!"
MESSAGE_CONTINUE_GAME = "Want to continue game? Type 'Y' to continue or 'N' to finish and view score: "
MESSAGE_CONTINUE_ERROR = "Please, type 'Y' or 'N'!"


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


def convert_figure(figure):
    """
    Function which converts number from 1 to 3 to corresponding figure
    Args:
        figure (int): number in range 1-3

    Returns:
        (str): text containing figure of game

    """
    if figure == 1:
        return 'Rock'
    elif figure == 2:
        return 'Scissors'
    elif figure == 3:
        return 'Paper'


def calc_result(player_figure, bot_figure):
    """
    Function which calculates winner of exact party depending on user`s and bot`s game figures
    Args:
        player_figure (int): pseudo-randomly chosen or inserted by user integer from range 1-3
        bot_figure (int): pseudo-randomly chosen integer from range 1-3

    Returns:
        (str): party tesult - user victory, bot victory or draw

    """
    if player_figure == bot_figure:
        return 'draw'
    elif player_figure == 1 and bot_figure == 2:
        return 'player_victory'
    elif player_figure == 2 and bot_figure == 1:
        return 'bot_victory'
    elif player_figure == 2 and bot_figure == 3:
        return 'player_victory'
    elif player_figure == 3 and bot_figure == 2:
        return 'bot_victory'
    elif player_figure == 3 and bot_figure == 1:
        return 'player_victory'
    elif player_figure == 1 and bot_figure == 3:
        return 'bot_victory'


def receive_user_figure():
    """
    Function which checks user input when he is choosing game figure
    Returns:
        (int): pseudo-randomly chosen or inserted by user integer from range 1-3

    """
    while True:
        inserted_figure = input(MESSAGE_CHOOSE_FIGURE)
        if inserted_figure.isdigit() and 0 < int(inserted_figure) <= 3:
            return int(inserted_figure)
        elif inserted_figure == '0':
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
    user = receive_user_figure()
    bot = choose_random()
    result = calc_result(user, bot)
    user_string = convert_figure(user)
    bot_string = convert_figure(bot)
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
