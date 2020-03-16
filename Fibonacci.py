def fibonacci(n):
    if n == 0:

        print("0")

    elif n >= 1:

        first = 0
        second = 1
        third = first + second

        print(first)

        print(second)

        while n > third:
            third = first + second
            first = second
            second = third

            print(second)
    else:

        print("Error...Number must be a non-negative number.")



def ejecucionFuncion():

    n = int(input("Introduce a non-negative number: "))

    fibonacci(n)


ejecucionFuncion()
