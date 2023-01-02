def clean(floor):
    cost=-1
    m = len(floor)
    n = len(floor[0])
    for i in range(m):
            for j in range(n):
                if(floor[i][j] == 1):
                    cost=cost+1
                    print("STATUS:DIRTY")
                    print_floor(floor, i, j)
                    floor[i][j] = 0
                    cost=cost+1
                else:
                    cost=cost+1
                    print("STATUS:CLEAN")
                    print_floor(floor, i, j)
    print("STATUS: ALL STATES CLEANED")
    print_floor(floor, i, j)
    print("Cost=",cost)
    return


def print_floor(floor, row, col):  # row, col represent the current vacuum cleaner position
    print("Row :", row, " Column :", col)
    print(floor)
    print("-----------------")
    

floor1=[[0,0]]
clean(floor1)
