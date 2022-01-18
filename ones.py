number=1
multiple=1
n=int(input())
while number%n!=0:
    multiple*=10
    number+=multiple
    print(number)
print(len(str(number)))
