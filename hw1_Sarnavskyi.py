#hw1

# Task 1
# Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

print(first + second)
print(first - second)
print(first * second)
print(first / second)
print(first % second)
print(first ** second)


# Task 2
# Створіть змінну і запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.

is_lesser = first < second
is_bigger = first > second
is_equal = first == second
is_not_equal = first != second

print(is_lesser)
print(is_bigger)
print(is_equal)
print(is_not_equal)

# Task 3
# Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world". Виведіть на екран.

str1 = "Hello "
str2 = "world"

greetings_str = str1 + str2

print(greetings_str)