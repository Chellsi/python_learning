# task1
# завантажити використовуючи requests структуру даних з
# https://dummyjson.com/todos
# та вивести на екран не виконані значення todo з тих даних, які до вас прийшли

import requests
url = 'https://dummyjson.com/todos'
todo_request = requests.get(url)
todos = todo_request.json()

uncompleted_todos_list = []
todos_counter = 0

for todo in todos['todos']:
    if not todos['todos'][todos_counter]['completed']:
        uncompleted_todos_list.append(todos['todos'][todos_counter]['todo'])
    todos_counter += 1

uncompleted_todos_string = '\n- '.join(uncompleted_todos_list)
print(f'Next todos are not completed:\n- {uncompleted_todos_string}')
