#하노이탑 1

def hanoi(n):
	if(n==1): return 1 # 유한성 조건
	else: return hanoi(n-1)+1+hanoi(n-1)		
n = int(input("input hanoi coulum's number :")) #입력(0개 이상)
print(hanoi(n)) #출력(1개 이상)

# 하노이탑 2 축약
n = int(input("input hanoi coulum's number :")) #입력(0개 이상)
print(2**n-1)
#문제 분해를 통해 구조를 알아낸 후 수학적으로 구현한다.
