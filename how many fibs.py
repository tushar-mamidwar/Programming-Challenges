a,b=map(int,input().split())
output_list=[]
while a!=0 or b!=0:
    f1,f2,f3=0,1,0
    count=0
    if a==0:
        count+=1
    while(True):
        f3=f1+f2
        f1=f2
        f2=f3
        if(f1>b):
            break
        if(f1>=a):
            count+=1
        
    output_list.append(count)
    a,b=map(int,input().split())

for each in output_list:
    print(each)

"""
********OUTPUT********
PS C:\study material> python -u "c:\study material\CP-1\how many fibs.py"
10 100
1234567890 9876543210
0 0
5
4
"""