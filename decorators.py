def addition(func):
    def dummy(*args):
        s = 0
        for num in args:
            s += num
        return func('Addition',s)

    return dummy


def multiplication(func):
    def dummy(*args):
        s = 1
        for num in args:
            s *= num
        return func('Multiplication', s)

    return dummy



    
