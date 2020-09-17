

x = 1
y = 1

board_size = 3

gameover = False


def is_valid_move(x, y):
    if x < 1 or x > board_size:
        return False
    if y < 1 or y > board_size:
        return False
    return True

def show_available_directions(x, y):

    directions = ""

    # North
    if is_valid_move(x+1, y):
        if directions != "":
            directions += " or "
        directions += "(N)orth"

    # East
    if is_valid_move(x, y+1):
        if directions != "":
            directions += " or "
        directions += "(E)ast"

    # South
    if is_valid_move(x-1, y):
        if directions != "":
            directions += " or "
        directions += "(S)outh"

    # West
    if is_valid_move(x, y-1):
        if directions != "":
            directions += " or "
        directions += "(W)est"

    directions += "."

    print(directions)

def check_input(input, x, y):
    if input == 'n' or input == 'N':
        y += 1
    if input == 'e' or input == 'E':
        x += 1
    if input == 's' or input == 'S':
        y -= 1
    if input == 'w' or input == 'W':
        x -= 1

    if is_valid_move(x, y):
        return [x, y]
    return False

while not gameover:

    	
    show_available_directions(x, y)

    not_valid_input = True


    while not_valid_input:
        move = check_input(input("Direction: "), x, y)


        if move:
            not_valid_input = False
            x = move[0]
            y = move[1]
        else:
            print("Not a valid direction!")


    if x == 3 and y == 1:
        gameover = True
        print("Victory!") 
