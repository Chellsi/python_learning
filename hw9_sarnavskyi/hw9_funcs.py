from random import randint
import time


def time_counter(func):

    def time_count():
        start_time = time.time()
        result = func()
        print(f'The game continued {int(time.time() - start_time)} seconds')
        return result

    return time_count


def get_random_number():
    number = randint(1, 101)
    return number


def get_number_from_user():
    while True:
        try:
            return int(input('Enter int: '))
        except:
            print('It\'s not int')


def check_numbers(to_guess, user_number):
    if to_guess == user_number:
        return True
    elif abs(to_guess - user_number) > 10:
        print('Cold')
        return False
    elif 10 >= abs(to_guess - user_number) >= 5:
        print('Warm')
        return False
    elif 4 >= abs(to_guess - user_number) >= 1:
        print('Hot')
        return False
    else:
        return False


def get_max_count():
    while True:
        inserted_item = input('Please, insert max number of attempts: ')
        if inserted_item.isdigit() and 0 < int(inserted_item):
            return int(inserted_item)
        else:
            print('Choose normal')


@time_counter
def loop_game():
    counter = 1
    max_count = get_max_count()
    number_to_guess = get_random_number()
    while counter <= max_count:
        user_number = get_number_from_user()
        if check_numbers(number_to_guess, user_number):
            print('You WIN!!!!')
            break
        elif counter == max_count:
            print(f'You lost! Searched number - {number_to_guess}')
        else:
            print('Try again')
        counter += 1


if __name__ == '__main__':
    print('Inside library')
    loop_game()





