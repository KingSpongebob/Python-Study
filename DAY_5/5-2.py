# 계단오르기
#축약 전

'''
def stair(n):
	if(n==1):return 1
	elif(n==2):return 
	else:return stair(n-1)*stair(n-2)
n = int(input("input stair's number : "))
print(stair(n))
'''

# 계단 오르기 2
# 축약 후
def stair(n):
	if(n<3):return n
	else:return stair(n-1)+stair(n-2)

n = int(input("input stair's number : "))
print(stair(n))