import turtle,math

#~ bob=turtle.Turtle()
#~ #tell the turtle what to do
#~ bob.forward(100)
#~ bob.left(90)
#~ bob.forward(100)
#~ bob.left(90)
#~ bob.forward(100)
#~ bob.left(90)
#~ bob.forward(100)

#~ screen=bob.getscreen()
#~ screen.mainloop()

#functions/methods
#math function
#  f(x)->y
#  input ->box-> output
#methods
# input ->box 


def printHellos(name,name2):
    """
    Prints hello to two people.
    
    Variables:
    name - first person's name
    name2 - secon person's name
    """
    print("hello "+str(name))
    print("hello "+str(name2))


def sqrt(n):
    if n<0:
        raise ValueError("the value must be non-negative")
    print(math.sqrt(n))

name=input("what is your name? ")
printHellos(name,7)
sqrt(-10)
#this line




