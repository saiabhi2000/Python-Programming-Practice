t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    sum = 0
    for j in range(b+1):
        sum += j
    for j in range(a-1):
        x = 0
        for k in range(sum+1):
            x += k
        sum = x
    print(sum)
        
        
    
