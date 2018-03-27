'''a = input()
b = input()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print("%.2f" %(a/b)) #formatting C언어랑 다른점은 %
print(int(a/b))
print(a%b)'''

'''a,b = input().split() #한 줄 입력이 가능해진다.
#입력을 받아서 각 변수에 정수로 mappin
print(a+b)
print(a-b)
print(a*b)
print("%.2f" %(a/b)) 
print(int(a/b))
print(a%b) '''

a,b =  map(int, input().split)
print(a+b, a-b, a*b, "%.2f" %(a/b), a//b, sep = '\n')

