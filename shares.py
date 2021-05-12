import random
import time
from datetime import datetime

share1 = float(1.0)


def updateShares():
    global share1
    if random.random() > 0.35:
        share1 = share1 + random.random()
    else:
        share1 = share1 - random.random()
    print(share1)


for num in range(0, 50):
    updateShares()
    time.sleep(1)
