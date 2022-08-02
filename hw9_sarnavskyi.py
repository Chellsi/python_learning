from random import randint


def get_random_number():
    """
    Returns:
        (int)
    """
    number = randint(1, 101)
    return number


def get_number_from_user():
    """
    Returns:
        (int)
    """
    while True:
        try:
            return int(input('Enter int: '))
        except:
            print('It\'s not int')


def check_numbers(to_guess, user_number):
    """

    Args:
        to_guess (int):
        user_number (int):

    Returns:
        (bool):
    """
    print(f'---> {to_guess}')
    if to_guess == user_number:
        return True
    else:
        return False


def game():
    number_to_guess = get_random_number()

    while True:
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            break

    print('You WIN!!!!')


game()
