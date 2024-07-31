import pyautogui
import time
from pynput import keyboard

 # コードを中止か判断するためのフラグ

break_flag = False #初期化

# コードを中止する文字'q'が入力されたか判定する関数
def on_press(key):
    global break_flag
    try:
        if key.char == 'q':
            break_flag = True
            return False
    except AttributeError:
        pass


listener = keyboard.Listener(on_press=on_press) #初期化
listener.start()

while break_flag == False: #qが押されるまでループ
    print('roop')

break_flag = False #初期化
listener = keyboard.Listener(on_press=on_press)
listener.start()

for i in range(30):  # ここが消し込みの回数
    if break_flag: # 中止するかどうか判定
        break

    pyautogui.doubleClick()
    pyautogui.press('f1')
    pyautogui.press('y')
    time.sleep(2)  # yを押した後に少しまつ

    print(i)