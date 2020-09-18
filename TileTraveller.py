N = '(N)orth'
S = '(S)outh'
E = '(E)ast'
W = '(W)est'

x_pos, y_pos = 1,1
acceptable_moves = ('')
direction = ''


def moving(x_pos: int, y_pos: int, direction: str)->int :
    if direction.lower() == 'n':
        return x_pos, y_pos + 1
    elif direction.lower() == 's':
        return x_pos, y_pos - 1
    elif direction.lower() == 'e':
        return x_pos + 1, y_pos
    elif direction.lower() == 'w':
        return x_pos - 1, y_pos
      
direction = str(input("Direction: ")) 
if direction.lower() in acceptable_moves:
    x_pos, y_pos = moving(x_pos, y_pos, direction) 
else:
    print ('Not a valid direction')