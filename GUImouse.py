import pyautogui
print(pyautogui.size())
print(pyautogui.position())

pyautogui.moveTo(10, 10, duration = 0.5)
pyautogui.moveRel(200, 0, duration = 0.5)
pyautogui.moveRel(200, 400, duration = 0.5)
pyautogui.click(335, 50)
pyautogui.click(335, 50)
pyautogui.moveTo(200, 400, duration = 0.5)
pyautogui.click()

#if you move the mouse to the top left (0, 0) the failsafe will stop the program
