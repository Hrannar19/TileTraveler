x = 1
y = 1

gameover = False

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

def play_move(input): # skoðað hvaða átt má fara í

    x = 0
    y = 0
    
    if input == 'n' or input == 'N':
        y += 1
    elif input == 'e' or input == 'E':
        x += 1
    elif input == 's' or input == 'S':
        y -= 1
    elif input == 'w' or input == 'W':
        x -= 1
    else:
        return False
    return [x, y]

while not gameover:

    if(x == 3 and y == 1):
        gameover = True
        print("Victory!")
        break

    valid_input = show_available_directions(x, y) # sýnt hvert má fara
    input_is_valid = False # skoðað hvort input sé valid

    while not input_is_valid:
        move = play_move(input("Direction: "))
        if move[0] >= valid_input[0] and move[0] <= valid_input[1] and move[1] >= valid_input[2] and move[1] <= valid_input[3]:
            x += move[0]
            y += move[1]
            input_is_valid = True
        else:
            print("Not a valid direction!") # skilgreint hvað skal gerast ef það er keyrt utan í vegg
            show_available_directions(x, y)

    

# https://github.com/Hrannar19/TileTraveler