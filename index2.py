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
def play_move(input):
    x = 0
    y = 0
    if input == "N" or input == "n":
        y +=1
    elif input  == "S" or input  == "s":
        y -=1
    elif input  == "E" or input  == "e":
        x +=1
    elif input  == "W" or input  == "w":
        x -=1
    else:
        return False
    return[x,y]
def show_available_directions(x, y): # skilgreiningar á mögulegum leikjum

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    north = False
    east = False
    south = False
    west = False

    if x == 1:
        if y == 1:
            north = True
        elif y == 2:
            north = True
            east = True
            south = True
        elif y == 3:
            east = True
            south = True
    elif x == 2:
        if y == 1:
            north = True
        elif y == 2:
            south = True
            west = True
        elif y == 3:
            east = True
            west = True
    elif x == 3:
        if y == 1:
            north = True
        elif y == 2:
            north = True
            south = True
        elif y == 3:
            south = True
            west = True

    directions = ""

    if north:
        max_y = 1
        directions += "(N)orth"
    if east:
        max_x = 1
        directions += "(E)ast"
    if south:
        min_y = -1
        directions += "(S)outh"
    if west:
        min_x = -1
        directions += "(W)est"

    print("You can travel: " + directions.replace("(", " or (")[4:] + ".")

    return [min_x, max_x, min_y, max_y]


while not gameover:

    if(x == 3 and y == 1):
        gameover = True
        print("Victory!")
        break

    valid_input = show_available_directions(x, y)
    input_is_valid = False

    while not input_is_valid:
        move = play_move(input("Direction: "))
        if move[0] >= valid_input[0] and move[0] <= valid_input[1] and move[1] >= valid_input[2] and move[1] <= valid_input[3]:
            x += move[0]
            y += move[1]
            input_is_valid = True
        else:
            print("Not a valid direction!")
            show_available_directions(x, y)
            
    #https://github.com/Hrannar19/TileTraveler
