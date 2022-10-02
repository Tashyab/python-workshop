def solution(src, dest):
    sx, sy = src % 8, int(src / 8)
    dx, dy = dest % 8, int(dest / 8)
    
    xdif = abs(sx - dx)
    ydif = abs(sy - dy)

    if((sx==dx) and (sy == dy)):
        return 0

    if (xdif == ydif):
        if(xdif==1):
            if((sx == 0) or (sx == 7) or (sx == 56) or (sx ==63)):
                return 4
            else:
                return 2
        elif(xdif == 3):
            return 2
        elif(xdif ==7):
            return 6
        else:
            return 4
        
    elif((sx == dx) or (sy == dy)):
        if((xdif == 1) or (ydif == 1)):
            return 3
        elif((xdif == 2) or (ydif == 2)):
            return 2
        elif((xdif == 3) or (ydif == 3)):
            return 3
        elif((xdif == 4) or (ydif == 4)):
            return 2
        elif((xdif == 5) or (ydif == 5)):
            return 3
        elif((xdif == 6) or (ydif == 6)):
            return 4
        elif((xdif == 7) or (ydif == 7)):
            return 5

    elif((xdif == 1) or (ydif == 1)):
        if((xdif == 2) or (ydif == 2)):
            return 1
        elif(xdif == 3) or (ydif == 3):
            return 2
        elif(xdif == 4) or (ydif == 4):
            return 3
        elif(xdif == 5) or (ydif == 5):
            return 4
        elif(xdif == 6) or (ydif == 6):
            return 3
        elif(xdif == 7) or (ydif ==  7):
            return 4
        
    elif((xdif == 2) or (ydif == 2)):
        if((xdif == 3) or (ydif == 3)):
            return 3
        elif(xdif == 4) or (ydif == 4):
            return 2
        elif(xdif == 5) or (ydif == 5):
            return 3
        elif(xdif == 6) or (ydif == 6):
            return 4
        elif(xdif == 7) or (ydif == 7):
            return 5

    elif((xdif == 3) or (ydif == 3)):
        if(xdif == 4) or (ydif == 4):
            return 3
        elif(xdif == 5) or (ydif == 5):
            return 4
        elif(xdif == 6) or (ydif == 6):
            return 3
        elif(xdif == 7) or (ydif == 7):
            return 4

    elif((xdif == 4) or (ydif == 4)):
        if(xdif == 5) or (ydif == 5):
            return 3
        elif(xdif == 6) or (ydif == 6):
            return 4
        elif(xdif == 7) or (ydif == 7):
            return 5

    elif((xdif == 5) or (ydif == 5)):
        if(xdif == 6) or (ydif == 6):
            return 5
        elif(xdif == 7) or (ydif == 7):
            return 4

    elif((xdif == 5) or (ydif == 5)):
        if(xdif == 6) or (ydif == 6):
            return 5
        elif(xdif == 7) or (ydif == 7):
            return 4
    
    elif((xdif == 6) or (ydif == 6)):
        if(xdif == 7) or (ydif == 7):
            return 5
        



    