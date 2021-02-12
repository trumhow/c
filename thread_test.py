import threading

def func(x):
    while True:
        print('get number', x)

for i in range(8):
    threading.Thread(target=func, args=(i,)).start()
