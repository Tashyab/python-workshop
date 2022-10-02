def solution(x, y):
    m = (int)(x)
    f = (int)(y)
    gen = 0

    while(True):
        if(m == 1 and f == 1):
            return str(gen)
        elif((m < 1) or (f < 1) or (m == f)):
            return "impossible"
        if(m > f):
            if(m > 20*f):
                fact = m // f - 1
                m -= fact*f
            else:
                m -= f
                fact = 1
        else:
            if(f > 20*m):
                fact = f // m - 1
                f -= fact*m
            else:
                f -= m
                fact = 1
        gen += fact


print(solution(1, 100))
