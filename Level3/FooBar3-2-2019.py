def is_prev(c, hist):
    '''Checks if a current path is a repeat and updates the history.'''
    res = str(c['r']) + '_' + str(c['c']) + '_' + str(c['hammer'])
    if not res in hist:
        hist[res] = 1
        return False
    return True

def is_wall(r, c, m):
    return m[r][c]

def adjacent(r, c, m):
    x = [(i+r,j+c) for i,j in [(1, 0), (0, 1), (-1, 0), (0, -1)] ]
    return filter(lambda p: -1 < p[1] < len(m[0]) and -1 < p[0] < len(m), x)

def solution(m, paths=[{'r': 0, 'c': 0, 'hammer': 1}], hist={}, a=1):
    w, h = len(m[0]) - 1, len(m) - 1
    new_paths = []
    for p in paths:
        r,c = p['r'], p['c']
        if (r,c) == (h, w): return a  # Check for win condition
        if is_prev(p, hist): continue # Check for repeat situations
        # Add all possible directions for a previous path
        for i,j in adjacent(r, c, m):
            new = {'r': i, 'c': j}
            if is_wall(i, j, m) and p['hammer']:
                # Use hammer to smash wall
                new['hammer'] = 0
                new_paths.append(new) 
            elif not is_wall(i, j, m):
                # Walk normally without smashing anything
                new['hammer'] = p['hammer']
                new_paths.append(new)
    return solution(m, paths=new_paths, hist=hist, a=a+1)   

mapp = [[0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]
print(solution(mapp) )

'''
Prepare the Bunnies' Escape
===========================
You're awfully close to destroying the LAMBCHOP doomsday device and freeing
Commander Lambda's bunny prisoners, but once they're free of the prison blocks,
the bunnies are going to need to escape Lambda's space station via the escape
pods as quickly as possible. Unfortunately, the halls of the space station are a
maze of corridors and dead ends that will be a deathtrap for the escaping
bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling
project that will give you the opportunity to make things a little easier for
the bunnies. Unfortunately (again), you can't just remove all obstacles between
the bunnies and the escape pods - at most you can remove one wall per escape
pod path, both to maintain structural integrity of the station and to avoid
arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and
ending at the door to an escape pod. The map is represented as a matrix of 0s
and 1s, where 0s are passable space and 1s are impassable walls. The door out of
the prison is at the top left (0,0) and the door into an escape pod is at the
bottom right (w-1,h-1). 

Write a function answer(map) that generates the length of the shortest path from
the prison door to the escape pod, where you are allowed to remove one wall as
part of your remodeling plans. The path length is the total number of nodes you
pass through, counting both the entrance and exit nodes. The starting and ending
positions are always passable (0). The map will always be solvable, though you
may or may not need to remove a wall. The height and width of the map can be
from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves
are allowed.

Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int) maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
Output:
    (int) 7
Inputs:
    (int) maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 11
'''
    
    
    
