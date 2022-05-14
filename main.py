import pyautogui
from time import sleep

LETTER="a"
INTERVAL=0.003

def combo_start_up():
    for x in range(6):
        pyautogui.typewrite(LETTER*10, interval=INTERVAL)
        sleep(INTERVAL)
        pyautogui.typewrite(["enter"])
        sleep(INTERVAL)

def write_x_amount_for_achievement(x):
    pyautogui.typewrite(LETTER*x, interval=INTERVAL)
    sleep(INTERVAL)
    pyautogui.typewrite(["enter"])
    sleep(INTERVAL)

if __name__ == "__main__":
    print("Starting in 5...")
    sleep(5)
    combo_start_up()
    write_x_amount_for_achievement(64)
    write_x_amount_for_achievement(99)
    write_x_amount_for_achievement(1337)