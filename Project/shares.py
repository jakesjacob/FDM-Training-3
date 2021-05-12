import random
import time
import schedule

share1 = float(1.0)


def updateShares():
    global share1
    if random.random() > 0.35:
        share1 = share1 + random.random()
    else:
        share1 = share1 - random.random()
    # print(share1)


schedule.every(1).seconds.do(updateShares)


def updateAllShares():
    schedule.run_pending()
