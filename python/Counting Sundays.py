monthsDays = [30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
yearsPast = 0
daysPast = 0
curMonth = 0
curDayIndex = 1
year = 1901
answer = 0
while year <= 2000:
    curDayIndex = (curDayIndex + 1) % 7
    daysPast += 1
    if daysPast > monthsDays[curMonth]:
        daysPast = 0
        curMonth += 1
    if curMonth >= 12:
        year += 1
        curMonth = 0
        yearsPast += 1
        if not yearsPast % 4:
            monthsDays[1] = 29
        else:
            monthsDays[0] = 28
    if curDayIndex == 6 and daysPast == 0:
        answer += 1
print(answer-1)
