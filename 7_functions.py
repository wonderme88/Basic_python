def hello_func():
    return 'Hello Function'

""" print(hello_func())
def hello_dear(greeting):
    return '{} Function'.format(greeting)

print(hello_dear('Namaste')) """

def hello_hi(greeting):
    return '{} Function'.format(greeting)

print(hello_hi('Hello'))


def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Science',name='John',age=22)


