x,y = input().split()
x = int(x)
y = float(y)
if x%5==0 and (x+0.5)<y:
	y=y-(x+0.5)
print("%.2f" %y)
