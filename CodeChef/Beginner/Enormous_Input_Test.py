x,y=map(int, input().split())
count=0
while(x>0):
	num=int(input())
	if(num%y==0):
		count+=1
	x=x-1
	
print(count)
