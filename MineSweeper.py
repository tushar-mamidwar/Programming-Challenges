M,N=map(int,input().split())
def mine_sweeper():
    if not M<=100 and not N>0:
        print("invalid M or N input")
        return

    field=[]
    print("Enter field:")
    for i in range(M):
        column=input()
        column = list(column)
        field.append(column)
    for i in range(M):
        for j in range(N):
            if field[i][j]!="*":
                field[i][j]=0

    for i in range(M):
        for j in range(N):
            if field[i][j]=="*":
                if i-1>=0:
                    if j-1>=0:
                        field[i-1][j-1]+=1
                    field[i-1][j]+=1
                    if j+1<N:
                        field[i-1][j+1]+=1
                if j-1>=0:
                    field[i][j-1]+=1
                if j+1<N:
                    field[i][j+1]+=1
                if i+1<M:
                    if j - 1 >= 0:
                        field[i + 1][j - 1] += 1
                    field[i + 1][j] += 1
                    if j + 1 < N:
                        field[i + 1][j + 1] += 1
    display(field)
def display(field):
    for column in field:
        for i in column:
            print(i,end="")
        print()
mine_sweeper()