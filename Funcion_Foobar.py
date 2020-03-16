def foobar(n):


    for i in range (0,n+1):

        position = ""

        if (i%3==0) and (i%5==0):

            position = "Foobar"

        elif (i%3==0) and (i%5!=0):

            position = "Foo"

        elif (i%3!=0) and (i%5==0):

            position = "Bar"

        else:

            position = i

        print (position)



def createFoobar():

    n = int(input ("Introduce n numbers to analize: "))

    foobar(n)

createFoobar()
