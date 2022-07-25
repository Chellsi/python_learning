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


def cinema_cashier(checked_age, formatted_age_string):
    if checked_age < 7:
        print(f"Тобі ж {formatted_age_string}! Де твої батьки?")
    elif checked_age < 16:
        print(f'Тобі лише {formatted_age_string}, а це фільм для дорослих!')
    elif checked_age > 65:
        print(f'Вам {formatted_age_string}? Покажіть пенсійне посвідчення!')
    elif str(checked_age)[0] == str(checked_age)[1]:
        print(f'О, вам {formatted_age_string}! Який цікавий вік!')
    else:
        print(f'Незважаючи на те, що вам {formatted_age_string}, білетів всеодно нема!')


def age_string_create(age_tostring):
    if 20 > int(str(age_tostring)[-2:]) > 10:
        return f'{age_tostring} років'
    elif str(age_tostring).endswith('1'):
        return f'{age_tostring} рік'
    elif 4 >= int(str(age_tostring)[-1:]) >= 2:
        print(str(age_tostring)[-1:])
        return f'{age_tostring} роки'
    else:
        return f'{age_tostring} років'


def input_checker():
    while True:
        age_check = input("Please, insert your age: ")
        if age_check.isdigit() and int(age_check) > 0:
            return age_check
        else:
            print("Age should be a number bigger than zero!")


user_age = int(input_checker())
age_string = age_string_create(user_age)
cinema_cashier(user_age, age_string)
