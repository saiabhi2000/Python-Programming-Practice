import mathya i
for _ in range(int(input())):
    x = list(map(int, input().split()))
    y= x.pop(0)
    gc = x[0]
    for i in range(1,y):
        gc = math.gcd(gc,x[i])
    ans = [i//gc for i in x]
    print(*ans)
