# task1 Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
# Якщо перетворити не вдається функція має повернути 0.

def type_to_float(to_convert):
    try:
        return float(to_convert)
    except:
        return float(0)


res = type_to_float(False)
res1 = res + 1
print(res1)