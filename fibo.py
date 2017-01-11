import sys


def _quit():
    sys.exit(1)


def checkLength(n):
    """Due to implementation of recursion checking the fibonacci sequence
    total of a number greater than 998 throws a RecursionError
    """
    try:
        fiboTotal(fibo(n))
    except RecursionError:
        print("Value should be a number less than 999 (not inclusive)")
        return True


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
              " to that number: ")
    return n


def fiboTotal(sequence):
    """This function returns a total of the digits in the sequence
    """
    if sequence == []:
        return 0
    elif len(sequence) == 2:
        return sequence[0] + sequence[1]
    else:
        return sequence.pop() + fiboTotal(sequence)


def fibo(n=None):
    # this allows for test fibo(0) to run correctly
    if n == 0:
        sequence = []
        return sequence
    # prompt user for input
    n = n or getInput()

    # confirm that the number is an interger and not string or float
    if checkString(n):
        n = getInput()

    # if float, round float input to nearest 10
    if checkFloat(n):
        n = roundFloat(n)

    # convert n to int
    n = int(n)

    # generate fibonacci sequence to the nth number
    count = 2  # This is 2 because the sequence has 2 predefined values [0, 1]
    if n == 0:
        sequence = []
        return sequence
    elif n == 1:
        sequence = [0]
        return sequence
    else:
        sequence = [0, 1]
        value = 0
        while count < n:
            value = sequence[len(sequence) - 2] + sequence[len(sequence) - 1]
            count += 1
            sequence.append(value)
        return sequence

if __name__ == "__main__":
    # print out the results
    n = getInput()
    print(fibo(n))

    if checkLength(n):
        checkLength(n)
    else:
        print("The total of the fibonacci sequence to {} is: {}"
              .format(n, fiboTotal(fibo(n))))
