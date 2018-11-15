from subprocess import run
from opencvloc import locateCenterImage
import pyautogui as py#라이브러리 대체
import time

run(['calc'])

time.sleep(1)

x,y = locateCenterImage('2.png')
py.click(x,y)

x,y = locateCenterImage('x.png')
py.click(x,y)

x,y = locateCenterImage('3.png')
py.click(x,y)

x,y = locateCenterImage('=.png')
py.click(x,y)