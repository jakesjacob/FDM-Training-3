from threading import Thread
from time import sleep

result = None


def update_every_second():
    while result is None:
        sleep(1)
        print("update")


t = Thread(target=update_every_second)
t.start()
result = input('? ')

print("The user typed"), result
