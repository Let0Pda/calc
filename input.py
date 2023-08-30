import model

in_a = input('Введите число А = ')
in_b = input('Введите число Б = ')
oper = input('Введи знак операции(*/-+) = ')

def inp_operans():
    if 'i' in in_a and 'i' in in_b:
        model.init(a, b, True)

    elif '/' in in_a and '/' in in_b:
        model.init(a, b, False)
    else:
        return False
    return True


def calc(oper):
    if '*' in oper:
        result = model.mult()
        
    elif '+' in oper:
        result = model.sum()

    elif '-' in oper:
        result = model.sub()

    elif '/' in oper:
        result = model.div()

    else:
        print('оператор не верный')
    return result

def log(data):
    with open('log.txt', 'w') as file:
        file.write(data)


def view(data):
    print(data)


def run():
    result = calc(oper) if inp_operans() else False
    log(result)
    view(result)


