def leap_year(year):
    if 999 < year < 10000:
        return year % 400 == 0 or year % 4 == 0 and year % 100 != 0
    else:
        return "Enter a four digit number"


if __name__ == "__main__":
    y = int(input("Enter a year"))
    is_leap_year = leap_year(y)
    print(is_leap_year)