nlist = []
strnum = ''

with open("pattern.txt", "r") as f:
    txt = f.read()
    for num in txt:
        if(num != '\n'):
            strnum = strnum + num
        else:
            if '29' in strnum:
                nlist.append(int(strnum))
            strnum = ''

# with open("pattendswith9.txt", "a") as f:
#     for ele in nlist:
#         f.write(f"{str(ele)}\n")
with open("pattwith29.txt", "a") as f:
        for ele in nlist:
            f.write(f"{str(ele)}\n")
