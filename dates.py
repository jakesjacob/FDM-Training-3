from datetime import datetime

strDate = "20 December 2020"
print("original date: ", strDate)
datetimeDate = datetime.strptime(strDate, "%d %B %Y")
print("Converted date: ", datetimeDate)

strictDate = datetimeDate.strftime("%Y-%m-%d")
print("Converted date - strict date: ", strictDate)

strictDate2 = datetimeDate.strftime("%A %y %a")
print("Converted date - strict date: ", strictDate2)
