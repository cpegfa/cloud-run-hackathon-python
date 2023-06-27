import json
import numpy as np



#config
data = 0            # json data
board_dims = None          # game board dimension in a tuple (row,column)
self = None                 # my position on the game board
prox = None


"""
Read Json and Prepare variables
"""
def get_game_state(infos, size=3):
    global self
    global prox
    global board_dims
    myurl = infos['_links']['self']['href']
    players = infos['arena']['state']
    board_dims = infos['arena']['dims']
    for key, info in players.items():
        if key == myurl:
            self={'x':info['x'],'y':info['y'],'direction':info['direction'],'wasHit':info['wasHit'],'score':info['score']}
            pos=[info['x'],info['y']]
            break

    prox=np.empty((0,5))
    for key, info in players.items():
        if abs(pos[0] - info['x']) <= size and  abs(pos[1] - info['y']) <= size and key != myurl :
            prox = np.append(prox, [[info['x'],info['y'],info['direction'],info['wasHit'],info['score']]], axis=0)



def highChanceHit():
    global prox
    global self
    for i in range(len(prox)):
        print("s",self)
        print("p:",prox[i][0],",",prox[i][1])
        if self['x'] == prox[i][0] and self['y'] < prox[i][1] and self['direction'] == 'N': return True
        if self['y'] == prox[i][1] and self['x'] > prox[i][0] and self['direction'] == 'W': return True
        if self['x'] == prox[i][0] and self['y'] > prox[i][1] and self['direction'] == 'S': return True
        if self['y'] == prox[i][1] and self['x'] < prox[i][0] and self['direction'] == 'E': return True

        match self['direction']:
            case 'N':
                if self['x'] - 1 == prox[i][0] and self['y'] > prox[i][1] and prox[i][2] == 'E': return True
                if self['x'] + 1 == prox[i][0] and self['y'] > prox[i][1] and prox[i][2] == 'W': return True
            case 'W':
                if self['y'] - 1 == prox[i][1] and self['x'] > prox[i][0] and prox[i][2] == 'S': return True
                if self['y'] + 1 == prox[i][1] and self['x'] > prox[i][0] and prox[i][2] == 'N': return True
            case 'S':
                if self['x'] - 1 == prox[i][0] and self['y'] < prox[i][1] and prox[i][2] == 'E': return True
                if self['x'] + 1 == prox[i][0] and self['y'] < prox[i][1] and prox[i][2] == 'W': return True
            case 'E':
                if self['y'] - 1 == prox[i][1] and self['x'] < prox[i][0] and prox[i][2] == 'S': return True
                if self['y'] + 1 == prox[i][1] and self['x'] < prox[i][0] and prox[i][2] == 'N': return True
    return False
    

def mustMove():
    global prox
    global self
    global board_dims
    if self['wasHit'] == True:
        if self['direction'] == 'N' and self['y'] > 0 : return True
        if self['direction'] == 'W' and self['x'] > 0 : return True
        if self['direction'] == 'S' and self['y'] < board_dims[1]-1 : return True
        if self['direction'] == 'E' and self['x'] < board_dims[0]-1 : return True
    return False
     
def cannotMove():
    global prox
    global self
    global board_dims
    if self['direction'] == 'N' and self['y'] == 0 : return True
    if self['direction'] == 'W' and self['x'] == 0 : return True
    if self['direction'] == 'S' and self['y'] == board_dims[1]-1 : return True
    if self['direction'] == 'E' and self['x'] == board_dims[0]-1 : return True
    
    
