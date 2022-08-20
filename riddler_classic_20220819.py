
"""

https://fivethirtyeight.com/features/can-you-find-your-pills/ 


[0, 15, 0, 1.0]
[1, 13, 1, 1.0]
[2, 11, 2, 0.8571428571428571]
[2, 12, 0, 0.14285714285714285]
[3, 9, 3, 0.6043956043956044]
[3, 10, 1, 0.3956043956043956]
[4, 7, 4, 0.3296703296703296]
[4, 8, 2, 0.5956543456543456]
[4, 9, 0, 0.07467532467532467]
[5, 5, 5, 0.12587412587412586]
[5, 6, 3, 0.5664335664335665]
[5, 7, 1, 0.3076923076923077]
[6, 3, 6, 0.02797202797202797]
[6, 4, 4, 0.3234265734265734]
[6, 5, 2, 0.5649350649350648]
[6, 6, 0, 0.08366633366633366]
[7, 1, 7, 0.0023310023310023306]
[7, 2, 5, 0.08828671328671328]
[7, 3, 3, 0.5066956852671138]
[7, 4, 1, 0.40268659911517046]
[8, 0, 6, 0.005078255078255077]
[8, 1, 4, 0.16165382236810807]
[8, 2, 2, 0.6468584986442123]
[8, 3, 0, 0.18640942390942397]
[9, 0, 3, 0.2098802982731553]
[9, 1, 1, 0.7901197017268448]
[10, 0, 0, 0.9999999999999998]


There is a 0.7901197017268448 chance that there was nothing left in the bottle


"""


def nextDay(d, f, h, p):
    l = [] 
    
    if h > 2:
        #3 half pills
        l.append([d+1, f, h-3, p * 1.0 * (h * (h-1) * (h-2)) / ((f + h) * (f + h - 1) * (f + h - 2))])
        
    if h > 1 and f > 0:
        #2 half pills and then a full pill
        l.append([d+1, f-1, h-1, p * 1.0 * (h * (h-1) * (f)) / ((f + h) * (f + h - 1) * (f + h - 2))])
    
    if f > 1:
        #2 full pills
        l.append([d+1, f-2, h+1, p * 1.0 * (f * (f-1)) / ((f + h) * (f + h - 1))])
        
    if f > 0 and h > 0:
        #1 full pill and 1 half pill
        l.append([d+1, f-1, h-1, p * 1.0 * (2 * f * h) / ((f + h) * (f + h - 1))])
    
    return l


def compare(a, b):
    
    same, i = True, 0
    
    while same == True and i < 3:
        same = (a[i] == b[i])
        i += 1

    return same 


def consolidate(l):
    
    m = [] 
    
    if len(l) > 0:
    
        for a in l:
            included = False
            for b in m:
                if compare(a, b):
                    b[3] += a[3]
                    included = True
            
            if not included: 
                m.append(a)
            
    return m 


def helper(m, l): 
    
    n = nextDay(m[0], m[1], m[2], m[3])
    #print('Here', n)
    
    if len(n) > 0:
        
        for x in n:
            l.append(x)
        
        for x in n:
            helper(x, l)


def main(): 
    
    #list of possibilities
    l = [] 
    
    #day 0: 15 full pills, 0 half pills, 100% probability
    m = [0, 15, 0, 1.0]
    l.append(m)
        
    helper(m, l)
    
    l = consolidate(l)
    
    l.sort() 
    
    for x in l:
        print(x) 
        if x[0] == 9 and x[1] == 1:
            sol = x[3] 
    
    print('\n')
    
    print(f"There is a {sol} chance that there was nothing left in the bottle")
    
if __name__ == '__main__':
    main() 