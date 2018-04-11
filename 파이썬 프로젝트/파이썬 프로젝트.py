#1차

import random

arr = [0]*6
E = 0
V = 0

# 주사위 굴리기
roll = int(input('주사위 돌리세요 : '))
for i in range(roll):
    arr[random.randint(0,5)]+=1

# 확률 구하기
pro = [a/roll for a in arr]

# 기댓값 구하기
for i in range(6) :
    E += pro[i] * (i+1)

#분산 구하기
for i in range(6) :
    V += (((i+1) - E)**2)*pro[i]

#표준편차
S = V**0.5

print(' 확률     :', pro)
print(' 기댓값   :', E)
print(' 분산     :', V)
print(' 표준편차 :', S)
