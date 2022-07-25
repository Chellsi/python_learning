# task1
# Знову напишіть программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О, вам <>! Який цікавий вік!"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
# Наприклад:
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "О, вам 33 роки! Який цікавий вік!"

# Зробіть все за допомогою функцій! Для кожної функції пропишіть докстрінг.
# Не забувайте що кожна функція має виконувати тільки одне завдання і про правила написання коду.


def calc_user_response():
    """
    Function which takes user`s age and prints text message to user depends on his age

    Returns:
        (str): text message to user depends on his age
    """
    checked_age = validate_input()
    ages_string = create_ages_string(checked_age)
    if checked_age < 7:
        print(f"Тобі ж {checked_age} {ages_string}! Де твої батьки?")
    elif checked_age < 16:
        print(f'Тобі лише {checked_age} {ages_string}, а це фільм для дорослих!')
    elif checked_age > 65:
        print(f'Вам {checked_age} {ages_string}? Покажіть пенсійне посвідчення!')
    elif str(checked_age)[0] == str(checked_age)[1]:
        print(f'О, вам {checked_age} {ages_string}! Який цікавий вік!')
    else:
        print(f'Незважаючи на те, що вам {checked_age} {ages_string}, білетів всеодно нема!')


def create_ages_string(age_tostring):
    """
    Function to create string containing correct form of word "year/s" in ukrainian

    Args:
        age_tostring(int): verified age number inserted by user

    Returns:
        (str): string containing correct form of word "year/s" in ukrainian

    """
    if 20 > int(str(age_tostring)[-2:]) > 10:
        return f'років'
    elif str(age_tostring).endswith('1'):
        return f'рік'
    elif 4 >= int(str(age_tostring)[-1:]) >= 2:
        return f'роки'
    else:
        return f'років'


def validate_input():
    """
    Function which checks inserted age number by user, so it is digit and more than 0. Top age limit is not restricted.
    No long-livers hating :)

    Returns:
        age_check(int): verified age, corresponding to requirements

    """
    while True:
        age_check = input("Please, insert your age: ")
        if age_check.isdigit() and int(age_check) > 0:
            return int(age_check)
        else:
            print("Age should be a number bigger than zero!")


calc_user_response()
