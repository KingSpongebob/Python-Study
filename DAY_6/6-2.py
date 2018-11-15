#skip을 포함하는 문자열인 경우 rejected를 출력하고
#구분선을 출력하지 않은 함수
def print_without_skip(xxxx):
	if 'skip' in xxxx:
		print('rejected')
		return
	else:
		print(xxxx)
	pint('-'*10)
#quit을 입력할때 까지 반복하여 사용자 입력을 받음
user_input = ' '
while user_input != 'quit' :
	user_input = input('input: ')
	print_without_skip(user_input)
