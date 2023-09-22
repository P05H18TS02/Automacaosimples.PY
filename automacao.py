import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 3

pa.press('win')
pa.write("chrome")
pa.press('ENTER')
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(4)
pa.click(x=634, y=860)
pyperclip.copy("Você Sabia?")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')

