t= int(input())
for i in range(0,t):
    (a,b)=(int,input().split())
    if a>b:
        min=a
    else:
        min=b
    max=a+b
    print(min,max)
    
