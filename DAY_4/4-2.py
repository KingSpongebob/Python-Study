age = input("나이를 입력하세요 : ")
if int(age) >= 20: #괄호를 써도 되고 안써도 됨 
	print("party tonight")
else:
	print("Study tonight")
#파이썬의 코드 구분은 "들여쓰기"로 수행된다.
#함수, 조건, 반복 구조등 내포가 필요한 구문은
#콜론(:)으로 구분된다.

#삼항 연산자
# format : 명령문은 if  참조건 else 거짓일때의 명령문
age = input("나이를 입력하세요: ")
print("party tonight") if int(age)>=20 else print("Study tonight")