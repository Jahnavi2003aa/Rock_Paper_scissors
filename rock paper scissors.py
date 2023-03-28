import random
choices=('rock','paper','scissors')
n=int(input("Please enter the No.of choices u want"))
c=0
p=0
for i in range(n):
    player=input("enter any of your choice from {rock,paper,scissors}")
    
    if player in choices:
        computer=random.choice(choices)
        print('player:',player)
        print('computer:',computer)
        if player=='rock' and computer=='paper':
            print("computer won the game")
            c+=1
        elif player=='rock' and computer=='scissors':
            print("Player won the game")
            p+=1
        elif player=='paper' and computer=='rock':
            print("Player won the game")
            p+=1
        elif player=='paper' and computer=='scissors':
            print("computer won the game")
            c+=1
        elif player=='scissors' and computer=='rock':
            print("computer won the game")
            c+=1
        elif player=='scissors' and computer=='paper':
            print("player won the game")
            p+=1
        else:
            print("It was a tie!!")
    else:
        print("choose only from choices")
print("Thanks for Playing would you like to play one more!!")
if c>p:
    print("Oh NOOO!!!computer victory!!")
elif p>c:
    print("WOOHHH!!!Player victory")
else:
    print("Tie!!")



