import random
import time
import schedule

share1 = float(1.0)
share2 = float(1.0)
share3 = float(1.0)
share1rounded = float(1.0)
share2rounded = float(1.0)
share3rounded = float(1.0)

share1List = []


def shareShift():


def updateShares():
    global share1
    global share2
    global share3
    global share1rounded
    global share2rounded
    global share3rounded
    if random.random() > 0.35:
        share1 = share1 + random.uniform(0.1, 0.6)
    else:
        share1 = share1 - random.uniform(0.1, 0.6)

    if random.random() > 0.45:
        share2 = share1 + random.uniform(0.1, 0.7)
    else:
        share2 = share1 - random.uniform(0.1, 0.7)

    if random.random() > 0.4:
        share3 = share3 + random.uniform(0.1, 0.8)
    else:
        share3 = share3 - random.uniform(0.1, 0.8)

    share1rounded = round(share1, 2)
    share2rounded = round(share2, 2)
    share3rounded = round(share3, 2)


schedule.every(1).seconds.do(updateShares)


def updateAllShares():
    schedule.run_pending()
