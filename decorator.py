def new_tips(arg):
    def tips(func):
        def f(a, b):
            print('start {}'.format(arg))
            func(a, b)
            print('stop {}'.format(arg))
        return f
    return tips


@new_tips('add')
def add(a, b):
    print(a + b)


@new_tips('sub')
def sub(a, b):
    print(a - b)


add(3, 4)
sub(3, 2)
