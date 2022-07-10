# Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

checked_string = str(input("Please, input your string and hit 'Enter'"))
user_index = int(input("Input index of symbol you want to search for (count starts from '1')"))
character_index = user_index - 1

search_symbol = checked_string[character_index]

result_str = f"The {user_index} symbol in '{checked_string}' is '{search_symbol}'"

print(result_str)