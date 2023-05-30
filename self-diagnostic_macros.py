import pyautogui
import time
import os
import sys
import clipboard
import telegram
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Ready
mode_type = 0
chrome_options = Options()

name = ''
school = ''
date_birth = ''

token = '' # telegram bot token
bot = telegram.Bot(token=token)

# 동작 1 - 모니터 해상도 검사, 기능실 컴퓨터인 1920x1080에서만 동작
print('Check monitor resolution...')
monitor_width, monitor_height=pyautogui.size()
if monitor_width == 1920 and monitor_height == 1080:
    mode_type += 1

# 동작 2 - 전체화면으로 브라우저 띄우고 사이트 접속
if mode_type == 1:
    chrome_options.add_argument('--start-fullscreen')
    driver = webdriver.Chrome('C:/Python_driver/chromedriver.exe', options=chrome_options)
    driver.get('https://hcs.eduro.go.kr/#/loginHome')
    # 동작 3 - 자가진단 참여하기 Go 이미지를 인식해서 클릭
    time.sleep(3)
    print('running...')
    pyautogui.click(x=950, y=632)
    # 동작 4 - 자가진단 참여하는 포인트로 이동해서 완료
    time.sleep(1)
    pyautogui.click(x=1189, y=486)
    time.sleep(1)
    pyautogui.click(x=1114, y=309)
    time.sleep(1)
    pyautogui.click(x=837, y=935)
    time.sleep(1)
    pyautogui.click(x=890, y=391)
    time.sleep(1)
    pyautogui.click(x=865, y=600)
    time.sleep(1)
    pyautogui.click(x=879, y=513)
    time.sleep(1)
    clipboard.copy (school)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(x=1647, y=491)
    time.sleep(1)
    pyautogui.click(x=795, y=626)
    time.sleep(1)
    pyautogui.click(x=900, y=858)
    time.sleep(1)
    pyautogui.click(x=987, y=596)
    time.sleep(1)
    clipboard.copy(name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(x=909, y=728)
    time.sleep(1)
    clipboard.copy(date_birth)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(x=958, y=906)
    time.sleep(1)
    pyautogui.click(x=880, y=520)
    time.sleep(1)
    pyautogui.typewrite('****') # password
    time.sleep(1)
    pyautogui.click(x=946, y=648)
    time.sleep(1)
    pyautogui.click(x=593, y=775)
    time.sleep(2)
    pyautogui.scroll(-1000)
    time.sleep(2)
    pyautogui.click(x=190, y=426)
    time.sleep(1)
    pyautogui.click(x=197, y=615)
    time.sleep(1)
    pyautogui.click(x=194, y=872)
    time.sleep(1)
    pyautogui.click(x=855, y=973)
    # 동작 4 - 텔레그램 봇을 이용해서 자가진단을 완료했다고 보냄
    bot.sendMessage(chat_id='1561438894', text='건강상태 자가진단을 완료했습니다.')


    

    
    
    
    
    
    


