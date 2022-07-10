# task1
# Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

while True:
    # дозволив вводити будь що, крім порожньої строки
    checked_string = input("Please, input your string and press 'Enter'")
    if checked_string:
        break
    else:
        print("Your string shouldn`t be empty!")

while True:
    # спростив ввід індексу для юзера, не знайомого с програмуванням і зробів відлік символів не з 0, а з 1
    user_index = input("Input index of symbol you want to search for (count starts from '1')")
    if user_index.isdigit() and 1 <= int(user_index) <= len(checked_string):
        break
    else:
        print("Please, input number from 1 to maximum symbols in yor string!")

character_index = int(user_index) - 1
search_symbol = checked_string[character_index]

result_str = f"The {user_index} symbol in '{checked_string}' is '{search_symbol}'"
print(result_str)


# task2
# Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.

while True:
    # дозволив вводити будь що, крім порожньої строки або строки лише с пробілами
    user_string = input("Please, input your string and press 'Enter'")
    if user_string.split():
        break
    else:
        print("Your string shouldn`t be empty!")

user_list = user_string.split()
words_counter = f"There is(are) {len(user_list)} word(s) in your string"
print(words_counter)

# task3
# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for val in lst1:
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        lst2.append(val)
