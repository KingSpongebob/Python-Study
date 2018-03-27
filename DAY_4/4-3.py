'''i=0
while i<3:
	print(i)
	i = i+1'''

while True:
	a = input("아무거나 입력하세요 : ")
	if a=='1' and int(a)==1:
		print("The end")
		break
	else: 
		print("This is not one")
		type(a) == int

list_a= [3,6,9,12]
res1 = []
for n in list_a:
	res1.append(n-1)
print(res1)

res2 = [n=2 for n in list_a]
print res2
