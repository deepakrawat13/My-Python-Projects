import random
print("Welcome to snake water gun game\n"
      "It's a game of 5 rounds")
list = ["s", "w", "g"]
i=0
comp = 0
play = 0
while (i < 5) :
    i = i+1
    inp = input('Enter s for snake,w for water or g for gun :')
    c = random.choice(list)
    if inp == c:
        print ("it's a tie")
    elif inp == "s" and c == "w":
        print("you have won this round")
        play = play +1
    elif inp == "s" and c == "g":
        print("you have lost this round")
        comp = comp +1
    elif inp == "w" and c == "g":
        print("you have won this round")
        play = play +1
    elif inp == "w" and c == "s":
        print("you have lost this round")
        comp = comp +1
    elif inp == "g" and c == "s":       
        print("you have won this round")
        play = play +1
    elif inp == "g" and c == "w":
        print("you have lost this round")
        comp= comp +1
    else:
        print("error or invalid input")

if play > comp:
    print("CONGRATS you have won")
elif play < comp:
    print("OOPS you have lost")
else:
    print("It's a draw")
print("you have won", play ,"times")
print("computer has won", comp, "times")
