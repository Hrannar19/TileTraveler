x = 1
y = 1

gameover = False

def location(x,y):
    if x == 1:
        if y ==1:
            print("You can travel: (N)orth")
    if x == 1:
        if y ==2:
            print("You can travel: (N)orth or (E)ast or (S)outh")
    if x == 1:
        if y ==3:
            print("You can travel: (E)ast or (S)outh")
    if x == 2:
        if y == 1:
            print("You can travel: (N)orth")
    if x == 2:
        if y == 2:
            print("You can travel: (W)est or (S)outh")
    if x == 2:
        if y == 2:
            print("You can travel: (E)ast or (W)est")
    if x == 3:
        if y == 3:
            print("You can travel: (W)est or (S)outh")
    if x == 3:
        if y == 2:
            print("You can travel: (N)orth or (S)outh")
    if x == 3:
        if y == 1:
            print("Victory!")
def play_move(input,x,y):
    if input == "N" or input == "n":
        x +=1
    if input  == "S" or input  == "s":
        x -=1
    if input  == "E" or input  == "e":
        y -=1
    if input  == "W" or input  == "w":
        y +=1
    


location(x,y)

move = play_move(input("Direction: "), x, y)