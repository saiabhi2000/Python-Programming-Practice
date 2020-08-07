t = int(input())
for i in range(t):
    a = int(input())
    b = list(map(int,input().split()))
    for j in b:
        if (j%2==0):
            print('NO')
            break
    else:
        print('YES')
