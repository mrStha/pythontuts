import sys
"""
user1 = input("input your name please")
user2 = input("input your name please")

print ("hello %s and %s" %(user1, user2))
choice1 = input("%s, choose one: rock paper scissors" % user1)
choice2 =input ("%s, choose one:rock paper scissors" % user2)
"""


user1 =raw_input("What's your name?")
user2 = raw_input("And your name?")
choice1 = raw_input("%s, do yo want to choose rock, paper or scissors?" % user1)
choice2 = raw_input("%s, do you want to choose rock, paper or scissors?" % user2)

if((choice1=="rock" and choice2=="scissors") or (choice1=="scissors" and choice2=="paper") or (choice1=="paper" and choice2=="rock")):
    print("%s is winner" %user1) 
elif(choice1==choice2):
    print("Sorry its a tie")
else: 
    print("\n%s is winner" %user2)