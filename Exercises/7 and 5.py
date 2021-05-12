
string = ""
count = 100

while count < 204:
    if count % 7 == 0 and count % 5 != 0:
        string = string + str(count) + ", "
    count += 1

print(string)


num = 100
list = []

while num in range(100, 204):
    if num % 7 == 0 and num % 5 != 0:
        list.append(num)

    num += 1

print(list)
