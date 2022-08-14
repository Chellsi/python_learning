"критерієм перевірки буде проходження всіх ассертів"

##############################################################################
############                                                     #############
############                      TASK 1                         #############
############                                                     #############
##############################################################################
"""
написати декоратор wrap_validate, який не приймає жодних параметрів
його задача - перевірити, що функція, яку він задекорував, обовязково отримала
в своїх аргументах параметр 'password' (згадуємо про * в написанні аргументів функції)
значення 'password' повинне бути стрічкою, довжиною не менше 10 символів,
та містити в собі латинські літери (регістр не принципово), арабські цифри та знак '!"

кожну з перевірок отриманого значення паролю виконуємо в ОКРЕМІЙ функції, функції робимо
універсальними, називаємо їх (з опційними параметрами)
- is_valid_length(length=10)
- has_any_symbols(symbols='qwertyuiopasdfghjklzxcvbnm') (це приклад для латинських букв, повертає тру, якщо хоч
один символ в стрічці, аналогічно зробити для цифр та знаку оклику (у вас буде 3 виклики функції в середині декоратора
з різними параметрами)
- is_string()

якщо  'password'  відсутній - викликаємо помилку
raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')

якщо  'password'  не задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': False,
}

якщо  'password'  задовольняє вимогам валідації, написаним вище, то повертається словник виду
{ 'result': str(func(*args, **kwargs)),
  'is_secure': True,
}

зауважте, що str(func(*args, **kwargs)) МАЄ бути довжиною не більше 100 символів
якщо даний результат буде довшим за 100 символів, то стрічка має бути обрізана до 100 символів, причому останні
три символи мають бути ... (трьома крапками)
тут ви вже й самы здогадалися написати функцію на виконання даної роботи (тут вже без підказок)
"""


def wrap_validate(func):
    keyword_args = {}
    result = {}

    def cut_result(*args, **kwargs):
        func_res = str(func(*args, **kwargs))
        print(func_res)
        if len(func_res) > 100:
            return func_res[slice(98)] + '...'
        else:
            return func_res

    def checker(*args, **kwargs):
        if check_absence_password(*args, **kwargs):
            pass
        else:
            raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')
        if is_string():
            pass
        else:
            result.update({'result': cut_result(*args, **kwargs), 'is_secure': False})
            return result
        if is_valid_length(10):
            pass
        else:
            result.update({'result': cut_result(*args, **kwargs), 'is_secure': False})
            return result
        if has_any_symbols('letters_check'):
            pass
        else:
            result.update({'result': cut_result(*args, **kwargs), 'is_secure': False})
            return result
        if has_any_symbols('contains_number'):
            pass
        else:
            result.update({'result': cut_result(*args, **kwargs), 'is_secure': False})
            return result
        if has_any_symbols('contains_exclamation_mark'):
            pass
        else:
            result.update({'result': cut_result(*args, **kwargs), 'is_secure': False})
            return result
        result.update({'result': cut_result(*args, **kwargs), 'is_secure': True})
        return result

    def check_absence_password(*args, **kwargs):
        keyword_args.update(kwargs)
        count = False
        for key in keyword_args.keys():
            if key == 'password':
                count = True
        return count

    def is_valid_length(length=10):
        count = False
        if len(keyword_args['password']) >= length:
            count = True
        return count

    def is_string():
        count = False
        if isinstance(keyword_args['password'], str):
            count = True
        return count

    def has_any_symbols(method):
        count = False
        if method == 'letters_check':
            for char in keyword_args['password']:
                if char.isalpha():
                    count = True
            return count
        elif method == 'contains_number':
            for char in keyword_args['password']:
                if char.isdigit():
                    count = True
            return count
        elif method == 'contains_exclamation_mark':
            for char in keyword_args['password']:
                if char == '!':
                    count = True
            return count

    return checker


##############################################################################
############                                                     #############
############                      TASK 2                         #############
############                                                     #############
##############################################################################
"""
написати функцію registration, яка приймає
- позиційний аргумент id, стрічка або число - не важливо,  значення за замовчуванням - відсутнє
- позиційний або іменований аргумент login, тип даних - не важливий, значення за замовчуванням - відсутнє
- позиційний або іменований аргумент notes, тип даних - не важливий, значення за замовчуванням - відсутнє
- password - тип даних - не важливий, значення за замовчуванням - відсутнє

в середині функції вставити код (зназок для отримання даних прописаний нижче)
date = datetime.date.today()

результат робити функції - стрічка
f'User {login} created account on {date} with password "{password}". Additional information: {notes}'

задекоруйте написаним в завданні 1 декоратором
"""

import datetime


@wrap_validate
def registration(id, /, login=None, notes=None, *, password=None):
    date = datetime.date.today()
    return str(f'User {login} created account on {date} with password "{password}". Additional information: {notes}')




##############################################################################
############                                                     #############
############                      TASK 3                         #############
############                                                     #############
##############################################################################
"""
створіть умову if name == main (тут ціленаправлено написано не вірно, як вірно - ви знаєте)
в цій умові створіть assert на всі створені функції (окрім декоратора), викликайте функції з різними параметрами 
(довжина слів, різні текстовки....)
на кожну функцію, що використовується в декораторі, має бути мінімум 3 ассерта,

функцію registration перевіряйте з огляду на роботу декоратора (ключі, значення). обовязково перевірте кількість ключів, 
тип даних в значеннях, назви ключів, значення отриманого результату в залежності від переданих даних   

ВАЖЛИВО 
функцію registration ассертимо ТІЛЬКИ при передачі їй валідних даних (поля паролю)
"""

if __name__ == '__main__':
    assert type(registration(3434, 'Comp', notes='notes', password='wasdwasd9!')) == dict, 'not a string'
    assert type(registration(3434, 'Comp', notes='notes', password='wasdwasd9')) == dict, 'not a dict'


##############################################################################
############                                                     #############
############                      TASK 4                         #############
############                     HAVE FUN                        #############
############                                                     #############
##############################################################################
