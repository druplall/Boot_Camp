# How to define functions
## def name_of_function():
## Docsting explain function.
## print('Hello')
### Call function by name, example name_of_function

def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input..
    OUTPUT: Hello..
    :return:
    '''
    print('Hello')

name_function()

# Find out of the word dog is in a string ?
def dog_check(mystring):
    return 'dog' in mystring.lower()

print(dog_check('MY DOG is great !'))