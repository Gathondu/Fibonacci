def roundFloat(n):
    return round(n)


def checkFloat(n):
    if isinstance(n, float):
        return True


def checkString(n):
    try:
        int(n)
    except ValueError:
        print("Value must be a number and not a string or character")
        return True


def getInput(n=None):
    n = input("Enter a number to generate the fibonacci sequence"
              "to that number: ")

    return n


def fibo(n=None):
    # prompt user for input
    n = n or getInput()

    # confirm that the number is an interger and not string or float
    if checkString(n):
        n = getInput()

    # if float, round float input to nearest 10
    if checkFloat():
        n = roundFloat(n)

    # generate fibonacci sequence to the nth number
    # print out the results
    # prompt user to quit or generate another sequence
