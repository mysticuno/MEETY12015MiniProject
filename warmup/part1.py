import turtle as t

t.penup() #move pen without writing
t.ht()

COUNTDOWN = 10

def say_hi():
    t.ontimer(print("Hi MEET student!"),1000)
    t.ontimer(say_bye,3000)

def say_bye():
    print("Bye MEET student!")

def countdown():
    '''
    Prints a countdown from 10.
    '''
    global COUNTDOWN
    while COUNTDOWN >= 0:
        print(COUNTDOWN)
        COUNTDOWN -= 1

t.ontimer(say_hi,3000) #don't remove this line
t.mainloop()
