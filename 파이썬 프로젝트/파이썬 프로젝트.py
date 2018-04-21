import random
import sys

#주사위를 굴렸을 때 확률, 기댓값, 분산, 표준편차
while(1):

    arr = [0]*6
    E = 0
    V = 0

    i = 1

#예외처리
    while(i):
        try:
            roll = int(input('주사위 돌리세요(종료 = 0) : '))    # 주사위 굴리기
        except:                                                               #입력된 값이 정수가 아닐경우         
            print("정수만 입력하세요.")
        else:
            i = 0            
        finally:                                                                #0이면 종료
            if (roll < 1):
                sys.exit(1)
                
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
