import calendar

month, day, year = input().split()
i = calendar.weekday(int(year), int(month), int(day))
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[i])
