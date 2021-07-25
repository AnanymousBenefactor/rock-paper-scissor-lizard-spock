import random
def RPSLS(c,u):
      pp=pc=0
      if c==u:
            print("no one wins it's a tie")
      if c!=u:
            if u==1 and c==2:
                  print("paper covers rock!!")
                  print("computer wins!!")
            if u==1 and c==3:
                  print("rock crushes scissor!!")
                  print("player wins!!")
            if u==1 and c==4:
                  print("rock crushes lizard!!")
                  print("player wins!!")
            if u==1 and c==5:
                  print("spock vapourizes rock!!")
                  print("computer wins!!")
            if c==1 and u==2:
                  print("paper covers rock!!")
                  print("player wins!!")
            if c==1 and u==3:
                  print("rock crushes scissor!!")
                  print("computer wins!!")
            if c==1 and u==4:
                  print("rock crushes lizard!!")
                  print("computer wins!!")
            if c==1 and u==5:
                  print("spock vapourizes rock!!")
                  print("player wins!!")
            if u==2:
                  if c==3:
                        print("scissor cuts paper!!")
                        print("computer wins!!")
                  if c==4:
                        print("lizard eats paper!!")
                        print("computer wins!!")
                  if c==5:
                        print("paper disproves spock!!")
                        print("player wins!!")
            if c==2:
                  if u==3:
                        print("scissor cuts paper!!")
                        print("player wins!!")
                  if u==4:
                        print("lizard eats paper!!")
                        print("player wins!!")
                  if u==5:
                        print("paper disproves spock!!")
                        print("computer wins!!")
            if u==3:
                  if c==4:
                        print("scissor decapitates lizard!!")
                        print("player wins!!")
                  if c==5:
                        print("spock smashes sicssor!!")
                        print("computer wins!!")
            if c==3:
                  if u==4:
                        print("scissor decapitates lizard!!")
                        print("computer wins!!")
                  if u==5:
                        print("spock smashes sicssor!!")
                        print("player wins!!")
            if u==4:
                  if c==5:
                        print("lizard poisons spock!!")
                        print("player wins!!")
            if c==4:
                  if u==5:
                        print("lizard poisons spock!!")

                        print("computer wins!!")
            
#_main_
print("""Welcome to the rock paper scissor lizard spock game!!
1 corresponds to rock
2 corresponds to paper
3 corresponds to scissor
4 corresponds to lizard
5 corresponds to spock
**************************
instructions:
rock wins over scissor and lizard
scissor wins over paper and lizard
paper wins over rock and spock
lizard wins over paper and spock
spock wins over rock and scissors""")

while True:
      ch=int(input("enter 1/2/3/4/5:"))
      cch=random.randint(1,5)
      RPSLS(cch,ch)
      if ch not in [1,2,3,4,5]:
            print("game over")
      break





      
