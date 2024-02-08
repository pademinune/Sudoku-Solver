
# def fact(n):
#     if n <= 1:
#         return 1
#     return n*fact(n-1)

# print(fact(9)**9)

def createList(items,index=0):
    if type(items[index]) == list:
        if len(items) == index+1:
            return createList(items[index])
        return createList(items[index])+createList(items[index+1:])
    elif len(items) == index+1:
        return [items[index]]
    return [items[index]] + createList(items[index+1:])
# print(createList([1,2,4,[1,2,[[3,3,[[3]],6]]]]))

def replace(grid,square,row,col,num):
    return grid[:square]+[grid[square][:row]+[grid[square][row][:col]+[num]+grid[square][row][col+1:]]+grid[square][row+1:]]+grid[square+1:]

def prodLengths(lst):
    prod = 1
    for i in lst:
        prod *= len(i)
    return prod

def order(d):
    newD = {}
    for i in range(len(list(d.values()))):
        minKey = findMinLength(d)
        newD[minKey] = d[minKey]
        d.pop(minKey)
    return newD


def prodLengthsDict(d):
    return prodLengths(list(d.values()))

def findMinLength(lst):
    values = list(lst.values())
    minThing = values[0]
    for i in values:
        if len(i) < len(minThing):
            minThing = i
    for key,value in lst.items():
        if value == minThing:
            return key

def findIfEmpty(lst):
    values = list(lst.values())
    for i in values:
        if len(i) == 0:
            return True
    return False

def squareValid(grid):
    alreadySeen = []
    # print(grid)
    for row in grid:
        for col in row:
            if col is None:
                continue
            elif col in alreadySeen:
                return False
            else:
                 alreadySeen.append(col)
    return True

def rowValid(squares,row):
    alreadySeen = []
    # print(squares)
    for num in list(squares[0][row]+squares[1][row]+squares[2][row]):
        if num is None:
            continue
        elif num in alreadySeen:
            return False
        else:
            alreadySeen.append(num)
    return True

def colValid(squares,col):
    alreadySeen = []
    for square in squares:
        for row in square:
            num = row[col]
            if num is None:
                continue
            elif num in alreadySeen:
                return False
            else:
                alreadySeen.append(num)
    return True

def isValid(grid):
    # for rownum in range():
    for square in grid: #checking each square
        if not squareValid(square):
            # print(square)
            return False
    for row in range(9):
        squareRow = int(row/3)*3
        if not rowValid([grid[squareRow]]+[grid[squareRow+1]]+[grid[squareRow+2]],row%3):
            # print("row",row)
            # print([grid[squareRow]]+[grid[squareRow+1]]+[grid[squareRow+2]])
            return False
    for col in range(9):
        squareCol = int(col/3)
        if not colValid([grid[squareCol]]+[grid[squareCol+3]]+[grid[squareCol+6]],col%3):
            # print(col)
            return False
    return True

def isValidExtended(grid): #slower, dont use
    # for rownum in range():
    if findIfEmpty(PossibilityGrid(grid)):
        return False
    for square in grid: #checking each square
        if not squareValid(square):
            # print(square)
            return False
    for row in range(9):
        squareRow = int(row/3)*3
        if not rowValid([grid[squareRow]]+[grid[squareRow+1]]+[grid[squareRow+2]],row%3):
            # print("row",row)
            # print([grid[squareRow]]+[grid[squareRow+1]]+[grid[squareRow+2]])
            return False
    for col in range(9):
        squareCol = int(col/3)
        if not colValid([grid[squareCol]]+[grid[squareCol+3]]+[grid[squareCol+6]],col%3):
            # print(col)
            return False
    return True

def PossibilityGrid(grid):
    possibles = {}
    for square in range(9):
        for row in range(3):
            for col in range(3):
                # tmp = grid.copy()
                if grid[square][row][col] is None:
                    key = (square,row,col)
                    possibles[key] = []
                    for num in range(1,10):
                        # tmp[square][row][col] = num
                        # print(tmp)
                        if isValid(replace(grid,square,row,col,num)):
                            possibles[key].append(num)
                        # tmp = grid
    # print(tmp)
    return possibles

# grid = [[[None,None,None] for i in range(3)] for n in range(9)]

#squares -> square -> row -> item

# grid[0][0] = [None,2,7]
# grid[0][2] = [None,1,3]
# grid[6][0][0] = 1
# print(grid)
# print(replace(6,0,0,1))
# print(isValid(grid))
# print(grid)

