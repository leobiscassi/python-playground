def is_leap(year):
    leap = False

    if not (not ((year % 4 == 0) and not (year % 100 == 0)) and not ((year % 100 == 0) and (year % 400 == 0))):
        leap = True

    return leap


year = int(input())
print(is_leap(year))