class Error(Exception):
    '''Base class for other exceptions'''
    pass
class ValueTooSmallError(Error):
    '''Raised when the input is very too small'''
    pass
class ValueTooLargeError(Error):
    '''Raised when the input is very too large'''
    pass
#you need to guess this number
number = 10
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value small, try again!")
    except ValueTooLargeError:
        print("This value is too large, try again!")
print("Congratulations! You guessed it correctly.")