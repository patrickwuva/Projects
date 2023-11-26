import heapq




astroids = [5,10,-5]

def solution(al):
    
    p = []
    n = []

    a = []
     
    for a in al:

        if a >= 0:
            heapq.heappush(p,a)
        else:
        
            heapq.heappush(n,a)
    
    print(n)
    while len(p) and len(n) > 0:
        print(len(n))
        if p[0] == abs(n[-1]):
            p.remove(p[0])
            n.remove(n[-1])
    
        else:
            if p[0] < abs(n[-1]):
                p.remove(p[0])
            else:
                n.remove(n[-1])
    
    print(p,n)
    return 0
solution([10,2,-5,-20])
