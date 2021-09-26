n = int(input())
a = input().split()
w = []
gv=0
coins=0
for i in a:
	w.append(int(i))
m = int(input())
l=[]
for i in range(m):
	x=input().split()
	l.append(x)
for j in l:
	gv=int(j[0])
	y=min(w,key = lambda x:abs(x-gv))
	#print(y,gv)
	if gv in w:
		coins+=0
	elif y< gv:
		coins+=abs(y-gv)
		#print(abs(y-gv))
	#print(sum(w)-y,j[1])
	y=sum(w)-y
	if y < int(j[1]):
		coins+=abs(y-int(j[1]))
		#print(abs(y-int(j[1])))
	print(coins)
	coins=0
