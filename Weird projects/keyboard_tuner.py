notes = ['c2', 'd2', 'e2', 'f2', 'g2', 'a2', 'b2',
        'c3', 'd3', 'e3', 'f3', 'g3', 'a3', 'b3',
        'c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4',
        'c5', 'd5', 'e5', 'f5', 'g5', 'a5', 'b5',
        'c6', 'd6', 'e6', 'f6', 'g6', 'a6', 'b6',
        'c7']

keyb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 
        'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm']

note_dic = dict(zip(notes, keyb))
nt = input("Enter notes: ")

print("Keyboard keys: ")

i=0
while(i<len(nt)):
    if nt[i].isalpha():
        print(f"{note_dic[nt[i]+nt[i+1]]}", end='')
        i+=2
    else:
        print(nt[i], end='')
        i+=1