# possibles = PossibilityGrid()
# print(possibles)
# print("\n")
# possibles = order(possibles)
# print(possibles)


# print(grid)
# print(squareValid([[1,2,3],[4,5,6],[7,None,None]]))


grid = [[[] for i in range(3)] for i in range(9)]


rawIn = []
for i in range(9):
    rawIn += list(map(int,input().split()))

# print(rawIn)

for i in range(len(rawIn)):
    squareCol = int((i%9)/3)
    squareRow = int(i/27)
    itemRow = int(i/9)
    itemCol = (i%3)
    if rawIn[i] == 0:
        grid[squareRow*3 + squareCol][itemRow%3].append(None)
    else:
        grid[squareRow*3 + squareCol][itemRow%3].append(rawIn[i])

# print(grid)

# print(isValid(grid))
possibles = order(PossibilityGrid(grid))


things = [['a','b','c'],['a','d'],['1','2']]
numsPoss = list(possibles.values())
# print(numsPoss)
# print(possibles)
# for i in range(prodLengths(numsPoss)):
i = 0
while i < prodLengths(numsPoss):
    # print("hi")
    tryGrid = grid.copy()
    # current = []
    for r in range(len(numsPoss)):
        beforeWeight = prodLengths(numsPoss[r:])
        weight = prodLengths(numsPoss[r+1:])
        ind = int((i%(beforeWeight))/weight)
        coords = list(possibles.keys())[r]
        num = numsPoss[r][ind]
        tryGrid = replace(tryGrid,coords[0],coords[1],coords[2],num)
        # print(num)
        # if not isValidExtended(tryGrid):
        if not isValid(tryGrid):
            i = i - i%beforeWeight + (ind+1)*weight
            # print(num)
            break
        # current.append(things[r][ind])
    else:
        print("\n\n")
        # print(tryGrid)
        break
    # print(current)


#printing the formatted grid
for rowNum in range(9):
    squareRow = rowNum%3
    currentRow = ""
    firstSquare = rowNum - squareRow
    for i in range(3):
        currentRow += "{} {} {} ".format(tryGrid[firstSquare+i][squareRow][0], tryGrid[firstSquare+i][squareRow][1], tryGrid[firstSquare+i][squareRow][2])
    print(currentRow[:-1])

# 9 2 6 1 7 8 5 4 3
# 4 7 3 6 5 2 1 9 8
# 8 5 1 9 4 3 6 2 7
# 6 8 5 2 3 1 9 7 4 
# 7 3 4 8 9 5 2 6 1 
# 2 1 9 4 6 7 8 3 5
# 5 6 8 7 2 4 3 1 9
# 3 4 2 5 1 9 7 8 6
# 1 9 7 3 8 6 4 5 0


# 1 4 5 0 0 0 3 7 8
# 0 7 0 0 5 0 0 0 0
# 0 0 0 3 0 7 0 6 1
# 8 0 0 0 3 5 1 0 0
# 9 3 6 0 0 0 0 0 0
# 0 0 7 4 0 9 0 0 0
# 0 6 2 5 1 0 0 8 4
# 3 0 1 0 9 4 0 0 7
# 0 5 0 8 7 0 6 1 0

# 9 2 6 1 7 8 5 4 3
# 4 7 3 6 5 2 1 9 8
# 8 5 1 9 4 3 6 2 7
# 6 8 5 2 3 1 9 7 4
# 7 3 4 8 9 5 2 6 1
# 2 1 9 4 6 7 8 3 5
# 5 6 8 7 2 4 3 1 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

# 0 1 9 3 0 0 4 2 0
# 7 5 3 0 2 0 0 0 1
# 0 0 0 9 6 1 0 7 5
# 3 6 8 0 0 7 0 0 9
# 0 2 0 0 1 6 7 4 0
# 4 0 0 5 0 3 2 0 6
# 5 0 7 6 8 4 0 0 0
# 1 0 0 0 3 0 8 5 4
# 8 0 2 1 0 0 6 3 0


#Evil:
# 7 0 0 0 0 0 3 0 0
# 0 0 5 0 0 9 2 0 1
# 0 9 0 4 0 0 0 0 0
# 0 0 2 0 0 4 9 0 5
# 6 0 0 0 7 0 0 0 0
# 0 0 0 0 0 0 0 8 0
# 0 0 0 0 0 1 0 3 0
# 2 0 0 6 0 0 1 0 8
# 0 0 8 0 0 0 0 4 0