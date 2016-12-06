from random import randint

global pointOn,point
comeOnBet = 0
playerBank = 1000
playing = 'Y'

#roll while point is set
def rollwhilepoint():
    global pointOn,point,comeOnBet,playerBank

    while pointOn:
        v=roll()
        if v == point:
            print "You win!"
            playerBank += (comeOnBet*2)
            print "Your balance is",playerBank
            pointOn = False
        elif v == 7:
            print "You lose! \n Your balance is",playerBank
            pointOn = False



#initial roll
def roll():
    raw_input("Press any key to roll")
    #roll dice
    d1=randint(1,6)
    d2=randint(1,6)
    v=d1+d2
    print "You rolled a " , v
    return v

def gameplay():
    global pointOn, point, playerBank, playing, comeOnBet
    pointOn=False
    point=0

    playing = raw_input("Are you ready? Type Y to make a bet and play some Craps" )

    while playing == 'Y':
        while playerBank > 0:
            print "\nLet's play! You have",playerBank,"to bet with!"
            comeOnBet = int(raw_input("How much is your come on bet?" ))
            while comeOnBet < 1:
                comeOnBet = int(raw_input("How much is your come on bet?" ))
            playerBank -= comeOnBet
            v = roll()
            if v == 7 or v == 11:
                print "You won on the come out!"
                playerBank += (comeOnBet*2)

            elif v == 2 or v == 3 or v == 12:
                print "You lost on the come out!"

            else:
                print "The point is set to", v
                point = v
                pointOn = True
                rollwhilepoint();
        print "You have overleveraged and you are poor now... Goodbye"
        playing = 'N'

#
#
# while playing == 'Y':
gameplay();

print "Thanks for playing!"
