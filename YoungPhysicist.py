n = int(input())
f=[]
for i in range(n):
	x,y,z=input().split()
	if i ==0:
		f=[int(x),int(y),int(z)]
	else:
		f=[f[0]+int(x),f[1]+int(y),f[2]+int(z)]
if f == [0,0,0]:
	print('YES')
else:
	print('NO')
