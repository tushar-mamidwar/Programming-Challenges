def check_palindrome(num):
    num=str(num)
    lenght=len(num)
    reverse=num[::-1]
    if num==reverse:
        return True
    return int(reverse)


num_list=[]
count=int(input())
for i in range(count):
    num_list.append(int(input()))
for num in num_list:
    for i in range(1000):
        reverse=check_palindrome(num)
        if reverse==True:
            print(i,num)
            break
        num=num+reverse
