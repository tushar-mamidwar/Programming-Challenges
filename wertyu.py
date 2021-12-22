inp=input()
output=""
querty_layout="QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,./qwertyuiop[]asdfghjkl;'zxcvbnm,./"

for character in inp:
    if character==" " or character=='q' or character=='Q' or character=='a' or character=='A' or character=='z' or character=='Z':
        output+=character
        continue
    else:
        index=querty_layout.index(character)
        output+=querty_layout[index-1]

print(output)