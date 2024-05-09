def enc(dic):
    sym = input("Enter the symbol to be encoded: ")
    h = 1
    l = 0
    for sm in sym:
        k = h-l
        h = l + dic[sm][1] * k
        l = l + dic[sm][0] * k
    print(f"[{l}, {h})")
        

def dec(dic):
    sym = float(input("Enter the encoded symbol to decode: "))
    if(sym < 1 and sym >0):
        h = 1
        l = 0
        overflow = 100 # Run upto maximum 100 codes
        code = ""
        while(l != sym and overflow > 0):
            k = h - l
            for key in dic:
                h = l + dic[key][1] * k
                if(sym < h):
                    code += key
                    l = l + dic[key][0] * k
                    break
            overflow -=1
        if(overflow == 0):
            print("Code overflow")
        else:
            print(code)
    else:
        print("Wrong encoding")

if __name__=="__main__":
    try:
        ch = int(input("Enter 1 for encoding or 0 for decoding: "))
    except Exception as e:
        print("Enter from the given choices.")
    
    n = int(input("Enter the number of unique symbols: "))
    dic = {}
    pl = 0
    ph = 0
    for i in range(n):
        s = input(f"Enter the {i+1}th symbol: ")
        p = float(input(f"Enter the prob. of {i+1}th symbol: "))
        ph += p
        dic[s] = (pl, ph)
        pl += p

    if(ch == 1):
        enc(dic)
    elif(ch == 0):
        dec(dic)
    else:
        print("Wrong input")
