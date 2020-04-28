""" A program to read the contents of the file and calculate
    how many emails are sent each day of the week, Sunday through Saturday. (matplotlib)

    author: Fatih IZGI
    date: 26-Apr-2020
    python: v3.8.2
"""

from datetime import datetime
from typing import IO, Dict
import re
import matplotlib.pyplot as plt


file_name: str = input("Enter a file name: ")

weekday_map: Dict[int, str] = {6: "Sun", 0: "Mon", 1: "Tue", 2: "Wed",
                               3: "Thu", 4: "Fri", 5: "Sat"}  # Sunday through Saturday

dates: Dict[str, int] = {key: 0 for key in weekday_map.values()}  # container to count the emails

try:  # to open the file
    path: IO = open(file_name, "r")
except FileNotFoundError:
    print(f"File {file_name} is not found")
else:
    with path:  # close path after opening
        for line in path:
            if re.match(r'Date: \d{4}-\d{2}-\d{2}', line):  # if the line is in a specific format
                match = re.findall(r'\d{4}-\d{2}-\d{2}', line)  # extract the date(s) only
                date = datetime.strptime(match[0], "%Y-%m-%d")  # get the first (and the only) date
                dates[weekday_map[date.weekday()]] += 1  # increase the counter
                # I used to wrap the above 3 lines of code with try except block to check
                # if there is a corrupted data, but here no need to do it as I have already
                # checked it on line 29 if it starts with "Date: " and followed by a date (Y-m-d)
                # so I am working on an well-formatted data and no need to catch an exception here.

    plt.title("Emails sent each day of the week")
    plt.bar(list(dates.keys()), list(dates.values()))  # set the bar values
    for index, value in enumerate(dates.values()):
        plt.text(index, value, str(value))  # show values on top of each bar

    plt.show()
