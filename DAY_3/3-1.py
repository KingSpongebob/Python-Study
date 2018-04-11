#count
a = 'programming'
res =a.count('m')
print(res)
#count 함수가 메소드로 지정된 변수의 문자열에서 
# 카운트함수 인자(문자)으 개수를 변환한다.
#만약 a에 숫자를 담고 count에 숫자 인자를 넣으면?
#-> 불가능하다. 이유는 문자열 함수이기 때문이다
#-> 그래도 숫자를 세고싶다면?

#find 
a = "programming"
res = a.find('m')
print(res)
#find함수가 메소드로 지정된 변수의 문자열에서
#find함수 인자(문자)의 인덱스를 반환한다.
#만약 찾는 문자가 없다면? => -1을 출력한다.
# ex) if(res == -1)또는 res+1

#index

a = 'programming'
res = a.index('m')
print (res)
#만약 찾는 문자가 없다면? => 에러출력

#join
a = '_m-_-_m'
res = a.join('ABC')
print (res)
#find 함수가 메소드로 지정되 변수의 문자를
#find함수의 인자(문자) 사이에 삽입한다.
#숫자도 될까? => 당연히 안됨/ 문자열 함수 이므로, 
#가능하게 하는 방법? => 숫자를 문자로 지정해주면 가능
#한줄씩 띄어쓰기를 하고 싶을때
# => a='\n'

#준현이 타임 -> 성훈이 타임
#a= [1],'sfsdfsd',123 ,'ssdfs']
#print(a[2:4])
#print(st(a)[1:1]) #대괄호를 밴 결과(꼼수)

#upper
a = 'programming'
res = a.upper
print(res)
#대문자로 변환됨

#lower
a = 'PROGRAMMING'
res = a.lower()
print(res)
#소문자로 변환한 값을 반환한다.
#특수문자에 대해서도 될까? => upper, lower둘다 안됨.

#replace
a = 'programming'
res =a.replace('programming','gamer')
print(res)
#문자열을 치환한 결과를 반환한다.
#공백으로 치환이 가능할까? replace('','1')
#공백으로부터 치환이 가능할까? replace('g','')	
#띄어쓰기로 부터 치환이 가능할까? replace('','1')
#없는 문자열은 치환이 불가능하다. => 원본 그대로 출력

#split
a = 'pro gramm ing'
res = a.split(' ')
print(res)
#문자열을 나눈 결과를 반환한다. => result is list type
#a= 'a1p1p1l1e' // res = a.split('1')
#결과가 리스트이므로 나눈결과를 결합하려면 인덱스를 활용한다.


#lstrip
a = '	programming    '
res = a.lstrip()
print (res)
print(res +'1')
 #왼쪽 공백이 제거되었는지 확인

#rstrip
a = '	programming    '
res = a.rstrip()
print (res)
print(res +'1') #오른쪽 공백이 제거되었는지 확인

#strip
a = a.strip()
res = a.strip()
print('1'+ res+'1')

#type
a = 'programming'
res = type(a)
print(res)
#res에 type함수의 반환값을 넣을 수 있을까?

#str
a = 123
res = str(a)
print(res*10)
#숫자를 문자열로 바꿈
#문자열인지 판단하는 방법  => *10
#문자를 문자열로 바꾸는 것은? => 당연히 가능

#int
a= '123'
res = int(a) #실수로 바꾸려면 => float(a)
print(res)
#문자로 표현된 숫자를 정수형으로 바꿈
# 순수 문자를 정수로 바꾸는 건? =>  당연히 불가능
# 바꾼 숫자로 계산은 당연히 가능하다 => res+1

#ord
a='A'
res = ord(a)
print(res)
#정수에 해당하는 아스키 코드 문자를 변환한다.
#a = 34로 하고 char(a*2)로 하면? => 된다!
#a = 68로 하고 char(a/2)로 하면? => 안된다!
#이유는 a/2는 자료형이 float 이기 때문


#================
#append

res = [1,2,3]
a = [1,2,3]
res= a.append(4)
print(res)
print(a)

#append의 인자를 문자열 뒤에 추가한다.
#a= [1,2,3] , res = a.append(4)
# => append가 반환값이 있는 함수가 아니므로 none

#sort
res1 = ['e','a','h']
res2 = [1,6,2]
res1.sort()
res2.sort(reverse = True) #True라고 정확히 입력해야 함
print(res1)
print(res2)
res3 = sorted(res1)
res4 = sorted(res1, reverse = True)
print(res1)
print(res2)
print(res3)
print(res4)
#sorted는 딕셔너리 정렬이 가능하다.
a = {'2 : B','1 : A', '3 :U'}
a1= sorted(a)
print(a)

#insert
res = [100,123,123]
res.insert(1,2)
print(res)
#특정 인덱스의 값이 되도록 요소를 추가한다.
#계산값을 넣어도 된다.

#remove

res = [10,20,30,40]
res.remove(10)
print(res)
# 함수의 인자값을 찾아서 삭제한다.
# 값이 여러개라면? => 가장 첫번쨰 요소를 삭제한다.

# pop
res = [10,20,30,40]
a = res.pop() #반환값이 있게요? 없게요? => 있어요
print(a)
#마지막 요소를 삭제하는 함수
#반환값이 있으므로 변수에 pop한 값을 저장할 수 있음

#count
a = [10,10,101,102,10,'ab']
res = a.count(10)
print(res)
#함수의 인자값을 찾아서개수를 센다.

#딕셔너리 함수


#keys
a = {'a' : 123, 'b': 456}
res = a.keys
print(res)
#딕셔너리의 key 값을 반환한다.

#value
a= {'a' : 123, 'b': 456}
res = a.value
print(res)

#itmes
a = {'a' : 123, 'b': 456}
res = a.itmes
print(res)

#딕셔너리의 key들을 반환하다.
#dict~~라는 말을 업생고 싶다면? => list를 활용한다.

#get
a = {'q' : 123, 'w' : 456}
res = a.get(q)
print(res) #1
print(a['t'])#2 운래 t -> q

#1과 2 둘의 차이는? 키가 없는것을 반환한다면?
#get 함수를 쓸 떄 키가 없는 값을 찾으면 none
#그냥 딕션러ㅣ에서 키 값으로 찾았을 때 없으면 오류
#get 함수는 키 값이 있ㄷ다면 그 value를 반환해도
#없다면 기본값을 지정하여 반환할 수 있다.

#in
a = {'q': 123, 'w' : 456}
print('q' in a)
#키 값이 있는 없는지 검사
#있으면 True, 없으면 False
#이 결과를 가지고 if(~~~~~==True)
