import threading


class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


x = Messenger(name='Send messages')
y = Messenger(name='Recieve messages')
x.run()
y.run()
# thread is not working
