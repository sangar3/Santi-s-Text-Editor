import threading
import time


def func():
    print('ran')
    time.sleep(1) #goes to line 16 while sleeping
    print('done')
    time.sleep(.85)
    print("now done")


x = threading.Thread(target=func)

x.start()  # calls the x thread thats a seprate fro the main thread
print(threading.activeCount())
time.sleep(.9) # sleep number is lower than line 7 sp finally prints first
print('finally')