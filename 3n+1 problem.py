number1,number2=map(int,input("Enter two Number:").split())
cycle_length=1
maximum=0
for number in range(number1,number2+1):
    cycle_length=1
    while(number!=1):
        if not number%2:
            number/=2
        elif number%2:
            number=number*3+1
    
        cycle_length+=1
    if maximum<cycle_length:
        maximum=cycle_length
print(number1,number2,maximum)

