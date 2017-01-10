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

    # print out the results
    # prompt user to quit or generate another sequence
