l1=1
l2=1
r1=1
r2=1
print("\nCurrent Status:")
print("Player1- ",l1," ",r1)
print("Player2- ",l2," ",r2,"\n")

#START OF TURN FOR PLAYER 1
while(True):
    move=input("Enter move for player1 - ")
#ATTACK
    if move=="A":
        f,t=input("Enter the move combination - ").split(" ")
        if f=="L" and t=="L":
            l2 = l1 + l2
            if l2>=5:
               l2=0
        elif f=="L" and t=="R":
            r2 = l1+ r2
            if r2>=5:
              r2=0
        elif f=="R" and t=="L":
            l2 = l2 + r1
            if l2>=5:
              l2=0
        elif f=="R" and t=="R":
            r2= r2 + r1
            if r2>=5:
              r2=0
        else:
            print("Invalid input")
    elif move=="S":
#SPLIT
        h,a,b=input("Enter the move combination: ").split(" ")
        a=int(a)
        b=int(b)
        l1=a
        r1=b
    else:
       print("Invalid input")
#STATUS
    print("Current Status:")
    print("Player1- ",l1," ",r1)
    print("Player2- ",l2," ",r2,"\n")
    if l2==0 and r2==0:
       print("Player 1 wins!")
       break
#TURN START FOR PLAYER2
    move=input("Enter move for player2 - ")
#attack
    if move=="A":
        f,t=input("Enter the move combination - ").split(" ")
        if f=="L" and t=="L":
            l1 = l2 + l1
            if l2>=5:
                l2=0
        elif f=="L" and t=="R":
            r1 = l2 + r1
            if r1>=5:
                r1=0
        elif f=="R" and t=="L":
            l1 = l1 + r2
            if l1>=5:
               l1=0
        elif f=="R" and t=="R":
            r1 = r1 + r2
            if r1>=5:
              r1=0
        else:
            print("Invalid input")
    elif move=="S":
#SPLIT
        h,a,b=input("Enter the move combination: ").split(" ")
        a=int(a)
        b=int(b)
        l2=a
        r2=b
    else:
        print("Invalid input")
#stAus
    print("Current Status:")
    print("Player1- ",l1," ",r1)
    print("Player2- ",l2," ",r2,"\n")
    if l1==0 and r1==0:
       print("Player 2 wins!")
       break



        





    




