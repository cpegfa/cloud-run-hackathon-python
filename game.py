import json
import numpy as np
from collections import defaultdict

import time


#config
radar_size = 1      # area of players to consider, 4 = consider (4 * 2 + 1)^2
step_count = 1      # step number of the game
history_depth = 0   # 0 - all history
history=defaultdict(np.array)
data = 0            # json data
board_dim = None          # game board dimension in a tuple (row,column)
self = None                 # my position on the game board

def markAt(board, p):
    match p['direction']:
        case "N":
            adj = 0
        case "W":
            adj = 1
        case "S":
            adj = 2
        case "E":
            adj = 3
    #board[p['x'], p['y']] = adj+1
    board[(p['x']+radar_size)*5+adj, p['y']+radar_size] = 1
    if p['wasHit']: board[(p['x']+radar_size)*5+4, p['y']+radar_size] = 1



"""
Read Json and Prepare variables
"""
def get_game_state(infos):
    global self
    myurl = infos['_links']['self']['href']
    players = infos['arena']['state']
    for key, info in players.items():
        if key == myurl:
            self={'x':info['x'],'y':info['y'],'direction':info['direction'],'wasHit':info['wasHit'],'score':info['score']}

    
def readJson():
    with open('arena.json','r') as f:
        data = json.load(f)

def promxityUser():
    players = data['arena']['state']
    


def prepareHistory():
    start_time = time.time()

    arena = data['arena']
    players = arena['state']
    noofplayers = len(arena['state'])
    lastRound = data

    #print(data)
    print('no. of player:',len(arena['state']))
    print('dims0:',arena['dims'][0])
    print('dims1:',arena['dims'][1])


    """
    Map gameboard
    """

    #gameboard = np.zeros((arena['dims'][0], arena['dims'][1]))
    gameboard = np.zeros(((arena['dims'][0]+2*radar_size)*5, arena['dims'][1]+2*radar_size),dtype='i')   # radar_size padding at both end
    gameboard[:radar_size*5].fill(2)
    gameboard[-radar_size*5:].fill(2)
    gameboard[:,:radar_size].fill(2)
    gameboard[:,-radar_size:].fill(2)

    for key, info in players.items():
        print(key," is at ", info['x'],",",info['y']," facing ", info['direction']) 
        markAt(gameboard, info)
        
    with np.printoptions(threshold=np.inf,linewidth=200):
        print(np.transpose(np.copy(gameboard)))


    """
    Store history
    """

    radar_idx = 1
    #buf = [[0]*(radar_size*2+1)*5]* (radar_size*2+1) 
    buf = [[0]*(radar_size*2+1)*5]* (radar_size*2+1) 

    #with np.printoptions(threshold=np.inf,linewidth=200):
        #print(np.transpose(gameboard))

    for key, info in players.items():
        #for i in range(radar_size*2+1):
        buf = gameboard[info['x']*5:(info['x']+radar_size*2+1)*5,info['y']:info['y']+radar_size*2+1]      # range (incl):(excl)
        print(info['x']*5,":", (info['x']+radar_size*2+1)*5,",",info['y'],":",info['y']+radar_size*2+1)
        if key not in history:
            history[key] = buf
        else:
            history[key].append(np.concatenate(np.transpose(buf),axis=None))
        with np.printoptions(threshold=np.inf,linewidth=500):
            #print(key,":",np.concatenate(np.transpose(buf),axis=None))
            print(key,":",buf)
    print(history) 
        




    print("--- %s seconds ---" % (time.time() - start_time))

