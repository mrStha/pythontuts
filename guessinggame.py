import random


def guess():
    randomnum =  random.randint(0,9)
    count = 0
    tryagain = 1

    while(tryagain!="exit"):
        print(" the random num is %d " %randomnum)
        user1 = int(raw_input(" guess a number between 1-9\t"))  
       
        count+=1

        if(user1==randomnum):
                print " you got it correct in %d trials " % count
        elif(user1<randomnum):
               print(" number entered is too low \n ")
        elif(user1>randomnum):
            print(" number entered is too high \n")

                
            #would you like to guess again? Press Y to continue or exit to end")
                
                
                
    guess();


#return guess(tryagain)
 #return tryagain       
        
        