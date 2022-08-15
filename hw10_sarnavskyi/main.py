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

keyword_args = {}
result = {}


def check_absence_password(*args, **kwargs):
    keyword_args.update(kwargs)
    count = False
    for key in keyword_args.keys():
        if key == 'password':
            count = True
    return count


def is_valid_length(string, length=10):
    count = False
    if len(string) >= length:
        count = True
    return count


def is_string(string):
    count = False
    if isinstance(string, str):
        count = True
    return count


def has_any_symbols(string, method):
    count = False
    if method == 'letters_check':
        for char in string:
            if char.isalpha():
                count = True
        return count
    elif method == 'contains_number':
        for char in string:
            if char.isdigit():
                count = True
        return count
    elif method == 'contains_exclamation_mark':
        for char in string:
            if char == '!':
                count = True
        return count
    return count


def cut_result(to_check, *args, **kwargs):
    func_res = str(to_check(*args, **kwargs))
    if len(func_res) > 100:
        return func_res[slice(97)] + '...'
    else:
        return func_res


def wrap_validate(func):

    def checker(*args, **kwargs):
        if check_absence_password(*args, **kwargs):
            pass
        else:
            raise AttributeError(f'no parameter "password" in arguments of function{func.__name__}')
        if is_string(keyword_args['password']):
            pass
        else:
            result.update({'result': cut_result(func, *args, **kwargs), 'is_secure': False})
            return result
        if is_valid_length(keyword_args['password'], 10):
            pass
        else:
            result.update({'result': cut_result(func, *args, **kwargs), 'is_secure': False})
            return result
        if has_any_symbols(keyword_args['password'], 'letters_check'):
            pass
        else:
            result.update({'result': cut_result(func, *args, **kwargs), 'is_secure': False})
            return result
        if has_any_symbols(keyword_args['password'], 'contains_number'):
            pass
        else:
            result.update({'result': cut_result(func, *args, **kwargs), 'is_secure': False})
            return result
        if has_any_symbols(keyword_args['password'], 'contains_exclamation_mark'):
            pass
        else:
            result.update({'result': cut_result(func, *args, **kwargs), 'is_secure': False})
            return result
        result.update({'result': cut_result(func, *args, **kwargs), 'is_secure': True})
        return result

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

print(registration(12, password=None))

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
    assert check_absence_password(password=None, username='gus')
    assert check_absence_password(password='qweqweqwe1!')
    assert check_absence_password(password=12)

    assert not is_valid_length('1234', 5)
    assert not is_valid_length('1234')
    assert is_valid_length('1234', 4)

    assert not is_string(1)
    assert not is_string({1: 2})
    assert is_string('string')

    assert not has_any_symbols('1!', 'letters_check')
    assert not has_any_symbols('s!', 'contains_number')
    assert not has_any_symbols('1s', 'contains_exclamation_mark')
    assert has_any_symbols('s', 'letters_check')

    assert cut_result(lambda x: 'a' * 101, 1) == 'a' * 97 + '...'
    assert cut_result(lambda x: 'a' * 100, 1) == 'a' * 100
    assert cut_result(lambda x: 'a' * 50, 1) == 'a' * 50

    assert registration(12, 'fff', 'nnn', password='asdasdasd1!') == \
           {'result': 'User fff created account on 2022-08-15 with password "asdasdasd1!". '
                      'Additional information: nnn', 'is_secure': True}
    assert type(registration(12, 'fff', 'nnn', password='')) == dict
    assert registration(12, 'fff', 'nnn', password='asdasdasd1')
    assert registration(12, password=None)['is_secure'] is False
    assert registration(12, 'fff', 'nnn', password='a')['is_secure'] is False
    assert registration(12, 'fff', 'nnn', password='aaaaaaaaaa1')['is_secure'] is False
    assert registration(12, 'fff', 'nnn', password='aaaaaaaaaa!')['is_secure'] is False
    assert registration(12, 'fff', 'nnn', password='aaaaaaa1!')['is_secure'] is False
    assert registration(12, 'fff', 'nnn', password='aaaaaaaaaa1!')['is_secure'] is True




##############################################################################
############                                                     #############
############                      TASK 4                         #############
############                     HAVE FUN                        #############
############                                                     #############
##############################################################################
