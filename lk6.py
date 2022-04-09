def decor(func):
    def wrap(*args, reverse = True):
        print("Args: " + str(args))
        print("Kwargs: {reverse: "+str(reverse)+"}")
        func()
    return wrap

decor
def concat(*args, reverse = False):
    string = ''
    if(reverse):
        for i in args[::-1]:
            string+=i
    else:
        for i in args:
            string+=i
    print(string)


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
print(fibonacci(10))

concat("hello", " ","world.", reverse = True)