def powfinder(num):
    count=0
    while(num>1):
        num=num/2
        count+=1
    return count

print(powfinder(16))