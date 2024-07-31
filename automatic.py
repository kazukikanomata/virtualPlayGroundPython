import pyautogui
import time
from pynput import keyboard

 # コードを中止か判断するためのフラグ

print('Please type your number of roop and press enter')
n = int(input()) #ループ回数の入力を受け取る



break_flag = False #中止、開始フラグの初期化

# コードを中止する文字'q'が入力されたか判定する関数
def on_press(key):
    global break_flag
    try:
        if key.char == 'q':
            break_flag = True
            return False
    except AttributeError:
        pass



listener = keyboard.Listener(on_press=on_press) #中止、開始フラグの読み込み準備
listener.start()

while break_flag == False: #qが押されたらループ脱出して次の動作
    print('roop')

break_flag = False #中止、開始フラグの再初期化
listener = keyboard.Listener(on_press=on_press)#中止、開始フラグの再読み込み準備
listener.start()

#stime.sleep(5)

for i in range(n):  # ここから先が消し込み作業のプログラム文
    if break_flag: # 中止するかどうか判定
        break

    pyautogui.doubleClick()
    pyautogui.press('f1')
    pyautogui.press('y')
    time.sleep(1.8)  # yを押した後に少しまつ
    pyautogui.press('f10')

    print(i)

print('stopped')