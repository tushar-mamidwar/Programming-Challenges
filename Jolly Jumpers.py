output_list=[]
input_list=list(map(int,input().split()))

if input_list[0]==1:
    print('Jolly')
else:
    for i in range (2,input_list[0]+1):
        if abs(input_list[i]-input_list[i-1])>input_list[0]-1:
            print('Not Jolly')
            break
    else:
        print('Jolly')