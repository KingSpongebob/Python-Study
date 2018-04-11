''' a= input()
b = input()
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print("%.2f" %(a/b))  # formating c언어랑 다른 점은 %
print(int(a/b))
print(a%b) '''


#2
'''
a,b = input().split() #한 줄 입력이 가능해진다.
a=int(a)
b=int(b)
print(a+b)
print(a-b)
print(a*b)
print("%.2f" %(a/b))  # formating c언어랑 다른 점은 %
print(int(a/b))
print(a%b)'''


#3

a,b = map(int, input().split())
print(a+b,a-b,a*b, "%.2f" %(a/b), a//b, a%b, sep='\n')    
