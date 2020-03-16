def foobar(n):


    for i in range (0,n+1):

        position = ""

        if (i%3==0) and (i%5==0):

            print("Foobar")

        elif (i%3==0) and (i%5!=0):

            print("Foo")

        elif (i%3!=0) and (i%5==0):

            print("Bar")

        else:

            print(i)



def createFoobar():

    n = int(input ("Introduce n numbers to analize: "))

    foobar(n)

createFoobar()