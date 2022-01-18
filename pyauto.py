import pyautogui as pg
import time
print(pg.position())
i = 8881
#while i != 8885:
def pull(i):
    a = 0
    x = 0
    while x!= 20:
        i -= 1
        a+=1
        x +=1
        n = i-a
        time.sleep(2)
        pg.moveTo(909,440)
        pg.leftClick()
        time.sleep(1)
        pg.moveTo(913, 361)
        pg.doubleClick()

        pg.typewrite(str(n))
        pg.moveTo(1422, 409)
        pg.leftClick()
        time.sleep(1)
        pg.moveTo(844,362)
        time.sleep(1)
        pg.doubleClick()
        time.sleep(1)
        i += 1
        pg.typewrite(str(n+1))

        pg.moveTo(902, 362)
        pg.doubleClick()
        time.sleep(1)
        pg.typewrite(str(n+1))
        time.sleep(1)
        pg.moveTo(981, 358)
        pg.doubleClick()
        time.sleep(1)
        pg.typewrite(str(n+1))
        time.sleep(1)
        pg.moveTo(1397, 344)
        pg.leftClick()

pull(8875)