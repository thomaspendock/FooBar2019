from math import atan2, sqrt, hypot

# flips the point over wall (0 or dim) n times  
def flip(n, point, dim):
    wall_dists = [2*point, 2*(dim-point)]
    j = 1 if n < 0 else -1
    for i in range(n, 0, j):
        point -= j * wall_dists[(i + (n < 0))%2]
    return point

def get_mirrored(coord, dims, dis):
    coords = []
    for i in range(2):
        rnge = range(-(dis//dims[i])-1, (dis//dims[i])+2)
        coords.append([flip(p, coord[i], dims[i]) for p in rnge])
    return coords

def solution(dims, pos, gpos, dis):
    beam_dists = dict()
    angles = set()
    
    [your_coords, guard_coords] = [get_mirrored(pos,  dims, dis),
                                   get_mirrored(gpos, dims, dis)]

    for c in [your_coords, guard_coords]:
        coords = [(x,y) for x in c[0] for y in c[1]]
        for x,y in coords:
            dx, dy = pos[1]-y, pos[0]-x
            beam   = atan2(dy, dx)
            length = hypot(dy, dx)
            
            if [x,y] == pos or dis < length: continue
            min_beam = (beam in beam_dists and beam_dists[beam] > length)
            update_dists = min_beam or beam not in beam_dists
            if not update_dists: continue
            
            beam_dists[beam] = length
            if c == guard_coords: angles.add(beam)
    return len(angles)
            


dimensions = [2,5]
captain_position = [1,2]
badguy_position = [1,4]
distance = 11

dimensions = [2,5]
captain_position = [1, 2]
badguy_position = [1,4]
distance = 11

dimensions = [10,10]
captain_position = [4, 4]
badguy_position = [3,3]
distance = 5000
print(solution(dimensions, captain_position, badguy_position, distance))

   
'''
Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards!
Fortunately, you grabbed a beam weapon from an abandoned guard post while you
were running through the station, so you have a chance to fight your way out.
But the beam weapon is potentially dangerous to you as well as to the elite
guard: its beams reflect off walls, meaning you'll have to be very careful where
you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming
too weak to cause damage. You also know that if a beam hits a corner, it will
bounce back in exactly the same direction. And of course, if the beam hits
either you or the guard, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, guard_position, distance)
that gives an array of 2 integers of the width and height of the room, an array
of 2 integers of your x and y coordinates in the room, an array of 2 integers of
the guard's x and y coordinates in the room, and returns an integer of the
number of distinct directions that you can fire to hit the elite guard, given
the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and
the elite guard are both positioned on the integer lattice at different
distinct positions (x, y) inside the room such that
[0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can
travel before becoming harmless will be given as an integer
1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with
dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum
shot distance of 4, you could shoot in seven different directions to hit the
elite guard (given as vector bearings from your location): [1, 0], [1, 2],
[1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot
at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot
at bearing [-3, -2] bounces off the left wall and then the bottom wall before
hitting the elite guard with a total shot distance of sqrt(13), and the shot at
bearing [1, 2] bounces off just the top wall before hitting the elite guard with
a total shot distance of sqrt(5).

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases -- 
Input:
Solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
Solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9

-- Python cases -- 
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9
'''
