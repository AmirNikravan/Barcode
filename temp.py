import jdatetime
from datetime import datetime

# Example Gregorian date as string
gregorian_date_str = "2024/07/16"

# Parse Gregorian date string to datetime object
gregorian_date = datetime.strptime(gregorian_date_str, "%Y/%m/%d").date()

# Convert Gregorian date to Persian date
persian_date = jdatetime.date.fromgregorian(date=gregorian_date)

# Get year, month, day from Persian date
year = persian_date.year
month = persian_date.month
day = persian_date.day

print(f"Persian Date: {year}/{month}/{day}")
