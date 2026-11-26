# Knight's Tour using Warnsdorff's Rule
# http://en.wikipedia.org/wiki/Knight's_tour
# When calling the script, arguements are as follows:

import sys
from heapq import heappush, heappop # for priority queue
import random
import string
cbx = 8; cby = 8 # width and height of the chessboard
cb = [[0 for x in range(cbx)] for y in range(cby)] # chessboard
# directions the Knight can move on the chessboard
dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

xmap = {
    0 : '1',
    1 : '2',
    2 : '3',
    3 : '4',
    4 : '5',
    5 : '6',
    6 : '7',
    7 : '8'
}

ymap = {
    0 : '8',
    1 : '7',
    2 : '6',
    3 : '5',
    4 : '4',
    5 : '3',
    6 : '2',
    7 : '1'
}

# start the Knight from this position
for k,v in xmap.items():
    if v == str(sys.argv[1]):
        kx = int(k)

for k,v in ymap.items():
    if v == str(sys.argv[2]):
        ky = int(k)


for k in range(cbx * cby):
    cb[ky][kx] = k + 1
    pq = [] # priority queue of available neighbors
    for i in range(8):
        nx = kx + dx[i]; ny = ky + dy[i]
        if nx >= 0 and nx < cbx and ny >= 0 and ny < cby:
            if cb[ny][nx] == 0:
                # count the available neighbors of the neighbor
                ctr = 0
                for j in range(8):
                    ex = nx + dx[j]; ey = ny + dy[j]
                    if ex >= 0 and ex < cbx and ey >= 0 and ey < cby:
                        if cb[ey][ex] == 0: ctr += 1
                heappush(pq, (ctr, i))
    # move to the neighbor that has min number of available neighbors
    if len(pq) > 0:
        (p, m) = heappop(pq)
        kx += dx[m]; ky += dy[m]
    else: break

# print cb
for n in range(cby*cbx + 1):
    if n > 1:
        for cy in range(cby):
            for cx in range(cbx):
                if int(n) == int(cb[cy][cx]):
                    print('ride ' + str(xmap[cx]) + ' ' + str(ymap[cy]), end='\n')