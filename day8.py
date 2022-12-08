import pprint
with open('input.txt') as temp_file:
    input = [line.rstrip('\n') for line in temp_file]


"""def checkUp(grid, row,col):
    index = row - 1
    ret = False
    while True:
        if(grid[row][col] > grid[index][col]) and not ret:
            ret = True
        else:
            ret = False
        index -= 1
        
        if index < 0:
            break
    return ret"""
G = []

for line in input:
    G.append(list(line))

edge_trees = (len(G)*4) - 4 
inner_trees = 0
for i in range(0, len(G)):
    for j in range(0,len(G)):
        G[i][j] = int(G[i][j])

"""print(grid)

for i in range(1, len(grid) - 1):
    for j in range(1,len(grid) - 1):
        print(checkUp(grid , i , j))
    print()
print(edge_trees)"""

DIR = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(G)
C = len(G[0])

p1 = 0
for r in range(R):
    for c in range(C):
        vis = False
        for (dr,dc) in DIR:
            rr = r
            cc = c
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                if G[rr][cc] >= G[r][c]:
                    ok = False
            if ok:
                vis = True
        if vis:
            p1 += 1
print(p1)

p2 = 0
for r in range(R):
    for c in range(C):
        score = 1
        for (dr,dc) in DIR:
            dist = 1
            rr = r+dr
            cc = c+dc
            while True:
                if not (0<=rr<R and 0<=cc<C):
                    dist -= 1
                    break
                if G[rr][cc]>=G[r][c]:
                    break
                dist += 1
                rr += dr
                cc += dc
            score *= dist
        p2 = max(p2, score)
print(p2)