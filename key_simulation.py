import pyautogui
import time
from prev_week import previous_week, week_before_last
import credential as c

file_names = []


def open_chrome():
    pyautogui.hotkey('command', 'space')
    pyautogui.typewrite("chrome", interval=0.1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('shift', 'command', 'N')


def beeline_login(url, user, pwd):
    time.sleep(3)
    pyautogui.typewrite(url, interval=0.09)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(user)
    pyautogui.press('tab')
    pyautogui.typewrite(pwd)
    pyautogui.press('enter')
    time.sleep(5)


def save_time_sheet():
    saturday, sunday = previous_week()
    last_saturday, last_sunday = week_before_last()
    lst = [[saturday, sunday], [last_saturday, last_sunday]]
    for i in range(len(lst)):
        pyautogui.press('tab', presses=9+(i*3), interval=0.09)
        time.sleep(1)
        pyautogui.press('enter', presses=(i + 1), interval=0.09)
        time.sleep(1)
        pyautogui.hotkey('command', 'p')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.typewrite(f'TimeSheet({lst[i][1]} to {lst[i][0]})', interval=0.1)
        pyautogui.press('enter')
        file_names.append(f'TimeSheet({lst[i][1]} to {lst[i][0]})')


def mail_login(url, user, pwd):
    pyautogui.hotkey('command', 't')
    time.sleep(5)
    pyautogui.typewrite(url, interval=0.04)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.typewrite(user)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite(pwd)
    pyautogui.press('enter')
    time.sleep(10)


def send_email():
    pyautogui.press('tab', presses=11, interval=0.09)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.typewrite(c.mail_to, interval=0.09)
    pyautogui.press('tab', presses=2, interval=0.1)
    pyautogui.typewrite('Time Sheets', interval=0.09)
    pyautogui.press('tab', interval=0.9)
    pyautogui.typewrite('Attached are the time sheets of past two weeks.')
    for i in range(len(file_names)):
        time.sleep(i+1)
        pyautogui.press('tab', presses=3, interval=0.09)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('command', 'f')
        pyautogui.typewrite(file_names[i], interval=0.09)
        time.sleep(1)
        pyautogui.click(x=451, y=254, clicks=2)
        pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey('command', 'enter')


if __name__ == '__main__':
    open_chrome()
    beeline_login(c.beeline_host, c.beeline_name, c.beeline_pass)
    save_time_sheet()
    time.sleep(3)
    mail_login(c.mail_host, c.mail_name, c.mail_pass)
    send_email()

