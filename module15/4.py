# Custom Exception

# to create custom exception, i need to use inheritence
# my custom exception should be a child of RuntimeError class


class EmptyException(RuntimeError) :
    def __init__(self, arguments):
        self.arguments = arguments

var = ''

try :
    if var == '':
        raise EmptyException('This variable is a empty string')
except EmptyException as e:
    print(e.arguments)


