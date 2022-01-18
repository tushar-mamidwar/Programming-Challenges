name_changes=[]
text=[]

number_name_changes=int(input())
for i in range(number_name_changes):
    name_change=input().strip('"').split('" to "')
    name_changes.append(name_change)

number_of_lines=int(input())
for j in range(number_of_lines):
    text.append(input())

for i in range(number_of_lines):
    for old_name,new_name in name_changes:
        text[i]=text[i].replace(old_name,new_name)    
print()
for line in text:
    print(line)