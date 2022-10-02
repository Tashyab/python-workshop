
def solution(x, y):
    x = (int)(x)
    y = (int)(y)
    ls = [(1, 1)]
    ns = [(1, 1)]
    gen = 0
    if(x == 1 and y == 1):
        return "0"

    while(gen<10**50):
        gen += 1
        for item in ns:
            m = item[0]
            f = item[1]
            m = m + f
            if((m == x) and (f == y)):
                return str(gen)
            else:
                ls.append((m, f))
                m = m - f

            f = f + m
            if((m == x) and (f == y)):
                return str(gen)
            else:
                ls.append((m, f))
                f = f - m

        st = (2 ** gen) - 1
        ns = ls[st:]
    return "impossible"

print(solution(4, 12))