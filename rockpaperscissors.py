import sys



def game(play_again):
       
        if(play_again==True):
            user1 =raw_input("What's your name?\t")
            user2 = raw_input("And your name?\t")
            choice1 = raw_input("%s, do yo want to choose rock, paper or scissors?\t" % user1)
            choice2 = raw_input("%s, do you want to choose rock, paper or scissors?\t" % user2)

            if((choice1=="rock" and choice2=="scissors") or (choice1=="scissors" and choice2=="paper") or (choice1=="paper" and choice2=="rock")):
                print("\nCongratulations! %s is winner\n" %user1) 
                moregame()
            elif(choice1==choice2):
                print("\nSorry its a tie\n")
                moregame()
            elif((choice2=="rock" and choice1=="scissors") or (choice2=="scissors" and choice1=="paper") or (choice2=="paper" and choice1=="rock")): 
                print("\nCongratulations %s is winner\n" %user2)
                moregame()
            else:
                print(" choice could not be identified\n")
                moregame()
            

def moregame():            
        play = raw_input(" Continue again (Y/N)? ")
        if(play=="Y" or play =="yes" or play =="y"): 
            play_again = True
            game(play_again);

        else: 
            play_again = False            
            game(play_again)

game(True);