import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def nextPos(x, y, roomType, arriving):
    '''
    Determine what is the next position considering the current room and from where Indy comes (TOP, LEFT, RIGHT)
    '''
    if(roomType in ['2', '6']):
        if arriving == 'LEFT':
            x += 1
        elif arriving == 'RIGHT':
            x -= 1
    elif(roomType in ['1', '3', '7', '8', '9', '12', '13']):
        y += 1
    elif(roomType == '10'):
        x -= 1
    elif(roomType == '11'):
        x += 1
    elif(roomType == '4'):
        if(arriving == 'TOP'):
            x -= 1
        elif(arriving == 'RIGHT'):
            y += 1
    elif(roomType == '5'):
        if(arriving == 'TOP'):
            x += 1
        elif(arriving == 'LEFT'):
            y += 1

    return (x,y)





 # w: number of columns.
 # h: number of rows.
w, h = [int(i) for i in raw_input().split()]
map = []
for i in xrange(h):
    line = raw_input() # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    map.append(line.split(' '))
ex = int(raw_input()) # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while 1:
    xi, yi, pos = raw_input().split()
    xi = int(xi)
    yi = int(yi)

    x, y = nextPos(xi, yi, map[yi][xi], pos)

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print (str(x) + ' ' + str(y))