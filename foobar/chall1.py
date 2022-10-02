import re

def solution(s):
    i = 0
    part = s[0]
    while(len(part) != len(s)):
        print(part) 
        lf = re.findall(part, s)
        if (len(lf) * len(part) == len(s)):
            return len(lf)
        i += 1
        part = part + s[i]   
    return 1
if __name__ == "__main__":
    print(solution("abcdabcdabcdabcd"))
    
