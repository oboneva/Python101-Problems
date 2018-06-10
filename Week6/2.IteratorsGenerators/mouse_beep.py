import pyautogui


def main():
    i = 0
    while True:
        position = pyautogui.position()
        if position == (0, 0):
            print(i)
            i += 1

if __name__ == '__main__':
    main()
