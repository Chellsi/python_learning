# task1
# Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

def type_to_float(to_convert):
    """
    Function to convert data into float type if it is possible. If not - returns 0.

    Args:
        to_convert (any type): data to convert into float

    Returns:
        float: to_convert argument converted into float
        0 (int): if to_convert type doesn't allow to convert it into float

    """
    try:
        return float(to_convert)
    except:
        return 0


# task2
# Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# у будь-якому іншому випадку повернути кортеж з цих аргументів

def data_mixer(x, y):
    """
    Function to mix data provided by arguments and return them as combined.

    Args:
        x (any type): first argument, type will influence on what will be returned
        y (any type): second argument, type will influence on what will be returned

    Returns:
        (int, float): multiplication of x and y in case if both x and y are type of int or float
        (str): sum of x and y in case if both x and y are strings
        (dict): dictionary where x becomes key and y becomes value, in case if x is string and y is not
        (tuple): tuple where x becomes first item and y becomes second one,
                in case of any other types combinations of x and y

    """
    if type(x) in (int, float) and type(y) in (int, float):
        return x * y
    elif type(x) == str and type(y) == str:
        return x + y
    elif type(x) == str and type(y) != str:
        return {x: y}
    else:
        return tuple([x, y])

