def search_the_word(i,j,row_index_add,column_index_add,word):
    word_length=len(word)
    for index in range(word_length):  
        if grid[i][j]==word[index]:
            if index!=word_length-1:
                if i<m-1 and j<n-1:
                    if (i==0 and row_index_add==-1) or (j==0 and column_index_add==-1):
                        break
                    else:
                        i+=row_index_add
                        j+=column_index_add
                else:
                    break
        else: 
            break
    else:
        return True
    return False
    

        

def search_first_letter(word):
    adding=(0,1,-1)
    for i in range(m):
        for j in range(n):
            if grid[i][j]==word[0]:
                for row_add in adding:
                    for column_add in adding:
                        if not(row_add==0 and column_add==0):
                            if search_the_word(i,j,row_add,column_add,word):
                                return i,j

no_of_cases=int(input())
output=[]
for case_no in range(no_of_cases):
    case_output=[]
    m,n=map(int,input().split())
    grid=[]
    for i in range(m):
        grid.append(input().lower())
    k=int(input())
    word_list=[]
    for i in range(k):
        word_list.append(input().lower())
    for word in word_list:
        y,x=search_first_letter(word)
        case_output.append(str(y+1)+' '+str(x+1))
    output.append(case_output)

for case_output in output:
    for each in case_output:
        print(each)
    print()