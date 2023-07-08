import calendar

print("Welcome to the Calendar Generator App")
user_want_continue = True
while user_want_continue:
    yy = input("Enter a year (YYYY): ")
    mm = input("Enter a month (MM): ")

    if not yy.isdigit() or not mm.isdigit():
        print("Invalid input. Please enter a valid year and month.")
    else:
        yy = int(yy)
        mm = int(mm)
        if mm < 1 or mm > 12:
            print("Invalid month. Please enter a value between 1 and 12.")
        else:
            print(calendar.month(yy, mm))
            user_want_continue = False

