T = int(input())
A = []
for i in range(T):
    B = int(input())
    A.append(int(B))
for x in range(T):
    Num=A[x]
    Reverse=0
    while(Num>0):    
        Reminder = Num%10    
        Reverse = (Reverse*10)+Reminder    
        Num = Num//10 
    print("%d"%Reverse)

