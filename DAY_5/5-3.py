#중복되지 않은 10개의 코드를 가진 암호코드표가 주어지고,
#각각의 암호 코드에는 0부터 9까지의 숫자가 매칭된다.
#암호문이 주어졌을 때 이 암호코드를 기반으로 암호문을 
#복호화하는 알고리즘(파이썬 코드를 작성하시오)
#공백을 허용한다+

#현재상태 : 암호호콛드가 입력된 상황
#목표상태 : 암호코드에서 암호문의 문자를 찾아 인덱스 출력
#핵심요소1 : 공백이 입력되면 공백을 반환
#핵심요소2 : 문자가 입력되면 암호문을 순차 탐색하여 인덱스 반환
'''
#축약전
a = input()
b = input()
i=0
while(i<len(b))
	if b[i] !=' ':
		print(a.find(b[i]), end="")
	else:
		print(b[i], end="")
		i=i+1
		'''
# 축약 while
a = input()
b = input()
i=0
while(i<len(b))
	print(a.find(b[i]) if b[i]=' 'else b[i], end="")
	i=i+1
'''
#축약 for
a = input()
b = input()
i=0
for i in b:
	print(a.find(i)if i!=' ' else i, end="")'''