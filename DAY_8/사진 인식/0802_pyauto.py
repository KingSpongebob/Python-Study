#pyautogui library test

import pyautogui

# size
# 화면의 크기를 반환하는 'pyautogui 라이브러리' 함수 

scrWD, scrHE = pyautogui.size()

print(scrWD, scrHE)


# click
# 딱 봐도 클릭하는 함수
# 옵션을 통해 횟수와 버튼 지정 가능
# x, y => 마우스 위치 이동
# clicks => 마우스 클릭 횟수
# interval => 클릭 간격 조정(값 : second)
# button => 마우스 버튼 위치 선택(left, right)

# pyautogui.click(x=scrWD/3, y=scrHE/2, button='left')


# typewrite
# 키를 입력하는 함수
# 지금은 영어만 입력할 수 있음.
# pyautogui.typewrite('calc')


# press
# 특수키를 입력할 때 사용하는 함수
# pyautogui.press('enter')


# locateCenterOnScreen
# 그림과 일치하는 위치의 좌표 반환 함수
# 그림파일을 png로 설정해야 함.
lx, ly = pyautogui.locateCenterOnScreen('test.png')
pyautogui.moveTo(lx, ly)

# 역시 안 되는군 ^^^^^^^^^
# 이 함수는 다른 매크로나 자동 동작에 있어서 인식률이 낮다.