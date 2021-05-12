from datetime import datetime
import time
price = float(10.55)

txt = "The price is £{}"

print(txt.format(price))

fullName = "John Smith"
accountNum = float(1986253.468674)

message = "Welcome {1}. Account number is {0:.2f}"

print(message.format(accountNum, fullName))

# random()


for num in range(0, 5):
    print(num)
    time.sleep(2)

print(datetime.today())
